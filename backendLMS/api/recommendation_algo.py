import numpy as np
import random
from sklearn.metrics.pairwise import cosine_similarity
# from django.contrib.auth.models import User
from .models import Books, Users

# build user book intraction matrix

def users_interaction_matrix(transactions):
    users = list(Users.objects.all())  # Get all users
    books = list(Books.objects.all())  # Get all books
    
    user_count = len(users)
    book_count = len(books)
    
    interaction_matrix = np.zeros((user_count, book_count))

    # Fill the matrix with transaction history
    for transaction in transactions:
        user_idx = users.index(Users.objects.get(id=transaction['user_id']))
        book_idx = books.index(Books.objects.get(id=transaction['book_id']))
        interaction_matrix[user_idx][book_idx] = 1  # Assuming 1 for each transaction
    
    return interaction_matrix, users, books

# Calculate cosine similarity between users
def calculate_similarity(interaction_matrix):
    return cosine_similarity(interaction_matrix)


# Recommend random 5 books based on cosine similarity
def recommend_books_for_user(user_id, interaction_matrix, similarity_matrix, books):
    user_idx = Users.objects.get(id=user_id).pk - 1  # Get index of the user
    similar_users = np.argsort(-similarity_matrix[user_idx])  # Sort users by similarity
    
    recommended_books = set()
    
    # Get books from top similar users
    for similar_user_idx in similar_users[1:5]:  # Get top 5 similar users
        user_books = np.where(interaction_matrix[similar_user_idx] > 0)[0]  # Books read by similar user
        recommended_books.update([books[idx].id for idx in user_books])  # Use book.id
    
    # Return 5 random book IDs from the set of recommended books
    return random.sample(recommended_books, min(len(recommended_books), 5))