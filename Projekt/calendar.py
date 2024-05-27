import csv
import structures as s
import methods as m


    
class Calendar:
    def __init__(self):
        self.visits = []
        with open('./visits.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if any(row):
                    v_date, v_service_info, v_client_login, v_done, v_payed, v_contractor_login = map(m.parse_value, row)
                    self.visits.append(s.Visit(v_date, v_service_info, v_client_login, v_done, v_payed, v_contractor_login))

    def show_calendar(self):
        return self.visits

    def add_visit(self, visit: s.Visit):
        data = list(map(str,[visit.date, visit.service_info, visit.client_login, visit.status, visit.payed, visit.contractor_login]))
        print(data)
        with open('./visits.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

    def delete_visit(self, client_login):

        del_visits = [visit for visit in self.visits if visit.client_login == client_login and visit.status == "niedokonana"]

        if not del_visits:
            print("Brak nadchodzacych wizyt.")
            return

        while True:
            for idx, visit in enumerate(del_visits, start=1):
                print(f"[{idx}] {visit.service_info} data: {visit.date} status: {visit.status}")

            try:
                delete_visit_id = int(input("Podaj numer wizyty do usunięcia: ").strip())

                if 1 <= delete_visit_id <= len(del_visits):
                    visit_to_remove = del_visits[delete_visit_id - 1]
                    self.visits.remove(visit_to_remove)
                    print("-------------------------")
                    print("Wizyta usunięta.")
        
                    with open('./visits.csv', mode='w', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        for visit in self.visits:
                            writer.writerow([visit.date, visit.service_info, visit.client_login, visit.status, visit.payed, visit.contractor_login])
                    break
                else:
                    print("-------------------------")
                    print("Nieprawidłowy numer usługi.")
            except ValueError:
                print("-------------------------")
                print("Nieprawidłowy numer usługi.")