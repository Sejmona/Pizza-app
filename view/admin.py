class AdminUI:
    def display_login(self):
        return input("Enter admin password: ")

    def display_sales_summary(self, summary):
        for pizza, count in summary.items():
            print(f"{pizza}: {count} sold")
