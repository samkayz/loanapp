from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, UserManager, BaseUserManager
from django.http import request
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.sessions.models import Session
import os


identification = FileSystemStorage(location=os.path.join('media/identification'))
profile = FileSystemStorage(location=os.path.join('media/profile'))


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    fullname = models.TextField("fullname", null=True, blank=True)
    mobile = models.CharField(verbose_name='mobile', max_length=100, null=True, blank=True)
    is_manager = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_staff = models.BooleanField(verbose_name='is_staff', default=True)
    date_joined = models.DateTimeField(
        verbose_name='date_joined', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='is_active', default=True)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['fullname']

    class Meta:
        db_table = 'user'

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.email)



class AccountInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_no = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)
    address = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)
    means_of_id = models.CharField(max_length=100, null=True, blank=True)
    mid_image = models.FileField(upload_to=identification, null=True, blank=True)
    profile_image = models.FileField(upload_to=profile, null=True, blank=True)

    class Meta:
        db_table = 'account_info'
    

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.user)



class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    session = models.OneToOneField(Session, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_session'

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.user)


class EmailConfig(models.Model):
    name = models.CharField(default='email', max_length=10)
    port = models.BigIntegerField(null=True, blank=True)
    is_tls = models.BooleanField(null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    host = models.CharField(max_length=100, null=True, blank=True)
    default_email = models.EmailField(null=True, blank=True)

    class Meta:
        db_table = 'email_config'
    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)