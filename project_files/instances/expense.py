

class Expense:
    def __init__(self, car_id=None, reported_at=None, mileage=None, liters=None, total_cost=None, exp_id=None):
        self.car_id = car_id
        self.reported_at = reported_at
        self.mileage = mileage
        self.liters = liters
        self.total_cost = total_cost
        self.exp_id = exp_id

    def get_expense_id(self, response):
        """Get expense id from response of request 'Creates new expense'
        """
        self.exp_id = response.json()["data"]["id"]
        return self.exp_id
