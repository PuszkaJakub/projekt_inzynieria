import sys
import structures as s
import csv
import methods
import offer as ofr
import user

class Administrator(user.User):
    def __init__(self):
        self.login = ''
        self.password = ''
        self.permissions = 'Admin'
        self.visits = []

    def register(self):
        register_process = True
        while (register_process):
            login = input("Podaj login: ").strip()
            password1 = input("Podaj haslo: ").strip()
            password2 = input("Powtorz haslo: ").strip()
            if password1 == password2:
                is_login_taken = methods.check_user_in_database(login, password1, "register", "Admin")
                if (not is_login_taken):
                    register_process = False
                else:
                    print("-------------------------")
                    print("Nazwa uzytkownika zajeta! Sprobuj ponownie")
                    print("-------------------------")
            else:
                print("-------------------------")
                print("Hasla musza byc identyczne! Sprobuj ponownie")
                print("-------------------------")

        data = [{'Login': login, 'Password': password1, 'Permissions': 'Admin'}]

        with open('logins.csv', mode='a', newline='', encoding='utf-8') as file:
            fieldnames = ['Login', 'Password', 'Permissions']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerows(data)
        print("-------------------------")
        print("Zarejestrowano konto")

    def log_in(self):
        login_data_correct = False
        while (not login_data_correct):
            login = input("Podaj login: ").strip()
            password = input("Podaj haslo: ").strip()
            login_data_correct = methods.check_user_in_database(login, password, "login", "Admin")
            print("-------------------------")

            if not login_data_correct:
                print("Niepoprawny login lub haslo")
                print("[1] Sprobuj ponownie")
                print("[0] Wyjdz")
                try_again = int(input("Wybor: ").strip())

                match try_again:
                    case 1:
                        pass
                    case 0:
                        sys.exit()
                    case _:
                        print("Nieprawidłowy wybór. Spróbuj ponownie.")
            else:
                self.login = login
                self.password = password

        print("Zalogowano pomyslnie")


    def add_service(self):
        service_description = input("Nazwa usługi: ").strip()
        service_price = int(input("Cena: ").strip())
        service_contractor = self.login
        service = s.Service(service_description, service_price, service_contractor)
        offer = ofr.Offer()
        offer.add_service(service)
        print("-------------------------")
        print("Pomyślnie dodano nową usługę")


    def edit_service(self):
        self.check_offer()
        offer = ofr.Offer()
        offer.edit_offer(self.login)
        print("-------------------------")
        print("Zaktualizowano listę usług")

    def delete_service(self):
        self.check_offer()
        offer = ofr.Offer()
        offer.delete_service()
        print("-------------------------")
        print("Pomyślnie usunięto serwis z oferty")

    def check_offer(self):
        offer = ofr.Offer().show_offer()

        print("-------------------------")
        print("Lista dostepnych ofert")
        for i, service in enumerate(offer):
            print(f"[{i + 1}] {service.description} -- koszt {service.price}pln")

    def check_calendar(self):
        print("-------------------------")
        print("Lista niedokonanych wizyt:")

        with open('visits.csv', mode='r', newline='', encoding='utf-8') as file:
            counter = 0
            reader = csv.DictReader(file)
            for row in reader:
                if row['Stan'] == 'niedokonana' and row['Login pracownika'] == self.login:
                    counter+=1
                    print(f"Wizyta: {row['Data']} - Usługa: {row['Usluga']}, Klient: {row['Login klienta']}, Status: {row['Stan']}")
            if counter == 0:
                print("Brak wizyt w kalendarzu")