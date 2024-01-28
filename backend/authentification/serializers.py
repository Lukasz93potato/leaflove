from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirmedPassword = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'confirmedPassword')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True}
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value

    def validate(self, data):
        if data['password'] != data['confirmedPassword']:
            raise serializers.ValidationError("Passwords must match.")
        validate_password(data['password'])
        return data

    def create(self, validated_data):
        validated_data.pop('confirmedPassword')
        user = User.objects.create_user(
            username=validated_data['email'],  # Używamy e-mail jako nazwy użytkownika
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

# from rest_framework import serializers
# from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import validate_password
#
# class UserRegistrationSerializer(serializers.ModelSerializer):
#     confirmedPassword = serializers.CharField(write_only=True, required=True)
#
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'password', 'confirmedPassword')
#         extra_kwargs = {
#             'first_name': {'required': True},
#             'last_name': {'required': True},
#             'password': {'write_only': True}
#         }
#
#     def validate_email(self, value):
#         if User.objects.filter(email=value).exists():
#             raise serializers.ValidationError("Email is already in use.")
#         return value
#
#     def validate(self, data):
#         if data['password'] != data['confirmedPassword']:
#             raise serializers.ValidationError("Passwords must match.")
#         validate_password(data['password'])
#         return data
#
#     def create(self, validated_data):
#         validated_data.pop('confirmedPassword')
#         user = User.objects.create_user(
#             email=validated_data['email'],
#             password=validated_data['password'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name']
#         )
#         user.username = validated_data['email']
#         user.save()
#         return user

# from rest_framework import serializers
# from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import validate_password
#
# class UserRegistrationSerializer(serializers.ModelSerializer):
#     confirmedPassword = serializers.CharField(write_only=True, required=True)
#
#     class Meta:
#         model = User
#         fields = ('name', 'name', 'email', 'password', 'confirmedPassword')
#         extra_kwargs = {
#              'first_name': {'source': 'name'},
#              'last_name': {'source': 'surname'}
#         }
#
#     def validate_email(self, value):
#         if User.objects.filter(email=value).exists():
#             raise serializers.ValidationError("Email is already in use.")
#         return value
#
#     def validate(self, data):
#         if data['password'] != data['confirmedPassword']:
#             raise serializers.ValidationError("Passwords must match.")
#         validate_password(data['password'])
#         return data
#
#     def create(self, validated_data):
#         validated_data.pop('confirmedPassword')
#         return User.objects.create_user(
#             username=validated_data['email'],  # Używamy e-mail jako nazwy użytkownika
#             email=validated_data['email'],
#             password=validated_data['password'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name']
#         )