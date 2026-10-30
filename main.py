class Family:
    def __init__(self, family_id, name, members):
        self.family_id = family_id
        self.name = name
        self.members = members

    def display_info(self):
        return f"{self.family_id}, {self.name}, {self.members} members"


class FoodBank:
    def __init__(self):
        self.history = []
        self.families = {}
        self.ids = set()
        self.stock = 0
        self.total = 0

    def register_family(self, family_id, name, members):
        if not family_id or not name:
            print("Family ID or name can't be empty.")

        elif members <= 0:
            print("Number of members must be greater than 0.")

        elif family_id in self.ids:
            print("This ID is already registered.")

        else:
            family = Family(family_id, name, members)
            self.families[family_id] = family
            self.ids.add(family_id)
            print("Family Registered!")

    def add_food(self, quantity):
        if quantity <= 0:
            print("Quantity must be greater than 0.")
        else:
            self.stock += quantity
            print("Current stock:", self.stock)

    def food_distribution(self, family_id, quantity):
        if family_id not in self.ids:
            print("Family not found.")

        elif quantity <= 0:
            print("Invalid food quantity.")

        elif quantity > self.stock:
            print("Not enough food in stock!")

        else:
            self.stock -= quantity
            self.history.append((family_id, quantity))
            self.total += quantity
            print("Remaining stock:", self.stock)

    def show_report(self):
        print("\n=========== FOOD BANK REPORT ===========")
        print("Available stock:", self.stock)

        print("\n----- Registered Families -----")

        if not self.families:
            print("No families registered.")

        for family_id in self.families:
            family = self.families[family_id]
            print(family.display_info())

        print("\n----- Distribution History -----")

        if not self.history:
            print("No history.")

        for family_id, quantity in self.history:
            print(family_id, "received", quantity, "packs")

        print("Total Distributed:", self.total)


def main():
    food_bank = FoodBank()

    while True:
        print("\n===== COMMUNITY FOOD BANK =====")
        print("1. Register Family")
        print("2. Add Food Packs")
        print("3. Distribute Food Packs")
        print("4. Show Report")
        print("5. Exit")

        try:
            choice = input("Enter choice: ").strip()

            if choice == "1":
                family_id = input("Family ID: ").strip()
                name = input("Family Name: ").strip()
                members = int(input("Number of Members: "))

                food_bank.register_family(family_id, name, members)

            elif choice == "2":
                packs = int(input("Packs to add: "))
                food_bank.add_food(packs)

            elif choice == "3":
                family_id = input("Family ID: ").strip()
                packs = int(input("Packs requested: "))

                food_bank.food_distribution(family_id, packs)

            elif choice == "4":
                food_bank.show_report()

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select 1 to 5.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")


main()