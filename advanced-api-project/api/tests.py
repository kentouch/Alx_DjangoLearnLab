from typing import Any
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITest(APITestCase):
    
    def setUp(self):
        # let's first create a user and authenticate him
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        
        # create an author instance before running the book tests
        self.author = Author.objects.create(name="Clark Kent")
        # Set up initial data
        self.book1 = Book.objects.create(title="Book 1", author=self.author, publication_year=2020)
        self.book2 = Book.objects.create(title="Book 2", author=self.author, publication_year=2021)

    ###  Test to retrieve the list of books
    def test_get_books(self):
        
        # URL for the API endpoint
        url = reverse('book-list')  # Assuming the URL is named 'book-list'
        
        # Simulate a GET request
        response = self.client.get(url)
        
        # Check that the request succeeded
        self.assertEqual(response.status_code, 200)
        
        # Check the returned data
        self.assertEqual(len(response.data), 2)  # Expecting 2 books
        self.assertEqual(response.data[0]['author'], self.author.id)
        self.assertEqual(response.data[1]['author'], self.author.id)


    ###  Test to retrieve a single book
    def test_get_book(self):
     
        # URL for the API endpoint to retrieve a single book
        # args = [1] represents the ID of the book
        url = reverse('book-detail', kwargs={'pk': self.book1.id})
        
        # Simulate a GET request
        response = self.client.get(url)
        
        # Check that the request succeeded
        self.assertEqual(response.status_code, 200)
        
        # Check the returned data
        self.assertEqual(response.data['title'], "Book 1")
        self.assertEqual(response.data['author'], self.author.id)
        self.assertEqual(response.data['publication_year'], 2020)
    
    ### Test to create a new book
    def test_create_book(self):
       
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'author': self.author.id,
            'publication_year': 2022
        }
        
        # Simulate a POST request
        response = self.client.post(url, data, format='json')

    # Check that the request succeeded
        self.assertEqual(response.status_code, 201)
        # Check the returned data
        self.assertEqual(response.data['title'], "New Book")
        self.assertEqual(response.data['author'], self.author.id)
        self.assertEqual(response.data['publication_year'], 2022)
    
    ### Test to update an existing book
    def test_update_book(self):

        """ Test for updating an existing book """
        url = reverse('book-update', kwargs={'pk': self.book1.id})
        data = {
            'title': 'Updated Book 1',
            'author': self.author.id,
            'publication_year': 2021
        }
        
        # Simulate a PUT request
        response = self.client.put(url, data, format='json')
        
        # Check that the request succeeded
        self.assertEqual(response.status_code, 200)
        # Check the returned data
        self.assertEqual(response.data['title'], "Updated Book 1")
        self.assertEqual(response.data['author'], self.author.id)
        self.assertEqual(response.data['publication_year'], 2021)

    ### Test to delete an existing book
    def test_delete_book(self):
   
        # URL for the API endpoint to delete a book with Id = 1
        url = reverse('book-delete', kwargs={'pk': self.book2.pk})
        
        # Simulate a DELETE request
        response = self.client.delete(url)
        
        # Check that the request succeeded
        self.assertEqual(response.status_code, 204)

        # check that the book is deleted
        self.assertEqual(Book.objects.count(), 1)