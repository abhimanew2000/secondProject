from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from accounts.serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserProfileSerializer,
    UserChangePasswordSerializer,
    SendPasswordResetEmailSerializer,
    UserPassworddResetSerializer
)
from rest_framework.decorators import api_view, permission_classes

from django.contrib.auth import authenticate
from accounts.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.views import LogoutView
from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticated
from django.contrib.auth import logout
from .serializers import GoogleLoginSerializer
from django.contrib.auth import authenticate, login
from accounts.models import User
from django.contrib.auth import get_user_model




def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    # renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response(
                {"token": token, "msg": "Registration successfull"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user_with_google(request):
    if "google_oauth" in request.data:
        google_data = request.data["google_oauth"]

        serializer = UserRegistrationSerializer(data={
            'email': google_data.get("email"),
            'name': google_data.get("name"),
            'tc': True,  # You may need to adjust this based on your user model
            'password': 'some_random_password',  # Provide a default value
            'password2': 'some_random_password',
            # Add other relevant fields from Google data
        })

        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response({"msg": "Registration successful"})
        else:
            print(serializer.errors)  # Print the serializer errors for debugging
            return Response(serializer.errors, status=400)

    return Response({"msg": "Invalid request data"}, status=400)










class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes=[AllowAny]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            if user:
                token = get_tokens_for_user(user)
                return Response(
                    {"token": token, "msg": "Login Success","user_name":user.name,"email": user.email,}, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        "errors": {
                            "non_field_errors": ["Email or password is not Correct"]
                        }
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )



# @api_view(['GET'])
# @permission_classes([AllowAny])
# def check_user_registration(request):
#     email = request.GET.get('email')

#     # Perform a check in your database to see if the user with this email is registered
#     is_registered = User.objects.filter(email=email).exists()

#     return Response({'is_registered': is_registered})






@api_view(['POST'])
@permission_classes([AllowAny])
def google_login(request):
    print('enterrrred')
    try:
        # Extract the Google data from the request
        google_data = request.data.get("google_oauth")
        print(google_data,"doodle")

        # Check if the user is already registered
        user = User.objects.filter(email=google_data.get("email")).first()
        print(user,"userrrrrrrr")

        if user:
            # User is already registered, perform login
            serializer = UserLoginSerializer(data={"email": google_data.get("email"), "password": "some_random_password"})
            serializer.is_valid(raise_exception=True)
            user = authenticate(email=google_data.get("email"), password="some_random_password")
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response(
                {"token": {"access": access_token}, "msg": "Login Success", "user_name": user.name, "email": user.email},
                status=status.HTTP_200_OK
            )
        else:
            # User is not registered, return an error
            return Response({"msg": "User not registered"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"msg": "Error during Google login", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # Assuming you are using Django's built-in logout method

        # Perform user logout
        logout(request)

        return Response({"msg": "Logout successful"}, status=status.HTTP_200_OK)



class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={"user": request.user}
        )
        if serializer.is_valid(raise_exception=True):
            return Response(
                {"msg": "password Changed Successfully"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [AllowAny]


    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(
                {"msg": "password reset link send.Please check your Email"},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class UserPasswordResetView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes = [AllowAny]

    def post(self,request,uid,token,format=None):
        serializer=UserPassworddResetSerializer(data=request.data,context={'uid':uid,'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response(
                {"msg": "password Reset Successfully"},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
