from rest_framework import views
from rest_framework.response import Response
from django.http import Http404
from django.contrib.auth.models import User
from .serializers import CategorySerializer, ProductCommentSerializer, ProductImageSerializer, ProductSerializer
from .models import Category, Product, ProductComment, ProductImage
from rest_framework.parsers import JSONParser
from json import JSONDecodeError
from core.helpers import custom_response, parse_request

# Create your views here.
class CategoryAPIView(views.APIView):
    def get(self, request):
        try:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return custom_response('Get all category successfully!','Success', serializer.data, 200)
        except:
            return custom_response('Get all category failed!', 'Error', None ,400)
    def post(self, request):
        data = parse_request(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return custom_response('Create category successfully', 'Success', serializer.data, 200)
        else:
            return custom_response('Create category failed!', 'Error', serializer.errors, 400)

class CategoryDetailAPIView(views.APIView):
    def get_object(self, id_slug):
        try:
            return Category.objects.get(pk=id_slug)
        except:
            raise Http404
        
    def get(self, request, id_slug):
        try:
            category = self.get_object(id_slug)
            serializer = CategorySerializer(category)
            return custom_response('Get category successfully!', 'Success', serializer.data, 200)
        except:
            return custom_response('Get category failed!', 'Error', "Category not found!", 400)
        
    def put(self, request, id_slug):
        try:
            data = parse_request(request)
            category = self.get_object(id_slug)
            serializer = CategorySerializer(category, data=data)
            if serializer.is_valid():
                serializer.save()
                return custom_response('Update category successfully!', 'Success', serializer.data, 200)
            else:
                return custom_response('Update category failed!', 'Error', serializer.errors, 400)
        except:
            return custom_response('Update category failed!', 'Error', 'Category not found!', 400)
    
    def delete(self, request, id_slug):
        try:
            category = self.get_object(id_slug)
            category.delete()
            return custom_response('Delete category successfully!', 'Success', {'category_id':id_slug}, 204)
        except:
            return custom_response('Delete category failed!', 'Error', 'Category not found!', 400)
        
class ProductAPIView(views.APIView):
    
    def get(self, request):
        try:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return custom_response('Get products successfully!', 'Success', serializer.data, 200)
        except:
            return custom_response('Get products failed!', 'Success', None, 400)
        
    def post(self, request):
        data = parse_request(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return custom_response('Create product successfully!', 'Success', serializer.data, 201)
        else:
            return custom_response('Create product failed!','Error',serializer.errors, 400)
        

        
            

        

