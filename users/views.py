from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed

# Create your views here.

User = get_user_model()

class RegisterView(APIView):
    def post(self,request):
        serializers = UserSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    
class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        
        user = User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed('User not found')
    
        if not user.check_password(password):
            raise AuthenticationFailed('Password incorrect')
        
        return Response({'message':'success'})