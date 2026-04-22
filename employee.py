class Employee:
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        self.name = name
        self.employee_id = employee_id
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is None or str(value).strip() == "":
            raise ValueError("Name cannot be empty.")
        self._name = str(value).strip()

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        if value is None or str(value).strip() == "":
            raise ValueError("Employee ID cannot be empty.")
        self._employee_id = str(value).strip()

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        value = float(value)
        if value < 0:
            raise ValueError("Hourly rate cannot be negative.")
        self._hourly_rate = value

    @property
    def hours_worked(self):
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        value = float(value)
        if value < 0:
            raise ValueError("Hours worked cannot be negative.")
        if value > 168:
            raise ValueError("Hours worked cannot exceed 168.")
        self._hours_worked = value

    def calculate_gross_pay(self):
        if self.hours_worked <= 40:
            return self.hourly_rate * self.hours_worked
        else:
            regular = 40 * self.hourly_rate
            overtime_hours = self.hours_worked - 40
            overtime = overtime_hours * self.hourly_rate * 1.5
            return regular + overtime

    def __str__(self):
        return (
            f"Name: {self.name}, ID: {self.employee_id}, "
            f"Rate: ${self.hourly_rate:.2f}, Hours: {self.hours_worked:.1f}, "
            f"Gross Pay: ${self.calculate_gross_pay():.2f}"
        )
