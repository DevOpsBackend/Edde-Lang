from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from rest_framework.authtoken.models import Token
from lang.models import Language, Level, Unit


class UserManager(BaseUserManager):
    def create_user(self, phone, **kwargs):
        if not phone:
            raise TypeError('Phone did not come')
        user = self.model(phone=phone, **kwargs)
        user.save(using=self._db)
        Token.objects.create(user=user)
        return user

    def create_superuser(self, phone, password=None, **kwargs):
        if not password:
            raise TypeError('Password did not come')
        user = self.create_user(phone, **kwargs)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=12, unique=True)
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    coin = models.PositiveBigIntegerField(default=0)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.phone


class VerifyPhone(models.Model):
    phone = models.CharField(max_length=12)
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.phone


class PaymentHistory(models.Model):
    user = models.ForeignKey(User, models.CASCADE, 'payment_history')
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MyLanguage(models.Model):
    user = models.ForeignKey(User, models.CASCADE, 'my_languages')
    language = models.ForeignKey(Language, models.CASCADE)

    def __str__(self):
        return self.language.name


class MyLevel(models.Model):
    language = models.ForeignKey(MyLanguage, models.CASCADE, 'levels')
    level = models.ForeignKey(Level, models.CASCADE)

    def __str__(self):
        return self.level.name


class MyUnit(models.Model):
    level = models.ForeignKey(MyLevel, models.CASCADE, 'units')
    unit = models.ForeignKey(Unit, models.CASCADE)
    percent = models.FloatField(default=0.0)
    dialog_is_viewed = models.BooleanField(default=False)
    vocab_answer = models.JSONField(default=dict)
    phrase_answer = models.JSONField(default=dict)

    def __str__(self):
        return self.unit.name
