BASE_URL = "https://demoqa.com"
ENVIRONMENT = "QA"
AUTO_OPEN_REPORT = False
TIMEOUT = 10

REGISTER_URL = f"{BASE_URL}/Account/v1/User"
GENERATE_TOKEN_URL = f"{BASE_URL}/Account/v1/GenerateToken"
LOGIN_URL = f"{BASE_URL}/Account/v1/Authorized"
ACCOUNT_DETAIL_URL = f"{BASE_URL}/Account/v1/User"

BOOKS_URL = f"{BASE_URL}/BookStore/v1/Books"
BOOK_DETAIL_URL = f"{BASE_URL}/BookStore/v1/Book"