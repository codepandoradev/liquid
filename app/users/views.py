from random import randint

from django.db import IntegrityError
from django.forms import model_to_dict
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import EmailVerificationCode, Token, User
from .serializers import (
    CodeSerializer,
    LoginSerializer,
    TokenSerializer,
    UserSerializer,
    UserUpdateSerializer,
)
from .utils import email_to_nick, encode_password, generate_token


class UserApiView(APIView):
    @extend_schema(request=UserSerializer, responses={204: None}, methods=['POST'])
    @extend_schema(description="Override a specific method", methods=['POST'])
    def post(self, request):
        try:
            new_user = User.objects.create(
                login=request.data['login'],
                password=encode_password(request.data['password']),
                user_email=request.data['user_email'],
                phone_number='-' + str(randint(11111111111, 99999999999)),
                client_name=request.data['client_name'],
                nickname=email_to_nick(request.data['user_email']),
            )
        except IntegrityError:
            return Response({'details': "Пользователь с такими данными уже существует"})

        new_verificaton_code = EmailVerificationCode.objects.create(
            email=new_user.user_email,
            code=randint(10000, 99999),
            token=generate_token(),
        )
        return Response(
            {
                'user': model_to_dict(new_user),
                'DEBUG': model_to_dict(new_verificaton_code),
            }
        )

    def get(self, request):
        try:
            current_token = Token.objects.get(token=request.META['HTTP_TOKEN'])
        except Token.DoesNotExist:
            return Response({'details': "Token does not registred"})
        except KeyError:
            return Response({'details': "Not authorized"})

        try:
            current_user = User.objects.get(id=current_token.user_id)
        except User.DoesNotExist:
            return Response({'details': "User does not exists"})

        # if correct
        return Response(
            {
                'user': {
                    'email': current_user.user_email,
                    'nickname': current_user.nickname,
                    'profile_description': current_user.profile_description,
                    'client_name': current_user.client_name,
                    'user_avatar': current_user.user_avatar,
                    'clan_id': current_user.clan_id,
                }
            }
        )

    @extend_schema(
        request=UserUpdateSerializer, responses={204: None}, methods=['PATCH']
    )
    @extend_schema(description="Override a specific method", methods=['PATCH'])
    def patch(self, request):
        try:
            current_token = Token.objects.get(token=request.META['HTTP_TOKEN'])
        except Token.DoesNotExist:
            return Response({'details': "Token does not registred"})
        current_user = User.objects.get(id=current_token.user_id)
        current_user.nickname = request.data['nickname']
        current_user.profile_description = request.data['profile_description']
        current_user.user_avatar = request.data['user_avatar']
        current_user.save()

    def delete(self, request):
        try:
            current_token = Token.objects.get(token=request.META['HTTP_TOKEN'])
        except Token.DoesNotExist:
            return Response({'details': "Token does not registred"})
        current_user = User.objects.get(id=current_token.user_id)

        current_user.delete()
        return Response({'details': "User deleted"})

    class VerifyEmailToken(APIView):
        @extend_schema(request=CodeSerializer, responses={204: None}, methods=['POST'])
        def post(self, request):
            try:
                current_code = EmailVerificationCode.objects.get(
                    code=request.data['code']
                )
                if current_code.used:
                    return Response({'details': "Current code already used"})
            except EmailVerificationCode.DoesNotExist:
                return Response({'details': "code does not exist"})
            current_user = User.objects.get(user_email=current_code.email)
            current_user.email_verified = True
            current_user.save()

            current_code.used = True
            current_code.save()
            return Response({'details': current_user.user_email + ' verified'})

    class LoginEmail(APIView):
        @extend_schema(request=LoginSerializer, responses={204: None}, methods=['POST'])
        @extend_schema(description="Override a specific method", methods=['POST'])
        def post(self, request):

            try:
                current_user = User.objects.get(login=request.data['login'])
            except User.DoesNotExist:
                return Response({'details': "Incorrect login or password"})

            if current_user.password == encode_password(request.data['password']):
                if not current_user.email_verified:
                    return Response({'details': "Email not verified"})
                new_token = Token.objects.create(
                    user_id=current_user.id, token=generate_token()
                )
                return Response({'token': new_token.token})
            else:
                return Response({'details': "Incorrect login or password"})


@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        request.data['password'] = encode_password(request.data['password'])
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            token = generate_token()
            user = serializer.save()
            token_serializer = TokenSerializer(data={'user': user, 'token': token})
            token_serializer.is_valid()
            token_serializer.save()
            return Response(
                {'status': "user created", 'data': {'token': token}},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
