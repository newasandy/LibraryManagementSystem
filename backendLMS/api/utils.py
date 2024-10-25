from .models import BookTransaction, Books
import numpy as np
from .recommendation_algo import cosine_similarity

# fetch Books transaction data from the database

def fetch_bookstransaction_data(user_id):
    book_transactions = BookTransaction.objects.all().values('user_id', 'book_id')

    # filter unique user from the book transaction database table
    unique_user_book_transaction = {}

    for unique_user in book_transactions:
        if unique_user['user_id'] != user_id:
            unique_user_book_transaction.update({
                unique_user['user_id']: unique_user['user_id']
            })
    
    unique_user_list = list(unique_user_book_transaction.values())

  
    # filter unique book id from the book transaction
    zero_vector = {}
    for unique_book in book_transactions:
        zero_vector.update({unique_book['book_id'] : 0})


    # creating vector for the login user

    vector_1_dict = {}
    vector_1_dict.update(zero_vector)
    user1_book = set()
    for user_vector1 in book_transactions:
        if user_vector1['user_id'] == user_id:
            user1_book.add(user_vector1['book_id'])
            if vector_1_dict[user_vector1['book_id']] == 0:
                vector_1_dict.update({user_vector1['book_id']:1})
        
    vector_1 = np.array(list(vector_1_dict.values()))

    reco_book = set()
    # creating vector 2
    for each_user in unique_user_list:
        vector_2_dict = {}
        vector_2_dict.update(zero_vector)
        other_user_book = set()
        for user_vector2 in book_transactions:
            # vector_2_dict.update({user_vector2['book_id']:0})
            if user_vector2['user_id'] == each_user:
                other_user_book.add(user_vector2['book_id'])
                if vector_2_dict[user_vector2['book_id']] == 0:
                    vector_2_dict.update({user_vector2['book_id']:1})
        vector_2 = np.array(list(vector_2_dict.values()))
        similarity_value = cosine_similarity(vector_1, vector_2)
        if similarity_value > 0 and similarity_value <= 1:
            print(f"similarity value with {each_user} is : {similarity_value}")
            other_user_book = other_user_book.difference(user1_book)
            reco_book = reco_book.union(other_user_book)
    
    reco_book_list = list(reco_book)








    return reco_book_list