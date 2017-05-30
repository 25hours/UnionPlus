from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField(verbose_name='邮箱地址',max_length=255,unique=True)
    phone = models.BigIntegerField(blank=True,null=True)
    password = models.CharField(u'密码',max_length=128)
    is_admin = models.BooleanField(default=False)
    # is_staff = models.BooleanField(
    #     verbose_name='staff status',
    #     default=True,
    #     help_text='Designates whether the user can log into this admin site.',
    # )
    #role = models.ForeignKey("Role",verbose_name="权限角色")
    memo = models.TextField('备注', blank=True, null=True, default=None)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['name','token','department','tel','mobile','memo']
    # REQUIRED_FIELDS = ['name']

    # def get_full_name(self):
    #     # The user is identified by their email address
    #     return self.email
    #
    # def get_short_name(self):
    #     # The user is identified by their email address
    #     return self.email

    def __str__(self):  # __str__ on Python 2
        return u"%s,%s" %(self.email,self.is_admin)

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True
    # def has_perms(self, perm, obj=None):
    #     "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        # return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        # return True


    # @property
    # def is_superuser(self):
    #     "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        # return self.is_admin


    # objects = auth.UserManager()

    class Meta:
        verbose_name = ('用户信息')
        verbose_name_plural = ('用户信息')