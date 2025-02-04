from rest_framework import serializers
from .models import User, VerifyPhone, PaymentHistory, MyLanguage


class MyLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyLanguage
        fields = ('id', 'name', 'image1', 'count_lesson', 'percent')

    name = serializers.CharField(source='language.name')
    image1 = serializers.CharField(source='language.image1.url')
    count_lesson = serializers.SerializerMethodField()
    percent = serializers.SerializerMethodField()

    @staticmethod
    def get_count_lesson(obj):
        return sum([levels.units.count() for levels in obj.language.levels.all()])

    @staticmethod
    def get_level_percent(level):
        count = level.units.count()
        if count == 0:
            count = 1
        summa = sum([unit.percent for unit in level.units.all()])
        return round(summa / count, 2)

    def get_percent(self, obj):
        count = self.get_count_lesson(obj)
        if count == 0:
            count = 1
        summa = sum([self.get_level_percent(level) for level in obj.levels.all()])
        return round(summa / count, 2)


class PaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = ('name', 'amount', 'created_at')


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone', 'first_name', 'last_name', 'age', 'created_at')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'phone', 'password', 'confirm_password')

    confirm_password = serializers.CharField(max_length=128)

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Passwords don't match.")
        del attrs['confirm_password']
        return attrs


class VerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyPhone
        fields = ('phone', 'code')


class SendVerificationCodeSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12)
