from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from api.models import Books, Users , Admins, BookTransaction
from api.serializers import BooksSerializers, UserSerializers, AdminSerializer, BookTransactionSerializer
# from .recommendation_algo import users_interaction_matrix, calculate_similarity , recommend_books_for_user
from .utils import fetch_bookstransaction_data

# Create views for Books
class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers

# create views for users
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializers

# create views for admins
class AdminsViewSet(viewsets.ModelViewSet):
    queryset = Admins.objects.all()
    serializer_class = AdminSerializer

# create views for book transaction
class BookTransactionViewSet(viewsets.ModelViewSet):
    queryset = BookTransaction.objects.all()
    serializer_class = BookTransactionSerializer


####
from django.http import JsonResponse
from .utils import fetch_bookstransaction_data
import json
# from .models import Book

def get_recommendations(request, user_id):
    transactions = fetch_bookstransaction_data(user_id)

    demo_list_data = []

    for reco_book in transactions:
        book_dict = {}
        book_dict.update({'book_id':reco_book})
        demo_list_data.append(book_dict)

    return JsonResponse({
        'demoJson': demo_list_data
    })

class UserSignupView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User Registered Successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)