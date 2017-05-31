from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('必须输入邮件地址')

        user = self.model(
            email = self.normalize_email(email),
            name = name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email,password=password,name=name,)
        user.is_admin = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='邮件地址',
        max_length=255,
        unique=True,
    )
    # date_of_birth = models.DateField()
    name = models.CharField(u'用户名',max_length=32)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(u'管理员',default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin