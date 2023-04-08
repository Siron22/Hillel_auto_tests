class Car:

    def __init__(self, car_brand_id: int, car_model_id: int, mileage: int, car_id=None):
        self.car_brand_id = car_brand_id
        self.car_model_id = car_model_id
        self.mileage = mileage
        self.car_id = car_id

    def get_car_id(self, response):
        """Get car id from response of request 'Creates new car'
        """
        self.car_id = response.json()["data"]["id"]
        return self.car_id
