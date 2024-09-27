from rest_framework import serializers
from .models import Book, Author


# serializers for the Book model in used for
# the creation and update of Book records in the database through the API
# this is used for the POST and PUT requests
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate_publication_year(self, value):
        if value < 2024:
            raise serializers.ValidationError('Publication year must be less than 2024')
        return value

# serializers for the Author model in used for
# the creation and update of Author records in the database through the API
# this is used for the POST and PUT requests

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

# Describe how the relationship 
# between Author and Book is handled in your serializers.
# the relationship between Author and Book is one-to-many relationship
# and it is handled in serializers as a list of dictionaries
# the list of dictionaries will be used in the POST and PUT requests