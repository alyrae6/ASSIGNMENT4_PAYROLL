from payroll_processor import PayrollProcessor

class PayrollReport:
    def __init__(self, processor: PayrollProcessor):
        self.processor = processor

    def display_all_employees(self):
        print("Name\tID\tRate\tHours\tGross Pay")
        for emp in self.processor.employees:
            gross = emp.calculate_gross_pay()
            print(
                f"{emp.name}\t{emp.employee_id}\t"
                f"${emp.hourly_rate:.2f}\t{emp.hours_worked:.1f}\t"
                f"${gross:.2f}"
            )

    def display_payroll_summary(self):
        count = self.processor.get_employee_count()
        total = self.processor.calculate_total_payroll()
        avg = self.processor.calculate_average_pay()
        highest = self.processor.find_highest_paid()
        lowest = self.processor.find_lowest_paid()

        print("Payroll Summary")
        print(f"Total employees: {count}")
        print(f"Total payroll: ${total:.2f}")
        print(f"Average pay: ${avg:.2f}")

        if highest is not None:
            print(f"Highest paid: {highest.name} (${highest.calculate_gross_pay():.2f})")
        if lowest is not None:
            print(f"Lowest paid: {lowest.name} (${lowest.calculate_gross_pay():.2f})")

    def generate