import sys

from users import Client, Administrator


def client_session(user):
    while(True):
        print("-------------------------")
        print("Witamy w myjni!")
        print("[1] Zarezerwuj wizyte")
        print("[2] Odwolaj wizyte")
        print("[3] Sprawdz oferte")
        print("[4] Sprawdz swoje wizyty")
        print("[5] Historia wizyt")
        print("..")
        print("[0] Wyjscie")

        user_choice = input("Wybor: ").strip()

        match user_choice:
            case '1':
                user.reserve_visit()
            case '2':
                user.cancel_visit()
            case '3':
                user.check_offer(False)
            case '4':
                user.check_calendar("niedokonana")
            case '5':
                user.check_calendar("wykonana")
            case '0':
                break
            case _:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")
    

def admin_session(user):
    while(True):
        print("-------------------------")
        print("Witamy w myjni!")
        print("[1] Edytuj liste uslug")
        print("[2] Dodaj usluge")
        print("[3] Usun usluge")
        print("[4] Sprawdz oferte")
        print("[5] Sprawdz wizyty przy ktorych uczestniczysz")
        print("..")
        print("[0] Wyjscie")
        user_choice = input("Wybor: ").strip()
        match user_choice:
            case '1':
                user.edit_service()
            case '2':
                user.add_service()
            case '3':
                user.delete_service()
            case '4':
                user.check_offer()
            case '5':
                user.check_calendar()
            case '0':
                break
            case _:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")


def login_panel(user):
    while(True):
        print("-------------------------")
        print("Witamy w myjni!")
        print("[1] Zaloguj sie")
        print("[2] Zarejestruj sie")
        print("..")
        print("[0] Wyjscie")

        print("-------------------------")
        user_choice = input("Wybor: ").strip()

        match user_choice:
            case '1':
                user.log_in()
                break
            case '2':
                user.register()
            case '0':
                sys.exit()
            case _:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")
          
def welcome_panel():
    while(True):
        print("Wybierz tryb aplikacji:")
        print("[1] Klient")
        print("[2] Wlasciciel")
        print("..")
        print("[0] Wyjscie")
        print("-------------------------")
        mode = input("Wybor: ").strip()
        match mode:
            case '1':
                user = Client()
                login_panel(user)
                client_session(user)
                break
            case '2':
                user = Administrator()
                login_panel(user)
                admin_session(user)
                break
            case '0':
                break
            case _:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

welcome_panel()

