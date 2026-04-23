from payroll_processor import PayrollProcessor
from payroll_report import PayrollReport

def main():
    processor = PayrollProcessor()
    processor.load_from_file("employees.txt")
    report = PayrollReport(processor)

    while True:
        print("Payroll Management System")
        print("(1) View all employees")
        print("(2) View payroll summary")
        print("(3) Generate report file")
        print("(4) Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            report.display_all_employees()

        elif choice == "2":
            report.display_payroll_summary()

        elif choice == "3":
            filename = input("Enter report filename (e.g., report.txt): ").strip()
            if filename == "":
                filename = "payroll_report.txt"
            report.generate_report_file(filename)
            print(f"Report written to {filename}")

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please try again.")

        print()

if __name__ == "__main__":
    main()
