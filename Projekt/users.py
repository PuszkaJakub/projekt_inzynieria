import sys
from typing import List, Collection
import structures as s
import csv

def check_user_in_database(login, password, flag, type):
    if flag == "login":
        with open('./logins.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if any(row) and row['Login'] == login and row['Password'] == password and row['Permissions'] == type:
                    return True
            return False
    elif flag == "register":
        with open('./logins.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if any(row) and row['Login'] == login:
                    return True
            return False

def parse_value(value):
    if value.isdigit():
        return int(value)
    else:
        return value   
    
def date_select():
    ordered_date = ""
    while True:
        print("-------------------------")
        month_choice = input("Wybierz miesiac: ").strip()
        match month_choice:
            case '1' | '01' | 'styczen':
                ordered_date += '01.'
                max_days = 31
                break
            case '2' | '02' | 'luty':
                ordered_date += '02.'
                max_days = 28
                break
            case '3' | '03' | 'marzec':
                ordered_date += '03.'
                max_days = 31
                break
            case '4' | '04' | 'kwiecien':
                ordered_date += '04.'
                max_days = 30
                break
            case '5' | '05' | 'maj':
                ordered_date += '05.'
                max_days = 31
                break
            case '6' | '06' | 'czerwiec':
                ordered_date += '06.'
                max_days = 30
                break
            case '7' | '06' | 'lipiec':
                ordered_date += '07.'
                max_days = 31
                break
            case '8' | '08' | 'sierpien':
                ordered_date += '08.'
                max_days = 31
                break
            case '9' | '09' | 'wrzesien':
                ordered_date += '09.'
                max_days = 30
                break
            case '10' | '10' | 'pazdziernik':
                ordered_date += '10.'
                max_days = 31
                break
            case '11' | '11' | 'listopad':
                ordered_date += '11.'
                max_days = 30
                break
            case '12' | '12' | 'grudzien':
                ordered_date += '12.'
                max_days = 31
                break
            case _:
                print("Niepoprawne dane, sprobuj ponownie.")

    while True:
        print("-------------------------")
        day_choice = input("Wybierz dzien: ").strip()
        if day_choice.isdigit():
            day = int(day_choice)
            if 1 <= day <= max_days:
                ordered_date = str(day).zfill(2) + '.' + ordered_date
                break  
            else:
                print("Nieprawidlowe dane. Spróbuj ponownie.")
        else:
            print("Niepoprawne dane, sprobuj ponownie")
    return ordered_date + "2024"
        



class Calendar:
    def __init__(self):
        self.visits = []
        with open('./visits.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if any(row):
                    v_date, v_service_info, v_client_login, v_done, v_payed, v_contractor_login = map(parse_value, row)
                    self.visits.append(s.Visit(v_date, v_service_info, v_client_login, v_done, v_payed, v_contractor_login))

    def show_calendar(self):
        return self.visits

    def add_visit(self, visit: s.Visit):
        data = list(map(str,[visit.date, visit.service_info, visit.client_login, visit.status, visit.payed, visit.contractor_login]))
        print(data)
        with open('./visits.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

class Offer:
    def __init__(self):
        self.services = []
        with open('./services.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if any(row):
                    o_description, o_price, o_contractor_login = map(parse_value, row)
                    self.services.append(s.Service(o_description, o_price, o_contractor_login))

    def show_offer(self):
        return self.services

    def edit_offer(self,admin_login):
        while (True):
            edit_service_id = int(input("Podaj numer usługi do edycji: ").strip())
            print("Podaj nowe dane wybranej usługi")
            service_description = input("Opis usługi: ").strip()
            service_price = int(input("Cena usługi: ").strip())
            service = s.Service(service_description, service_price, admin_login)

            with open('./services.csv', 'r', newline='', encoding='utf-8') as csvfile:
                rows = list(csv.reader(csvfile))

            if 0 <= edit_service_id < len(rows):
                rows[edit_service_id-1] = [service.description, service.price, service.contractor_login]

                with open('./services.csv', 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(rows)
                    break
            else:
                print("-------------------------")
                print("Nieprawidłowy numer usługi.")

    def add_service(self, service: s.Service):
        with open('./services.csv',mode = 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([service.description,service.price,service.contractor_login])

    def delete_service(self):
        while True:
            delete_service_id = int(input("Podaj numer usługi usunięcia: ").strip())
            with open('./services.csv', 'r', newline='', encoding='utf-8') as csvfile:
                rows = list(csv.reader(csvfile))

            if 1 <= delete_service_id <= len(rows):
                del rows[delete_service_id - 1]

                with open('./services.csv', 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(rows)
                    break
            else:
                print("-------------------------")
                print("Nieprawidłowy numer usługi.")

class User:
    def register(self):
        pass

    def login(self):
        pass

    def check_offer(self) -> s.Visit:
        pass

    def check_callendar(self) -> str:
        pass

class Administrator(User):
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
                is_login_taken = check_user_in_database(login, password1, "register", "Admin")
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
            login_data_correct = check_user_in_database(login, password, "login", "Admin")
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
        # Dodaje do pliku services.csv usluge
        # new_service = s.Service
        service_description = input("Nazwa usługi: ").strip()
        service_price = int(input("Cena: ").strip())
        service_contractor = self.login
        service = s.Service(service_description, service_price, service_contractor)
        offer = Offer()
        offer.add_service(service)
        print("-------------------------")
        print("Pomyślnie dodano nową usługę")


    def edit_service(self):
        offer = Offer().show_offer()
        print("-------------------------")
        print("Lista dostępnych ofert: ")
        for i, service in enumerate(offer):
            print(f"[{i + 1}] {service.description} -- koszt {service.price}pln")
        offer = Offer()
        offer.edit_offer(self.login)
        print("-------------------------")
        print("Zaktualizowano listę usług")

    def delete_service(self):
        offer = Offer().show_offer()
        print("-------------------------")
        print("Lista dostępnych ofert: ")
        for i, service in enumerate(offer):
            print(f"[{i + 1}] {service.description} -- koszt {service.price}pln")
        offer = Offer()
        offer.delete_service()
        print("-------------------------")
        print("Pomyślnie usunięto serwis z oferty")

    def check_offer(self):
        offer = Offer().show_offer()

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
class Client(User):
    def __init__(self):
        self.login = ""
        self.password = ""
        self.permissions = "Client"
    

    def register(self):
        register_process = True
        while(register_process):
            login = input("Podaj login: ").strip()
            password1 = input("Podaj haslo: ").strip()
            password2 = input("Powtorz haslo: ").strip()
            if password1 == password2:
                is_login_taken = check_user_in_database(login, password1, "register","Client")
                if(not is_login_taken):
                    register_process = False
                else:
                    print("-------------------------")
                    print("Nazwa uzytkownika zajeta! Sprobuj ponownie")
                    print("-------------------------") 
            else:
                print("-------------------------")
                print("Hasla musza byc identyczne! Sprobuj ponownie")
                print("-------------------------")


        data = [{'Login':login, 'Password':password1, 'Permissions':'Client'}]

        with open('logins.csv', mode='a', newline='', encoding='utf-8') as file:
            fieldnames = ['Login', 'Password', 'Permissions']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerows(data)
        print("-------------------------")
        print("Zarejestrowano konto")
    

    def log_in(self):
        login_data_correct = False
        while not login_data_correct:
            login = input("Podaj login: ").strip()
            password = input("Podaj haslo: ").strip()
            login_data_correct = check_user_in_database(login, password, "login", "Client")
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
                        return
                    case _:
                        print("Nieprawidłowy wybór. Spróbuj ponownie.")
            else:
                self.login = login
                self.password = password
    
        print("Zalogowano pomyslnie")


    def reserve_visit(self):
        print("Wybierz oferte")
        ordered_service = self.check_offer(True)

        print("Wybierz termin")
        ordered_date = date_select()

        ordered_payed = self.pay()


        new_visit = s.Visit(ordered_date, ordered_service.description, self.login, "niedokonana", ordered_payed,  ordered_service.contractor_login)

        self.book_visit(new_visit)


    def cancel_visit(self):
        #TODO 

        # Zrobi Kuba

        # Clientowi wyswietlaja sie swoje uslugi, ktore maja status niewykonana

        # Client wybiera ktora usluge chce anulowac

        # Usluga jest usuwana

        pass


    def check_offer(self, flag) -> Offer:
        offer = Offer().show_offer()

        print("-------------------------")
        print("Lista dostepnych ofert")
        for i, service in enumerate(offer):
            print(f"[{i+1}] {service.description} -- koszt {service.price}pln")

        if(flag):
            while(True):
                user_choice = input("Wybor: ").strip()

                if user_choice.isdigit():
                    if 0 <= int(user_choice)-1 < len(offer):
                        return offer[int(user_choice)-1]
                    else:
                        print("Nieprawidlowy wybor, sprobuj ponownie")
                else:
                    print("Nieprawidlowy wybor, sprobuj ponownie")


    def check_calendar(self, status) -> str:
        dates = [date for date in Calendar().show_calendar() if date.client_login == self.login and date.status == status]
        print("-------------------------")
        print("Twoje uslugi")
        for i, visit in enumerate(dates):
            print(f"[{i+1}] {visit.service_info} data: {visit.date} status: {visit.status}")

    def pay(self) -> bool:
        return s.Payment().process_payment()



    def book_visit(self, visit: s.Visit):
        Calendar().add_visit(visit)
