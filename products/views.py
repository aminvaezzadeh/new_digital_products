from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category,Product,File
from .serializers import CategorySerializer,FileSerializer,ProductSerializer
from  rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from subscriptions.models import Subscription
from django.utils import timezone
class ProductListView(APIView):
    def get(self,request):
        print(request.user)
        print(request.auth)

        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True , context={'request': request})
        return Response(serializer.data)

class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        print(request.user)
        print(request.auth)
        if not Subscription.objects.filter(
            user=request.user,
            expire_time__gt=timezone.now(),
        ).exists():
            return Response({'Detail':'you dont have a valid subscription'},status=status.HTTP_401_UNAUTHORIZED)
        try:
            product=Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=ProductSerializer(product,context={'request': request})
        return Response(serializer.data)

class CategoryListView(APIView):
    def get(self,request):
        categories=Category.objects.all()
        serializer=CategorySerializer(categories,many=True,context={'request':request})
        return Response (serializer.data)

class CategoryDetailView(APIView):
    def get(self,request,pk):
        try:
            category=Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=CategorySerializer(category,context={'request':request})
        return Response(serializer.data)

class FileListView(APIView):
    def get(self,request,product_pk):
        files=File.objects.filter(product_id=product_pk)
        serializer=FileSerializer(files,many=True,context={'request':request})
        return Response(serializer.data)

class FileDetailView(APIView):
    def get(self,request,product_pk,pk):
        try:
            f=File.objects.get(pk=pk,product_id=product_pk)

        except File.DoesNotExist:
            return Response (status=status.HTTP_404_NOT_FOUND)
        serializer=FileSerializer(f,context={'request':request})
        return Response(serializer.data)







