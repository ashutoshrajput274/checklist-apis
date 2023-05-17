#from django.http import HttpResponse

from django.shortcuts import render
from django.http import Http404 # error show karane ke liye
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CheckListSerializer,CheckListItemSerializer
from .models import CheckList,CheckListItem

# Create your views here.
# data ko get karne ke liye or post (create karne ke liye ) karne ke liye api

class CheckListApi(APIView):
    serializer_class = CheckListSerializer
    
    def get(self,request, format=None):
        try:
            data = CheckList.objects.all()
            serializer = self.serializer_class(data, many=True)
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request, format=None):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CheckListApiGet(APIView):
    serializer_class = CheckListSerializer
    # exception handling
    def get_object(self, pk):
        try:
            return CheckList.objects.get(pk=pk)
        except CheckList.DoesNotExist:
            raise Http404
        
    # single object ko retrieve karne ke liye api 
    def get(self, request, pk, format=None):
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)
    
    # edit karne ke liye 
    def put(self, request, pk, format = None):
        CheckList =self.get_object(pk)
        serializer =self.serializer_class(CheckList, data = request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # delete karne ke liye 
    def delete(self, request, pk, format = None):
        CheckList = self.get_object(pk)
        CheckList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
     # checklist item create karne ke liye api
class CheckListItemCreateAPIView(APIView):
    serializer_class = CheckListItemSerializer
    
    def post(self, request , format=None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data =serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckListItems(APIView):
    serializer_class = CheckListItemSerializer
    
    def get_object(self, pk):
        try:
            return CheckListItem.objects.get(pk=pk)
        except CheckListItem.DoesNotExist:
            raise Http404
        
    
    def get(self, request, pk, format=None):
        CheckList_item = self.get_object(pk)
        serializer = self.serializer_class(CheckList_item)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)
    
     
    def put(self, request, pk, format = None):
        CheckList_item =self.get_object(pk)
        serializer =self.serializer_class(CheckList_item, data = request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk, format = None):
        CheckList_item = self.get_object(pk)
        CheckList_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    