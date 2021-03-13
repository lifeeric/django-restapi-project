from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


# User Config
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True
    )

    is_student = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True


# User Profile
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    name = models.CharField(max_length=100)
    bio = models.TextField(default='', blank=True)
    preferred_name = models.CharField(max_length=255, null=True)
    avatar_url = models.CharField(max_length=100, null=True)
    discord_name = models.CharField(max_length=100, null=True)
    github_name = models.CharField(max_length=100, null=True)
    codepen_username = models.CharField(max_length=100, null=True)
    fcc_profile_url = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=50, null=True)
    timezone = models.CharField(max_length=50, null=True)

    LEVELS = (
        (1, 'Level One'),
        (2, 'Level Two')
    )

    current_level = models.IntegerField(choices=LEVELS, default=1)

    def __str__(self):
        return f'{self.name}'
