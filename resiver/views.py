from django.shortcuts import render
from .models import ResiverModel
from .serializer import ResiverSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404 

class ResiverView(APIView):
    def get(self, request, format=None):
        user_id = request.query_params.get('user')
        location = request.query_params.get('location')
        username = request.query_params.get('username')

        # Start with filtering out entries where resivedBool is True
        base_query = ResiverModel.objects.filter(resivedBool=False)

        if user_id:
            data = base_query.filter(user=user_id)
            serializer = ResiverSerializer(data, many=True)
            return Response(serializer.data)

        if location:
            data = base_query.filter(location=location)
            serializer = ResiverSerializer(data, many=True)
            return Response(serializer.data)

        if username:
            data = ResiverModel.objects.filter(user__username=username)
            serializer = ResiverSerializer(data, many=True)
            return Response(serializer.data)

        # Get all records where resivedBool is False if no other filter is applied
        data = base_query.all()
        serializer = ResiverSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print('post request')
        serializer = ResiverSerializer(data=request.data)
        serializer.user = request.user
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            print('user', serializer.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResiverDataDetails(APIView):
    def get_object(self, pk):
        try:
            return ResiverModel.objects.get(pk=pk)
        except ResiverModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = ResiverSerializer(data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = ResiverSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_200_OK)
