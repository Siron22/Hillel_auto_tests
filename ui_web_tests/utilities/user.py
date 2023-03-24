class User:

    def __init__(self, name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password


class UserTestData:

    INVALID_EMAIL_DATA = ['abc@', 'abc@com', '@com.ua', 'emailcom.ua', '#$%^&*@com.ua']
    UNREGISTERED_EMAIL = 'abc@test.com'
    VALID_PASSWORD = 'Aa123456'
    OTHER_PASSWORD = 'Qq654321'
    INCORRECT_PASSWORD_DATA = ['Qq12345', 'Qq12345678901234', '12345678', 'AbCdEfGh', 'ABCDEFGH', 'abcdefgh',
                               'QQ123456', 'qq123456', 'Ыы123456', '1234QqЫы' 'Qq1234ыы', 'Qq123456Ыы']
    INCORRECT_NAME_DATA = ['Василий', '@#$%', '12345', 'John James', 'John123', '098James', '1', '@', 'ы',
                           'qwe123rtyuiopasdfghjklzx', 'qwer@#$tyuiopasdfghjklzx', 'qwertyuЭЭЭЭЭiopasdfghjklzx']
    INCORRECT_LENGTH_DATA = ['a', 'Q', 'qwertyuiopasdfghjklzx']




# TODO: Make user`s data generation from file .json
