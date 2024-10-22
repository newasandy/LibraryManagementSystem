from .models import BookTransaction, Books
from .recommendation_algo import users_interaction_matrix

# fetch Books transaction data from the database

def fetch_bookstransaction_data():
    transactions = BookTransaction.objects.all().values('user_id', 'book_id')
    return transactions