from django.contrib import admin
from django.urls import path, include
from api.views import BooksViewSet, UsersViewSet, AdminsViewSet, BookTransactionViewSet , get_recommendations, UserSignupView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books',BooksViewSet)
router.register(r'users',UsersViewSet)
# router.register(r'signup',UserSignupView)
router.register(r'admins', AdminsViewSet)
router.register(r'booktransaction', BookTransactionViewSet)
# router.register(r'recommendations/<int:user_id>/', get_recommendations)

urlpatterns = [

    path('', include(router.urls)),
    path('recommendations/<int:user_id>/', get_recommendations, name='get_recommendations'),
    path('signup/',UserSignupView.as_view(), name='user_signup')
    # path('admin/', admin.site.urls),
]


# i am using django python in backend and sqlite as database and react as frontend, i need to implementa collaborative filtering algorithms as cosine similarity algorithms, and i have book transaction database which have user is book id and other details, now i need to request through api by pass user id from frontend and in the backend get that user id and find the books to recommend to the that user by using collaborative filtering and pass the recommendation books id by api response. i need proper code to solve this problems