from django.forms import model_to_dict
from django.shortcuts import render, redirect
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Women, Category
from .serializers import WomenSerializer, CategorySerializer


class WomenViewSet(viewsets.ModelViewSet):
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Women.objects.all()
        return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        category = Category.objects.get(pk=pk)
        category_sr = CategorySerializer(category)
        return Response({'category': category_sr.data})



# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"posts": serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': "Method put not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': "object does not exist"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'upd_post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method delete not allowed'})
#
#         try:
#             obj = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "object does not exist"})
#
#         serializer = WomenSerializer(obj)
#         obj.delete()
#
#         return Response({'deleted_post': serializer.data})



















# class CategoryAPIView(APIView):
#     def get(self, request):
#         categories = Category.objects.all()
#         return Response({'cats': CategorySerializer(categories, many=True).data})
#
#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'new_cat': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not alloved'})
#
#         try:
#             instance = Category.objects.get(pk=pk)
#         except:
#             return Response({"error": "object does not exist"})
#
#         serializer = CategorySerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'upd_cat': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             instance = Category.objects.get(pk=pk)
#         except:
#             return Response({'error': "object does not exist"})
#
#         serializer = CategorySerializer(instance)
#         instance.delete()
#
#         return Response({'deleted_cat': serializer.data})
#
#
# class CategoryDetailView(APIView):
#     def get(self, request, pk):
#         c = Category.objects.get(pk=pk)
#         return Response({"cats": CategorySerializer(c).data})



