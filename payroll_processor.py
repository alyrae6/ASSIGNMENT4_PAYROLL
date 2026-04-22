from employee import Employee

class PayrollProcessor:
    def __init__(self):
        self._employees = []

    @property
    def employees(self):
        return list(self._employees)

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue

                    parts = line.split("\t")
                    if len(parts) != 4:
                        print(f"Warning: malformed line skipped: {line}")
                        continue

                    name, emp_id, rate_str, hours_str = parts

                    try:
                        rate = float(rate_str)
                        hours = float(hours_str)
                        employee = Employee(name, emp_id, rate, hours)
                        self._employees.append(employee)
                    except ValueError as e:
                        print(f"Warning: bad data for line: {line} ({e})")

        except FileNotFoundError:
            print(f"Error: file '{filename}' not found.")

    def calculate_total_payroll(self):
        return sum(emp.calculate_gross_pay() for emp in self._employees)

    def find_highest_paid(self):
        if not self._employees:
            return None
        return max(self._employees, key=lambda e: e.calculate_gross_pay())

    def find_lowest_paid(self):
        if not self._employees:
            return None
        return min(self._employees, key=lambda e: e.calculate_gross_pay())

    def get_employee_count(self):
        return len(self._employees)

    def calculate_average_pay(self):
        if not self._employees:
            return 0.0
        return self.calculate_total_payroll() / len(self._employees)
