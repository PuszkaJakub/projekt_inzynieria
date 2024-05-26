class Service:
    def __init__(self, description: str, price: int, contributor_id):
        self.description = description
        self.price = price
        self.contractor_id = contributor_id


class Car:
    def __init__(self, license_plate_number: str):
        self.license_plate_number = license_plate_number


class Payment:

    def process_payment(self) -> bool:
        # Implement payment processing logic
        pass


class Visit:
    def __init__(self, date: str, service_info: str, client_login: str, status: str, payed: bool, contractor_id: int):
        self.date = date
        self.service_info = service_info
        self.client_login = client_login
        self.status = status
        self.payed = payed
        self.contractor_id = contractor_id
