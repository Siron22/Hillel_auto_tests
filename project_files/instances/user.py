class User:

    def __init__(self, name=None, lastname=None, email=None, password=None, user_id=None,
                 photo_filename="default-user.png", distance_units="km", currency="usd", country=None, date_birth=None):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.user_id = user_id
        self.photo_filename = photo_filename
        self.distance_units = distance_units
        self.currency = currency
        self.country = country
        self.date_birth = date_birth

    def get_user_id(self, response):
        """Get car id from response of request 'Sign in'
        """
        self.user_id = response.json()["data"]["userId"]
        return self.user_id

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
    TRIM_DATA = [' Alex', 'Alex ', ' Alex ']


registered_user_data = {
    "name": "Anne",
    "lastName": "Beatty",
    "email": "Etha_Lind@gmail.com",
    "password": "Sunday1XxXx",
    "repeatPassword": "Sunday1XxXx",
    "userId": 32358,
    "photoFilename": "default-user.png",
    "distanceUnits": "km",
    "currency": "usd"
}
