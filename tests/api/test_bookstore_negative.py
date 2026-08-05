import allure
from http import HTTPStatus
from testdata.bookstore import BOOKS
from testdata.credentials import CREDENTIALS
from testdata.messages import ERROR
        
@allure.title("User cannot add book without authorization token")
def test_add_book_without_token(book_service):

    with allure.step("Send request to add book without token"):
        response = book_service.add_book(
            user_id=CREDENTIALS["user_id"],
            isbn=BOOKS["existing"]["isbn"],
            token=CREDENTIALS["empty_token"],
        )

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.UNAUTHORIZED
    
    with allure.step("Verify response body"):
        body = response.json()
        
        assert body["code"] == ERROR["unauthorized"]["expected_code"]
        assert body["message"] == ERROR["unauthorized"]["expected_error_message"]
        
@allure.title("User cannot retrieve specific book using invalid ISBN")
def test_get_book_invalid_isbn(book_service):

    with allure.step(f"Send request to retrieve book using invalid ISBN {BOOKS["invalid"]["isbn"]}"):
        response = book_service.get_book_by_isbn(BOOKS["invalid"]["isbn"])

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.BAD_REQUEST
        
    with allure.step("Verify response body"):
        body = response.json()
        
        assert body["code"] == ERROR["invalid_isbn"]["expected_code"]
        assert body["message"] == ERROR["invalid_isbn"]["expected_error_message"]
        
@allure.title("User cannot add duplicate book")
def test_add_duplicate_book(book_service):

    with allure.step("Add book as initial data"):
        first_response = book_service.add_book(
            user_id=CREDENTIALS["user_id"],
            isbn=BOOKS["existing"]["isbn"],
            token=CREDENTIALS["valid_token"],
        )

        assert first_response.status_code == HTTPStatus.CREATED

    try:
        with allure.step("Send request to add duplicate book"):
            second_response = book_service.add_book(
                user_id=CREDENTIALS["user_id"],
                isbn=BOOKS["existing"]["isbn"],
                token=CREDENTIALS["valid_token"],
            )

        with allure.step("Verify response status code"):
            assert second_response.status_code == HTTPStatus.BAD_REQUEST
            
        with allure.step("Verify response body"):
            body = second_response.json()

            assert body["code"] == ERROR["duplicate_book"]["expected_code"]
            assert body["message"] == ERROR["duplicate_book"]["expected_error_message"]

    finally:
        with allure.step("Remove created book"):
            book_service.delete_book(
                user_id=CREDENTIALS["user_id"],
                isbn=BOOKS["existing"]["isbn"],
                token=CREDENTIALS["valid_token"],
            )
        
@allure.title("User cannot update book using invalid ISBN")
def test_update_invalid_book(book_service):

    with allure.step(f"Send request to update book using invalid ISBN {BOOKS["invalid"]["isbn"]}"):
        response = book_service.update_book(
            old_isbn=BOOKS["existing"]["isbn"],
            user_id=CREDENTIALS["user_id"],
            new_isbn=BOOKS["invalid"]["isbn"],
            token=CREDENTIALS["valid_token"],
        )
            
    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.BAD_REQUEST
        
    with allure.step("Verify response body"):
        body = response.json()
        
        assert body["code"] == ERROR["invalid_isbn"]["expected_code"]
        assert body["message"] == ERROR["invalid_isbn"]["expected_error_message"]
        
@allure.title("User cannot delete book without authorization token")
def test_delete_book_without_token(book_service):

    with allure.step("Send request to delete book without token"):
        response = book_service.delete_book(
            user_id=CREDENTIALS["user_id"],
            isbn=BOOKS["new"]["isbn"],
            token=CREDENTIALS["invalid_token"],
        )

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.UNAUTHORIZED
    
    with allure.step("Verify response body"):
        body = response.json()
        
        assert body["code"] == ERROR["unauthorized"]["expected_code"]
        assert body["message"] == ERROR["unauthorized"]["expected_error_message"]