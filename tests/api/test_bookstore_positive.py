import allure
from http import HTTPStatus
from testdata.bookstore import BOOKS
from testdata.credentials import CREDENTIALS
from utils.assertions import assert_book_schema

@allure.title("User can add a book into collection")
def test_add_book_success(book_service):

    with allure.step("Send request to add a book into user's collection"):
        response = book_service.add_book(
            user_id=CREDENTIALS["user_id"],
            isbn=BOOKS["existing"]["isbn"],
            token=CREDENTIALS["valid_token"],
        )

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.CREATED

    with allure.step("Verify response body"):
        body = response.json()

        assert "books" in body
        assert len(body["books"]) > 0
        assert body["books"][0]["isbn"] == BOOKS["existing"]["isbn"]

    with allure.step("Verify data type"):
        assert isinstance(body["books"], list)
        assert isinstance(body["books"][0]["isbn"], str)
        
@allure.title("User can retrieve the book list")
def test_get_all_books_success(book_service):

    with allure.step("Send request to retrieve all books"):
        response = book_service.get_all_books()

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.OK

    with allure.step("Verify response body"):
        body = response.json()

        assert "books" in body
        assert len(body["books"]) > 0
        
        for book in body["books"]:
            assert_book_schema(book)
    
    with allure.step("Verify data type"):
        assert isinstance(body["books"], list)
        assert isinstance(body["books"][0]["title"], str)
        assert isinstance(body["books"][0]["pages"], int)
        
@allure.title("User can retrieve specific book using valid ISBN")
def test_get_book_detail_success(book_service):

    with allure.step(f"Send request to retrive book with ISBN {BOOKS["existing"]["isbn"]}"):
        response = book_service.get_book_by_isbn(BOOKS["existing"]["isbn"])

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.OK

    with allure.step("Verify response body"):
        body = response.json()

        assert body["isbn"] == BOOKS["existing"]["isbn"]
        assert body["title"] == BOOKS["existing"]["title"]
        assert body["author"] == BOOKS["existing"]["author"]
        assert body["pages"] > 0
        
    with allure.step("Verify data type"):
        assert isinstance(body, dict)
        assert isinstance(body["title"], str)
        assert isinstance(body["pages"], int)
        
@allure.title("User can update an existing book")
def test_update_book_success(book_service):

    with allure.step(f"Send request to update ISBN from {BOOKS["existing"]["isbn"]} to {BOOKS["new"]["isbn"]}"):
        response = book_service.update_book(
            old_isbn=BOOKS["existing"]["isbn"],
            user_id=CREDENTIALS["user_id"],
            new_isbn=BOOKS["new"]["isbn"],
            token=CREDENTIALS["valid_token"],
        )

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.OK

    with allure.step("Verify response body"):
        body = response.json()

        assert "books" in body
        assert len(body["books"]) == 1
        assert body["books"][0]["isbn"] == BOOKS["new"]["isbn"]
        assert body["books"][0]["title"] == BOOKS["new"]["title"]
        assert body["books"][0]["author"] == BOOKS["new"]["author"]
        
    with allure.step("Verify data type"):
        assert isinstance(body["books"], list)
        assert isinstance(body["books"][0]["title"], str)
        assert isinstance(body["books"][0]["pages"], int)

@allure.title("User can delete a book from collection")
def test_delete_book_success(book_service):

    with allure.step(f"Send request to delete book with ISBN {BOOKS["new"]["isbn"]}"):
        response = book_service.delete_book(
            user_id=CREDENTIALS["user_id"],
            isbn=BOOKS["new"]["isbn"],
            token=CREDENTIALS["valid_token"],
        )

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.NO_CONTENT