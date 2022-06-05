
from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError

from .models import Follow

User = get_user_model()



class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user



class UserChangeForm(forms.ModelForm):
    

    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'first_name',
                  'last_name', 'is_active', 'role', 'is_staff')

    


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    
    add_form = UserCreationForm

    list_display = (
        'email', 'username', 'first_name',
        'last_name', 'role', 'is_staff'
    )
    list_filter = ('role', 'email', 'username')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('role', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name',
                       'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('^email', '^username')
    ordering = ('email',)
    filter_horizontal = ()


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('author', 'user')


admin.site.unregister(Group)
admin.site.register(Follow, SubscriptionAdmin)