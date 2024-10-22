from rest_framework import serializers
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
