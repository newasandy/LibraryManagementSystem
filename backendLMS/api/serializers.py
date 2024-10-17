from rest_framework import serializers
from api.models import Books
class BooksSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Books
        fields = '__all__'