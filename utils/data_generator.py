from faker import Faker
import random

fake = Faker()

def register_data():
    return {
        "username": f"{fake.user_name()}{random.randint(100000, 999999)}",
        "password": fake.password(
            length=12,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ),
    }