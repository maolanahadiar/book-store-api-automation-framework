def adding_new_book_payload(user_id, isbn):
    return {
        "userId": user_id,
        "collectionOfIsbns": [
            {
                "isbn": isbn,
            }
        ],
    }

def isbn_book_payload(user_id, isbn):
    return {
        "userId": user_id,
        "isbn": isbn,
    }