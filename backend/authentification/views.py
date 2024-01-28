from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from drf_yasg.utils import swagger_auto_schema

def login_page(request):
    return render(request, "login.html")

class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
        return Response(content)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    @swagger_auto_schema(request_body=UserRegistrationSerializer)
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'User registered successfully.'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'status': 'error',
                'message': 'Registration failed.',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework import status
# from django.contrib.auth.models import User
# from .serializers import UserRegistrationSerializer
# from drf_yasg.utils import swagger_auto_schema
#
# def login_page(request):
#     return render(request, "login.html")
#
# class HomeView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
#         return Response(content)
#
# class LogoutView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
# class RegisterView(APIView):
#      #@swagger_auto_schema(request_body=UserRegistrationSerializer)
#     def post(self, request):
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({
#                 'status': 'success',
#                 'message': 'User registered successfully.'
#             }, status=status.HTTP_201_CREATED)
#         else:
#             return Response({
#                 'status': 'error',
#                 'message': 'Registration failed.',
#                 'errors': serializer.errors
#             }, status=status.HTTP_400_BAD_REQUEST)




# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework import status
# from django.contrib.auth.models import User
# from django.shortcuts import render
# def login_page(request):
#     return render(request, "login.html")
# class HomeView(APIView):
#     permission_classes = (IsAuthenticated,)
#     def get(self, request):
#         content = {'message': 'Welcome to the JWTAuthentication page using React Js and Django!'}
#         return Response(content)
#
#
# class LogoutView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request):
#
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
# class RegisterView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         username = request.data.get('username', email)  # Użyj emaila jako nazwy użytkownika, jeśli nie podano innej
#
#         if not email or not password:
#             return Response({'status': 'error', 'message': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
#
#         if User.objects.filter(username=username).exists():
#             return Response({'status': 'error', 'message': 'Username is already taken.'}, status=status.HTTP_400_BAD_REQUEST)
#
#         if User.objects.filter(email=email).exists():
#             return Response({'status': 'error', 'message': 'Email is already registered.'}, status=status.HTTP_400_BAD_REQUEST)
#
#         user = User.objects.create_user(username=username, email=email, password=password)
#         return Response({'status': 'success', 'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)