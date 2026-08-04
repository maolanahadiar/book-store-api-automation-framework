import pytest
import os
import subprocess
from services.bookstore_service import BookStoreService
from utils.allure_helper import AllureHelper

ALLURE_RESULTS_DIR = "reports/allure-results"
ALLURE_REPORT_DIR = "reports/allure-report"

def pytest_sessionstart(session):
    AllureHelper.create_environment(ALLURE_RESULTS_DIR)
    AllureHelper.create_executor(ALLURE_RESULTS_DIR)
    AllureHelper.copy_history(
        ALLURE_RESULTS_DIR,
        ALLURE_REPORT_DIR,
    )
    
def pytest_sessionfinish(session, exitstatus):
    subprocess.run([
        "allure",
        "generate",
        "reports/allure-results",
        "-o",
        "reports/allure-report",
        "--clean",
    ], check=True)

    if os.getenv("CI", "").lower() != "true":
        subprocess.Popen([
            "allure",
            "open",
            "reports/allure-report",
        ])    

@pytest.fixture(scope="session")
def book_service():
    return BookStoreService()