class User:

    def __init__(self, name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password


class UserDataIncorrect:

    INVALID_EMAIL_DATA = ['abc@', 'abc@com', '@com.ua', 'emailcom.ua', '#$%^&*@com.ua']
    UNREGISTERED_EMAIL = 'abc@test.com'
    RANDOM_PASSWORD = 'Aa12345678'
    INCORRECT_PASSWORD_DATA = []
    INCORRECT_NAME_DATA = ['Василий', '@#$%', '12345', 'John James']




# TODO: Make user`s data generation from file .json
