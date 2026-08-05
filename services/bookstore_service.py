from clients.api_client import ApiClient
from headers.headers import auth_header
from config.settings import BOOKS_URL, BOOK_DETAIL_URL
from payloads.bookstore_payload import (
    adding_new_book_payload,
    specific_book_payload,
)

class BookStoreService(ApiClient):

    def get_all_books(self):
        """Retrieve the list of all available books"""
        
        return self.get(
            url=BOOKS_URL,
        )

    def get_book_by_isbn(self, isbn):
        """Retrieve specific book by using ISBN"""
        
        return self.get(
            url=BOOK_DETAIL_URL,
            params={
                "ISBN": isbn,
            },
        )

    def add_book(self, user_id, isbn, token):
        """Add book to the user's collection"""
        
        return self.post(
            url=BOOKS_URL,
            json=adding_new_book_payload(user_id, isbn),
            headers=auth_header(token),
        )

    def update_book(self, old_isbn, user_id, new_isbn, token):
        """Replace an existing book in the user's collection"""
        
        return self.put(
            url=f"{BOOKS_URL}/{old_isbn}",
            json=specific_book_payload(user_id, new_isbn),
            headers=auth_header(token),
        )

    def delete_book(self, user_id, isbn, token):
        """Remove book from the user's collection"""
        
        return self.delete(
            url=BOOK_DETAIL_URL,
            json=specific_book_payload(user_id, isbn),
            headers=auth_header(token),
        )