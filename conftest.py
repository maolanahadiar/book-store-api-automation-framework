import pytest
from services.bookstore_service import BookStoreService
from utils.allure_helper import AllureHelper
from config.settings import AUTO_OPEN_REPORT

@pytest.fixture(scope="session")
def book_service():
    return BookStoreService()

RESULTS_DIR = "reports/allure-results"
REPORT_DIR = "reports/allure-report"

def pytest_sessionstart(session):
    AllureHelper.create_environment(RESULTS_DIR)
    AllureHelper.create_executor(RESULTS_DIR)
    
def pytest_sessionfinish(session, exitstatus):
    AllureHelper.copy_history(
        RESULTS_DIR,
        REPORT_DIR
    )

    if AUTO_OPEN_REPORT:
        AllureHelper.generate_report(
            RESULTS_DIR,
            REPORT_DIR
        )

        AllureHelper.open_report(REPORT_DIR)