from rest_framework import generics, mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .mixins import CreateUserMixin
from .paginators import UsersCustomPagination
from .serializers_follow import FollowerSerializer
from .serializers_user import (ChangePasswordSerializer, UserInfoSerialiser,
                               UserRegistrationSerializer, UsersListSerialiser)

User = get_user_model()


class UpdatePassword(APIView):
    '''
        Смена пасса. Post запрос.
    '''
    permission_classes = (IsAuthenticated, )

    def _get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self._get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            
            current_password = serializer.validated_data.get(
                "current_password"
            )
            if not self.object.check_password(current_password):
                return Response({"current_password": ["Неверный пароль!"]},
                                status=status.HTTP_400_BAD_REQUEST)
            
            self.object.set_password(
                serializer.validated_data.get("new_password")
            )
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


@action(detail=True, methods=["LIST", "POST"])
class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  CreateUserMixin,
                  viewsets.GenericViewSet):
    
    lookup_field = "pk"
    lookup_url_kwarg = "id"
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    pagination_class = UsersCustomPagination

    def get_serializer_class(self):
        if self.action in ("me"):
            return UserInfoSerialiser
        elif self.action in ("create",):
            return UserRegistrationSerializer
        else:
            return UsersListSerialiser

    def retrieve(self, request, *args, **kwargs):
        if (
            request.user.is_authenticated
            and request.user.id == int(kwargs.get('id', -1))
        ):
            print(
                "ВЫ перешли на свою страницу, "
                "а как вас редиректнуть на me - я хз"
            )
        return super().retrieve(request, *args, **kwargs)

    @action(
        detail=False,
        methods=["get", ],
        permission_classes=[IsAuthenticated],
    )
    def me(self, request):
        user = request.user
        if request.method == "GET":
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = self.get_serializer(
            user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubscribeViewset(APIView):
    """Подписка - отписка (POST - DELETE запрос)
    """
    permission_classes = (IsAuthenticated,)

    def _get_author_and_user(self, request, author_id):
        return(
            get_object_or_404(User, id=author_id),
            request.user
        )

    
    def _check_user_is_author(self, user, author):
        return user == author

    def _check_user_is_trying_to_follow_himself(self, user, author):
        is_trying = self._check_user_is_author(user, author)
        message = (
            {
                "error":
                "Невозможно подписаться на самого себя!"
            } if is_trying else {}
        )
        return (is_trying, message)

    def _check_user_is_trying_to_unfollow_himself(self, user, author):
        is_trying = self._check_user_is_author(user, author)
        message = (
            {
                "error":
                "Невозможно отписаться от самого себя!"
            } if is_trying else {}
        )
        return (is_trying, message)

    def _check_user_is_not_following_author(self, user, author):
        is_not_following = not user._is_following(author)
        message = (
            {
                "error":
                "Невозможно отписаться, вы не были подписаны "
                f"на {author}!"
            } if is_not_following else {}
        )
        return(is_not_following, message)

    def _check_user_is_following_author(self, user, author):
        is_following = user._is_following(author)
        message = (
            {
                "error":
                "Невозможно подписаться, вы уже подписаны "
                f"на {author}!"
            } if is_following else {}
        )
        return(is_following, message)

    def _send_error_message(
        self, first, first_messare,
        second, second_message
    ):
        if first or second:
            message = (
                first_messare if first
                else second_message
            )
            return (
                True,
                Response(
                    message,
                    status=status.HTTP_400_BAD_REQUEST
                )
            )
        return False, None

    
    def post(self, request, author_id):
        author, user = self._get_author_and_user(request, author_id)
        is_following, message_is_following = (
            self._check_user_is_following_author(user, author)
        )

        (
            is_trying_to_follow_himself,
            message_is_trying_to_follow_himself
        ) = (
            self._check_user_is_trying_to_follow_himself(user, author)
        )

        send, response = self._send_error_message(
            is_trying_to_follow_himself,
            message_is_trying_to_follow_himself,
            is_following, message_is_following
        )
        if send:
            return response

        user._follow(author)
        serializer = FollowerSerializer(author, context={'request': request})
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    
    def delete(self, request, author_id):
        author, user = self._get_author_and_user(request, author_id)
        is_not_following, message_is_not_following = (
            self._check_user_is_not_following_author(user, author)
        )

        (
            is_trying_to_unfollow_himself,
            message_is_trying_to_unfollow_himself
        ) = (
            self._check_user_is_trying_to_unfollow_himself(user, author)
        )

        send, response = self._send_error_message(
            is_trying_to_unfollow_himself,
            message_is_trying_to_unfollow_himself,
            is_not_following, message_is_not_following
        )
        if send:
            return response
        user._unfollow(author)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListSubscriptions(generics.ListAPIView):
    """ Список подписок, GET запрос """
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowerSerializer
    pagination_class = UsersCustomPagination

    def get_queryset(self):
        user = self.request.user

        user_is_follower = user.follower.all()
        return User.objects.filter(
            id__in=user_is_follower.values('author')
        ).all()