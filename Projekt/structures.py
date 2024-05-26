class Service:
    def __init__(self, description: str, price: int, contributor_login):
        self.description = description
        self.price = price
        self.contractor_login = contributor_login


class Payment:

    def process_payment(self) -> bool:
        print("Wybierz metodę płatnośći:")
        print("[1] Online")
        print("[2] Na miejscu")
        mode = input("Wybór: ").strip()
        match mode:
            case "1":
                return True
            case "2":
                return False



class Visit:
    def __init__(self, date: str, service_info: str, client_login: str, status: str, payed: bool, contractor_login: str):
        self.date = date
        self.service_info = service_info
        self.client_login = client_login
        self.status = status
        self.payed = payed
        self.contractor_login = contractor_login
