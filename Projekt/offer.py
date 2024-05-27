import csv
import structures as s
import methods as m

class Offer:
    def __init__(self):
        self.services = []
        with open('./services.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if any(row):
                    o_description, o_price, o_contractor_login = map(m.parse_value, row)
                    self.services.append(s.Service(o_description, o_price, o_contractor_login))

    def show_offer(self):
        return self.services

    def edit_offer(self,admin_login):
        while True:
            edit_service_id = int(input("Podaj numer usługi do edycji: ").strip())
            print("Podaj nowe dane wybranej usługi")
            service_description = input("Opis usługi: ").strip()
            service_price = int(input("Cena usługi: ").strip())
            service = s.Service(service_description, service_price, admin_login)

            with open('./services.csv', 'r', newline='', encoding='utf-8') as csvfile:
                rows = list(csv.reader(csvfile))

            if 0 < edit_service_id <= len(rows):
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