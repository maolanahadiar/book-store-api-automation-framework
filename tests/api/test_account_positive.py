import allure
from http import HTTPStatus
from utils.data_generator import register_data

data = register_data()

@allure.title("User can register successfully")
def test_register_success(account_service):
    
    with allure.step("Send request to register new account"):
        
        response = account_service.register(
            username=data["username"],
            password=data["password"]
        )
        
    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.CREATED
        
    with allure.step("Verify response body"):
        body = response.json()
        
        assert "userID" in body
        assert isinstance(body["userID"], str)
        assert body["username"] == data["username"]

@allure.title("User can generate token after registration")        
def test_generate_token_success(account_service):
    
    with allure.step("Send request to generate token"):
        response = account_service.generate_token(
            username=data["username"],
            password=data["password"]
        )
        
    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.OK
        
    with allure.step("Verify response body"):
        body = response.json()
        
        assert isinstance(body["token"], str)
        assert isinstance(body["expires"], str)
        assert body["status"] == "Success"
        assert body["result"] == "User authorized successfully."