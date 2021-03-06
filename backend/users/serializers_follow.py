from rest_framework import serializers

from django.contrib.auth import get_user_model

from recipes.models import Recipe
from recipes.serializers import FavoritORInShopingCartRecipeSerializer

from .models import Follow

User = get_user_model()




class FollowerSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField()
    first_name = serializers.ReadOnlyField()
    last_name = serializers.ReadOnlyField()
    is_subscribed = serializers.SerializerMethodField()
    recipes = serializers.SerializerMethodField()
    recipes_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'email', 'id', 'username', 'first_name', 'last_name',
            'is_subscribed', 'recipes', 'recipes_count'
        )

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False
        return Follow.objects.filter(
            user=request.user, author=obj
        ).exists()

    def get_recipes(self, obj):
        request = self.context.get('request')
        limit = request.GET.get('recipes_limit')
        queryset = Recipe.objects.filter(author=obj).all()
        if not queryset.exists():
            return None

        if limit is not None:
            queryset = Recipe.objects.filter(
                author=obj
            )[:int(limit)]

        return FavoritORInShopingCartRecipeSerializer(
            queryset, many=True
        ).data

    def get_recipes_count(self, obj):
        return Recipe.objects.filter(author=obj).count()