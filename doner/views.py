from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DonerModel
from .serializer import DonerSerializer
from django.contrib.auth.models import User
from resiver.models import ResiverModel

class CreateDonationRequestView(APIView):
   
    def post(self, request):
        serializer = DonerSerializer(data=request.data)
        if serializer.is_valid():
            resiver_id = request.data.get('resiver')
            post_id = request.data.get('post')
            confirm = request.data.get('confirm', False)  

            try:
                resiver = User.objects.get(id=resiver_id)
                post = ResiverModel.objects.get(id=post_id)

                if confirm and post.user == request.user:
                    return Response(
                        {'error': 'The post creator cannot confirm their own request.'},
                        status=status.HTTP_403_FORBIDDEN
                    )

               
                donation = DonerModel.objects.create(
                    sender=request.user,
                    resiver=resiver,
                    post=post
                )
                donation.save()

                
                if confirm:
                    post.resivedBool = True
                    post.save()

                return Response(
                    {'message': 'Donation request created successfully', 'confirmed': confirm},
                    status=status.HTTP_201_CREATED
                )
            except User.DoesNotExist:
                return Response({'error': 'Resiver not found'}, status=status.HTTP_404_NOT_FOUND)
            except ResiverModel.DoesNotExist:
                return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def get(self, request):
        
        donations = DonerModel.objects.none()

        
        sender_username = request.query_params.get('sender', None)
        resiver_username = request.query_params.get('resiver', None)

      
        if sender_username:
            try:
                sender_user = User.objects.get(username=sender_username)
                donations = DonerModel.objects.filter(sender=sender_user)
            except User.DoesNotExist:
                return Response({'error': 'Sender not found'}, status=status.HTTP_404_NOT_FOUND)

        
        elif resiver_username:
            try:
                resiver_user = User.objects.get(username=resiver_username)
                donations = DonerModel.objects.filter(resiver=resiver_user)
            except User.DoesNotExist:
                return Response({'error': 'Resiver not found'}, status=status.HTTP_404_NOT_FOUND)

        
        else:
            donations = DonerModel.objects.filter(sender=request.user) | DonerModel.objects.filter(resiver=request.user)

        serializer = DonerSerializer(donations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
