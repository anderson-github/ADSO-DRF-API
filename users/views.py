from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers import InputSerializer, OutputSerializer
from users.serializers import LogInInputSerializer, LogInOutputSerializer, ProfileOutputSerializer

from users.models import CustomUser


class SignUp(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        """ """

        # Validating input data
        serializer = InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Create user
        if CustomUser.objects.filter(email=serializer.validated_data['email']).exists():
            return Response("Email already registered", status=status.HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(username=serializer.validated_data['username']).exists():
            return Response("Username already registered", status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.create_user(**serializer.validated_data)

        # Log in (Getting an access token)
        refresh = RefreshToken.for_user(user)

        # Returning json response
        serializer = OutputSerializer({
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "birth_date": user.birth_date,
            "biography": user.biography,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        })
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class Login(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        # Validating input data
        serializer = LogInInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = CustomUser.objects.get(username=serializer.validated_data['username'])
        except CustomUser.DoesNotExist:
            return Response("Username or password is incorrect", status=status.HTTP_400_BAD_REQUEST)

        is_password_correct = user.check_password(serializer.validated_data['password'])
        if is_password_correct is False:
            return Response("Username or password is incorrect", status=status.HTTP_400_BAD_REQUEST)

        # Log in (Getting an access token)
        refresh = RefreshToken.for_user(user)

        # Returning json response
        serializer = LogInOutputSerializer({
            "username": user.username,
            "email": user.email,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        })
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class Profile(APIView):

    def get(self, request):
        """ """
        # Returning json response
        serializer = ProfileOutputSerializer({
            "username": request.user.username,
            "email": request.user.email,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "birth_date": request.user.birth_date,
            "biography": request.user.biography,
        })
        return Response(data=serializer.data, status=status.HTTP_200_OK)



