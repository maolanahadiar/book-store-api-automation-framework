import allure
from http import HTTPStatus
from testdata.sample_data import BookStoreData as Data

@allure.title("User can retrieve the book list")
def test_get_all_books_success(book_service):

    with allure.step("Send request to retrieve all books"):
        response = book_service.get_all_books()

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.OK

    with allure.step("Verify response body"):
        body = response.json()

        assert "books" in body
        assert isinstance(body["books"], list)
        assert len(body["books"]) > 0

@allure.title("User can retrieve specific book using valid ISBN")
def test_get_book_detail_success(book_service):

    with allure.step(f"Send request to retrive book with ISBN {Data.ISBN}"):
        response = book_service.get_book_by_isbn(Data.ISBN)

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.OK

    with allure.step("Verify response body"):
        book = response.json()

        assert book["isbn"] == Data.ISBN
        assert book["title"]
        assert book["pages"] > 0

@allure.title("User can add a book into collection")
def test_add_book_success(book_service):

    with allure.step("Send request to add a book into user's collection"):
        response = book_service.add_book(
            user_id=Data.USER_ID,
            isbn=Data.ISBN,
            token=Data.TOKEN,
        )

    with allure.step("Verify response status code"):
        assert response.status_code in (
            HTTPStatus.OK,
            HTTPStatus.CREATED,
        )

    with allure.step("Verify response body"):
        body = response.json()

        assert "books" in body
        assert len(body["books"]) > 0

@allure.title("User can update an existing book")
def test_update_book_success(book_service):

    with allure.step(f"Send request to update ISBN from {Data.ISBN} to {Data.NEW_ISBN}"):
        response = book_service.update_book(
            old_isbn=Data.ISBN,
            user_id=Data.USER_ID,
            new_isbn=Data.NEW_ISBN,
            token=Data.TOKEN,
        )

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.OK

    with allure.step("Verify response body"):
        body = response.json()

        assert "books" in body
        assert len(body["books"]) == 1
        assert body["books"][0]["isbn"] == Data.NEW_ISBN

@allure.title("User can delete a book from collection")
def test_delete_book_success(book_service):

    with allure.step(f"Send request to delete book with ISBN {Data.NEW_ISBN}"):
        response = book_service.delete_book(
            user_id=Data.USER_ID,
            isbn=Data.NEW_ISBN,
            token=Data.TOKEN,
        )

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.NO_CONTENT