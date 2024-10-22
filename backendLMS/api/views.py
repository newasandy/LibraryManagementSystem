from django.shortcuts import render
from django.http import JsonResponse
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
    transactions = fetch_bookstransaction_data()
    # print("hello sandy  ",transactions['book_id'])

    # print(transactions)

    demo_list_data = []



    for dataa in transactions:
        dict_data = {}
        dict_data['book_id'] = dataa['book_id']
        demo_list_data.append(dict_data)
        # print(f"sandy : user_id= {dataa['user_id']} and book_id= {dataa['book_id']} tashi")

    demo_dictt_data = {
        'demo_data' : demo_list_data
    }
    demo_json_data = json.dumps(demo_dictt_data)

    # print(demo_json_data)
    print(demo_list_data)
    for check_data in demo_list_data:
        # print(f"check data = {check_data['book_id']} tashi")
        
        print(check_data)

    # interaction_matrix, users, books = build_interaction_matrix(transactions)
    # similarity_matrix = calculate_similarity(interaction_matrix)
    # recommended_books = recommend_books_for_user(user_id, interaction_matrix, similarity_matrix, books)
    
    # book_titles = [book.title for book in recommended_books]
    # return JsonResponse(transactions)
    demoJson = [{'book_id':1},{'book_id':1},{'book_id':1},{'book_id':1},{'book_id':1}]
    return JsonResponse({
        # 'user_id': 5,
        # 'recommended_books':'hero mero vai',
        'demoJson': demo_list_data
    })
