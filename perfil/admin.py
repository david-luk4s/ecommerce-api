from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, ReadOnlyPasswordHashWidget
from .models import User


class UserCreationForm(forms.ModelForm):
    """Um formulário para criar novos usuários. Inclui todos os requisitos
    campos, além de uma senha repetida. """

    password1 = forms.CharField(label = 'Senha', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirmação Senha', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username')
    
    def clean_password2(self):
        # Verifique se as duas entradas de senha correspondem
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2 :
            raise forms.ValidationError('Password não correspondem')

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """Um formulário para atualizar usuários. Inclui todos os campos em
    o usuário, mas substitui o campo de senha por admin
    campo de exibição hash da senha.
    """
    
    password = ReadOnlyPasswordHashField(label=('Password'), help_text=('Raw passwords are not stored, so there is no way to see this user password, but you can change the using <a href=\'../password/\'>This form</a>'))

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_active', 'is_staff')

    def clean_password(self):
        # Independentemente do que o usuário fornece, retorne o valor inicial.
        # Isso é feito aqui, ao invés de no campo, porque o
        # field não tem acesso ao valor inicial
        return self.initial['password']

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email','username','phone', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_superuser', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Dados do Usuário', {'fields': ('username', 'phone')}),
        ('Permissão',     {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups' )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone', 'groups','password1', 'password2')
        }),
    )

    # search_fields = ('email')
    # ordering = ('email')
    # filter_horizontal = ()

admin.site.register(User, UserAdmin)