from faker import Faker


fake = Faker()

def login_generator():
    generated_login = fake.user_name()
    return generated_login

def password_generator():
    generated_password = fake.random_number(8)
    return str(generated_password)

def name_generator():
    generated_name = fake.first_name()
    return generated_name
