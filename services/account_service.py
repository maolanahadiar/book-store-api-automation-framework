from clients.api_client import ApiClient
from config.settings import REGISTER_URL, LOGIN_URL, ACCOUNT_DETAIL_URL, GENERATE_TOKEN_URL

class AccountService(ApiClient):
    
    def register(self, username, password):
        
        payload = {
            "userName": username,
            "password": password
        }
        
        return self.post(
            url=REGISTER_URL,
            json=payload
        )
    
    def generate_token(self, username, password):
        
        payload = {
            "userName": username,
            "password": password
        }
        
        return self.post(
            url=GENERATE_TOKEN_URL,
            json=payload
        )
        
    def login(self, username, password):
        
        payload = {
            "userName": username,
            "password": password
        }
        
        return self.post(
            url=LOGIN_URL,
            json=payload
        )
        
    def account_detail(self, user_id, token):
        
        headers = {
            "Authorization": f"Bearer {token}"
        }
        
        return self.get(
            url=f"{ACCOUNT_DETAIL_URL}/{user_id}",
            headers=headers
        )