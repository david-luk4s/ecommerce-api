from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class UserManager(BaseUserManager):
    def _create_user(self,email, password, phone, is_staff, is_superuser, **extra_fields):
        """Cria e salva um usuário com o email fornecido e senha 
        """
        if not email:
            raise ValueError('Necessário email para usuário')
        
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            phone = phone,
            is_active = True,
            is_staff = is_staff, 
            is_superuser = is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False,**extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        user=self._create_user(email, password, True, True,**extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    #Fields relations to acess login
    email = models.EmailField('Email', max_length=100, unique = True)
    phone = models.CharField('Telefone', max_length=15, null=True, blank=True)
    username = models.CharField('Nome', max_length=50, blank=True)
    is_active = models.BooleanField('Ativo', default=True)
    is_staff = models.BooleanField('Acesso Admin', default=False)
    is_superuser = models.BooleanField('Super Admin', default=False)
    date_register = models.DateTimeField('Data registro', auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['']
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
