from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from api.models import Books , Users , Admins , BookTransaction

# serilizers for books
class BooksSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Books
        fields = '__all__'

# serilizers for users
class UserSerializers(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField()
    class Meta:
        model = Users
        fields = '__all__'
    
    def create(self, validated_data):
        # user = Users(
        #     first_name = validated_data['first_name'],
        #     last_name =validated_data['last_name'],
        #     email =validated_data['email'],
        #     phone =validated_data['phone']
        # )
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

# serilizers for admin
class AdminSerializer(serializers.HyperlinkedModelSerializer):
    admin_id = serializers.ReadOnlyField()
    class Meta:
        model = Admins
        fields = '__all__'

# serilizers for BookTransaction
class BookTransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookTransaction
        fields = '__all__'
