import user
import methods
import csv
import sys
import structures as s
import calendar
import offer as ofr


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
        

class Client(user.User):
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
                is_login_taken = methods.check_user_in_database(login, password1, "register","Client")
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
            login_data_correct = methods.check_user_in_database(login, password, "login", "Client")
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
        calendar.Calendar().delete_visit(self.login)
        

    def check_offer(self, flag) -> ofr.Offer:
        offer = ofr.Offer().show_offer()

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
        dates = [date for date in calendar.Calendar().show_calendar() if date.client_login == self.login and date.status == status]
        print("-------------------------")
        print("Twoje uslugi")
        for i, visit in enumerate(dates):
            print(f"[{i+1}] {visit.service_info} data: {visit.date} status: {visit.status}")

    def pay(self) -> bool:
        return s.Payment().process_payment()

    def book_visit(self, visit: s.Visit):
        calendar.Calendar().add_visit(visit)