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
                    v_date, v_service_info, v_client_login, v_done, v_payed, v_contractor_id = map(parse_value, row)
                    self.visits.append(s.Visit(v_date, v_service_info, v_client_login, v_done, v_payed, v_contractor_id))   

    def show_calendar(self):
        return self.visits

    def add_visit(self, visit: s.Visit):
        data = list(map(str,[visit.date, visit.service_info, visit.client_login, visit.status, visit.payed, visit.contractor_id]))
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
                    o_description, o_price, o_contractor_id = map(parse_value, row)
                    self.services.append(s.Service(o_description, o_price, o_contractor_id))

    def show_offer(self):
        return self.services
    
    def change_offer(self, id):
        #TODO
        pass

class User:
    def register(self):
        pass

    def login(self):
        pass

    def check_offer() -> s.Visit:
        pass

    def check_callendar() -> str:
        pass

class Administrator(User):
    def __init__(self, login: str, password: str, permissions: str, id: int, visits: Collection[s.Visit]):
        super().__init__(login, password, permissions)
        self.id = id
        self.visits = visits

    def register(self):
        pass

    def log_in(self):
        pass


    def add_service(self, service: s.Service):
        # Dodaje do pliku services.csv usluge
        # new_service = s.Service
        pass

    def edit_service(self):
        Offer().change_offer()
        pass

    def delete_service(self, service: s.Service):
        # Implement deleting service logic
        pass

    def show_offer(self) -> Offer:
        # Implement showing offer logic
        pass

    def check_calendar(self) -> str:
        # Implement checking calendar logic
        pass

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
                is_login_taken = check_user_in_database(login, password1, "register")
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
        while(not login_data_correct):
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
                        #TODO obsluzyc bo jest luka
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

        # TODO
        # Client dokonuje platnosci
        # ordered_payed = self.pay()
        ordered_payed = True


        new_visit = s.Visit(ordered_date, ordered_service.description, self.login, "niedokonana", ordered_payed,  ordered_service.contractor_id)

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
        #TODO
    
        # To wszystko nizej bedzie w Payment klasie w pliku structures

        # To wszystko w while(True)
        # Wybierz sposob platnosci: karta/gotowka
        # Jesli gotowka - return false
        # JEsli karta - 
        # zmienna = input("[Y] zeby zaplacic").strip()
        # sprawdzasz czy zmienna jest 'Y'
        # jak tak to return True
        # jak nie - print("Sprobuj ponownie")

        return s.Payment().process_payment()



    def book_visit(self, visit: s.Visit):
        Calendar().add_visit(visit)
