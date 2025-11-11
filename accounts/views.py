from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import RegisterSerializer,LoginUserSerializer

class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "ثبت‌نام با موفقیت انجام شد!"}, status=201)
        return Response(serializer.errors, status=400)

class LoginUserView(APIView):
    def post(self,request):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"result": "you are logged in"}, status=200)
        return Response(serializer.errors, status=400)