# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
# from .models import ReviewModel
# from .serializer import ReviewSerializer
# from rest_framework import generics, permissions
# from rest_framework.response import Response
# from rest_framework import status

# class ReviewViews(generics.ListCreateAPIView):
#     serializer_class = ReviewSerializer
#     # permission_classes = [permissions.IsAuthenticated]  # Ensure only logged-in users can post

#     def get_queryset(self):
#         """
#         Optionally filter reviews by username.
#         If no username is provided, return all reviews.
#         """
#         queryset = ReviewModel.objects.all()
#         username = self.request.query_params.get('username', None)
        
#         if username:
#             user = get_object_or_404(User, username=username)  # Ensure the user exists
#             queryset = queryset.filter(user=user)  # Filter reviews by the user
        
#         return queryset

#     def perform_create(self, serializer):
#         """Automatically assign the logged-in user when creating a review."""
#         serializer.save(user=self.request.user)


from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User  # Import the User model
from .models import ReviewModel
from .serializer import ReviewSerializer
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class ReviewViews(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    # permission_classes = [permissions.IsAuthenticated]  # Ensure only logged-in users can post

    def get_queryset(self):
        """
        Optionally filter reviews by username.
        If no username is provided, return all reviews.
        """
        queryset = ReviewModel.objects.all()
        username = self.request.query_params.get('username', None)
        
        if username:
            user = get_object_or_404(User, username=username)  # Ensure the user exists
            queryset = queryset.filter(user=user)  # Filter reviews by the user
        
        return queryset

    def perform_create(self, serializer):
        """Automatically assign the logged-in user when creating a review."""
        serializer.save(user=self.request.user)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET, PUT, PATCH, DELETE for individual reviews.
    """
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]  # Ensure only authenticated users can update/delete

    def get_object(self):
        """Retrieve the review and ensure the user has permission."""
        review = get_object_or_404(ReviewModel, pk=self.kwargs['id'])
        
        # Optional: If you want only the owner to be able to update/delete their own review
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            if review.user != self.request.user:
                raise PermissionDenied("You do not have permission to modify this review.")
        
        return review
