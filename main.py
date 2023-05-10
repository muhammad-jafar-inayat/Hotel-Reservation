class HotelReservation:
    def __init__(self):
        self.reservations = {}
        self.tenants = {}

    def add_reservation(self, tenant_id,capacity, name, checkout_date, checkin_date, cost, reservation_number):
        if reservation_number in self.reservations:
            print("Reservation number already exists")
        else:
            self.reservations[reservation_number] = {
                "capacity": capacity,
                "confirmation_list": [],
                "waiting_list": [],
                "checkin_date": checkin_date,
                "checkout_date": checkout_date,
                "total_revenue": 0
            }
            print(f"Reservation {reservation_number} added")
            reservation = self.reservations[reservation_number]
            if len(reservation["confirmation_list"]) < reservation["capacity"]:
                reservation["confirmation_list"].append(tenant_id)
                reservation["total_revenue"] += cost
                status = "confirmed"
            else:
                reservation["waiting_list"].append(tenant_id)
                status = "waiting"
            self.tenants[tenant_id] = {
                "name": name,
                "checkout_date": checkout_date,
                "checkin_date": checkin_date,
                "cost": cost,
                "reservation_number": reservation_number,
                "status": status
            }
            print(f"Tenant {tenant_id} added to reservation {reservation_number} with status {status}")
    def delete_reservation(self, reservation_number):
        if reservation_number in self.reservations:
            del self.reservations[reservation_number]
            print(f"Reservation {reservation_number} deleted")
        else:
            print(f"Reservation {reservation_number} not found")

    def search_tenant(self, tenant_id):
        if tenant_id in self.tenants:
            return self.tenants[tenant_id]
        else:
            print(f"Tenant with ID {tenant_id} not found")

    def print_report(self, tenant_id):
        if tenant_id in self.tenants:
            tenant_info = self.tenants[tenant_id]
            reservation_info = self.reservations[tenant_info["reservation_number"]]
            print(f"Tenant ID: {tenant_id}")
            print(f"Name: {tenant_info['name']}")
            print(f"Check-in date: {reservation_info['checkin_date']}")
            print(f"Check-out date: {reservation_info['checkout_date']}")
            print(f"Reservation number: {tenant_info['reservation_number']}")
            print(f"Cost of stay: {tenant_info['cost']}")
        else:
            print(f"Tenant with ID {tenant_id} not found")

    def print_confirmed_tenants(self, reservation_number):
        if reservation_number in self.reservations:
            confirmation_list = self.reservations[reservation_number]["confirmation_list"]
            if len(confirmation_list) > 0:
                print(f"Confirmed tenants for reservation {reservation_number}:")
                for tenant_id in confirmation_list:
                    print(f"{tenant_id}: {self.tenants[tenant_id]['name']}")
            else:
                print(f"No confirmed tenants for reservation {reservation_number}")
        else:
            print(f"Reservation {reservation_number} not found")

    def print_waiting_list(self, reservation_number):
        if reservation_number in self.reservations:
            waiting_list = self.reservations[reservation_number]["waiting_list"]
            if len(waiting_list) > 0:
                print(f"Waiting list for reservation {reservation_number}:")
                for tenant_id in waiting_list:
                    print(f"{tenant_id}: {self.tenants[tenant_id]['name']}")
            else:
                print(f"No tenants on waiting list for reservation {reservation_number}")
        else:
            print(f"Reservation {reservation_number} not found")

    def calculate_revenue(self):
        for reservation_number in self.reservations:
            reservation = self.reservations[reservation_number]
            confirmed_tenants = len(reservation["confirmation_list"])
            total_revenue = confirmed_tenants * reservation["total_revenue"]
            print(f"Reservation {reservation_number} revenue: {total_revenue}")

    def print_total_revenue(self):
        for reservation_number, reservation in self.reservations.items():
            print(f"Reservation {reservation_number} revenue: {reservation['total_revenue']}")

def main():
    hotel = HotelReservation()

    while True:
        print("\nMenu:")
        print("1. Add a new reservation")
        print("2. Delete reservation")
        print("3. Search for a tenant using the ID number")
        print("4. Print a report for a given tenant using his ID number")
        print("5. Print the confirmed tenants given a reservation number")
        print("6. Print the waiting list of tenants given a reservation")
        print("7. Print total hotel revenue of each room reserved")
        print("8. Exit from the system")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            reservation_number = int(input("Enter reservation number: "))
            capacity = int(input("Enter reservation capacity: "))
            checkin_date = input("Enter check-in date (YYYY-MM-DD): ")
            checkout_date = input("Enter check-out date (YYYY-MM-DD): ")
            cost = int(input("Enter cost: "))
            name= input("Enter name: ")
            tenant_id = int(input("Enter tenant ID: "))
            hotel.add_reservation(tenant_id,capacity, name, checkout_date, checkin_date, cost, reservation_number)
        elif choice == 2:
            reservation_number = int(input("Enter reservation number: "))
            hotel.delete_reservation(reservation_number)
        elif choice == 3:
            tenant_id = int(input("Enter tenant ID: "))
            print(hotel.search_tenant(tenant_id))
        elif choice == 4:
            tenant_id = int(input("Enter tenant ID: "))
            hotel.print_report(tenant_id)
        elif choice == 5:
            reservation_number = int(input("Enter reservation number: "))
            hotel.print_confirmed_tenants(reservation_number)
        elif choice == 6:
            reservation_number = int(input("Enter reservation number: "))
            hotel.print_waiting_list(reservation_number)
        elif choice == 7:
            hotel.print_total_revenue()
        elif choice == 8:
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()        

