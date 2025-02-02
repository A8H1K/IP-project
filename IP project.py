import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: MySQL Connection Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'hospital_management'
}

def connect_db():
    """Connects to the hospital_management MySQL database."""
    return mysql.connector.connect(**DB_CONFIG,port='3307')

def menu():
    """Displays the hospital management system menu."""
    print("\n*****************************************************************")
    print("                  HOSPITAL MANAGEMENT SYSTEM                    ")
    print("*****************************************************************\n")
    print("Data Analysis")
    print("1. Display Doctor details")
    print("2. Add a New Doctor")
    print("3. Sort Doctors by Name")
    print("4. Display Patient details")
    print("5. Delete a Column from Patients Table")
    print("6. Display All Bills")
    print("7. Display Total Bills")
    print("8. Increase Doctor Visit Charges by Rs 250")
    print("9. Display Worker Records")
    print("10. Display Highest Salary")
    print("11. Increase Worker Salary by Rs 250")
    print("\nData Visualization")
    print("12. Hbill Bar Plot")
    print("\n*****************************************************************")

# Step 2: Functionality for Each Option
def display_doctors():
    """Fetch and display doctor details."""
    conn = connect_db()
    df = pd.read_sql("SELECT * FROM department", conn)
    print(df)
    conn.close()

def add_new_doctor():
    """Adds a new doctor record."""
    conn = connect_db()
    cursor = conn.cursor()

    doctor_id = input("Enter Doctor ID: ")
    name = input("Enter Doctor Name: ")
    department = input("Enter Department: ")
    phone = input("Enter Doctor Phone: ")

    cursor.execute("INSERT INTO department VALUES (%s, %s, %s, %s)", 
                   (doctor_id, name, department, phone))
    conn.commit()
    print(" Doctor Added Successfully!")
    conn.close()

def sort_doctors():
    """Sorts and displays doctors by name."""
    conn = connect_db()
    df = pd.read_sql("SELECT * FROM department ORDER BY doctor_name ASC", conn)
    print(df)
    conn.close()

def display_patients():
    """Fetch and display patient details."""
    conn = connect_db()
    df = pd.read_sql("SELECT * FROM patients", conn)
    print(df)
    conn.close()

def delete_patient_column():
    """Deletes the 'age' column from the patients table (if exists)."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("ALTER TABLE patients DROP COLUMN disease ")
    conn.commit()
    print("disease column deleted (if it existed).")
    conn.close()

def display_bills():
    """Fetch and display all hospital bills."""
    conn = connect_db()
    df = pd.read_sql("SELECT * FROM hbills", conn)
    print(df)
    conn.close()

def display_total_bills():
    """Calculates and displays total bills."""
    conn = connect_db()
    df = pd.read_sql("SELECT *,sum(d_visit) +  sum(medicine)+ sum(toopv) AS total_bill FROM hbills", conn)
    print(df[['bill_id', 'total_bill']])
    conn.close()

def increase_doctor_fee():
    """Increases doctor visit charges by Rs 250."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE hbills SET d_visit = d_visit + 250")
    conn.commit()
    print("Doctor visit charges increased by Rs 250!")
    conn.close()

def display_workers():
    """Fetch and display worker records."""
    conn = connect_db()
    df = pd.read_sql("SELECT * FROM workers", conn)
    print(df)
    conn.close()

def highest_salary():
    """Displays the highest salary in the workers table."""
    conn = connect_db()
    df = pd.read_sql("SELECT MAX(salary) AS highest_salary FROM workers", conn)
    print(df)
    conn.close()

def increase_worker_salary():
    """Increases all workers' salary by Rs 250."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE workers SET salary = salary + 250")
    conn.commit()
    print("Workers' salaries increased by Rs 250!")
    conn.close()

def hbill_bar_plot():
    """Generates a bar plot for hospital bills."""
    conn = connect_db()
    df = pd.read_sql("SELECT medicine, d_visit FROM hbills", conn)
    conn.close()

    plt.figure(figsize=(10, 5))
    plt.xlabel('Medicine Cost', fontsize=14, color='red')
    plt.ylabel('Doctor Visit Cost', fontsize=14)
    plt.title('Charges of Medicine and Doctor Visits')
    plt.bar(df['medicine'], df['d_visit'], width=40, color='red', edgecolor='green')
    plt.show()

# Step 3: Main Execution (Menu System)
if __name__ == "__main__":
    while True:
        menu()
        choice = input("\nEnter your choice (or type 'exit' to quit): ")

        if choice == '1':
            display_doctors()
        elif choice == '2':
            add_new_doctor()
        elif choice == '3':
            sort_doctors()
        elif choice == '4':
            display_patients()
        elif choice == '5':
            delete_patient_column()
        elif choice == '6':
            display_bills()
        elif choice == '7':
            display_total_bills()
        elif choice == '8':
            increase_doctor_fee()
        elif choice == '9':
            display_workers()
        elif choice == '10':
            highest_salary()
        elif choice == '11':
            increase_worker_salary()
        elif choice == '12':
            hbill_bar_plot()
        elif choice.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
