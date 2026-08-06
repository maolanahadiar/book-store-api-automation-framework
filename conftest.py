import pytest
from http import HTTPStatus
from services.bookstore_service import BookStoreService
from services.account_service import AccountService
from utils.allure_helper import AllureHelper
from config.settings import AUTO_OPEN_REPORT

RESULTS_DIR = "reports/allure-results"
REPORT_DIR = "reports/allure-report"

def pytest_sessionstart(session):
    """Prepare Allure metadata before test execution"""
    
    AllureHelper.create_environment(RESULTS_DIR)
    AllureHelper.create_executor(RESULTS_DIR)
    
def pytest_sessionfinish(session, exitstatus):
    """Generate and open Allure report based on config after test execution"""
    
    AllureHelper.copy_history(
        RESULTS_DIR,
        REPORT_DIR
    )

    if AUTO_OPEN_REPORT == True:
        AllureHelper.generate_report(
            RESULTS_DIR,
            REPORT_DIR
        )

        AllureHelper.open_report(REPORT_DIR)
        
@pytest.fixture(scope="session")
def book_service():
    return BookStoreService()

@pytest.fixture(scope="session")
def account_service():
    return AccountService()

@pytest.fixture(scope="session")
def auth_token(account_service, created_user):

    response = account_service.generate_token(
        username=created_user["username"],
        password=created_user["password"],
    )

    assert response.status_code == HTTPStatus.OK

    return response.json()["token"]