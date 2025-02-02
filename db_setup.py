import mysql.connector 
conn = mysql.connector.connect(host= 'localhost',user= 'root', password='root', database='hospital_management',port=3307)
print("1")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE department (
            doctor_id VARCHAR(10) PRIMARY KEY,
            doctor_name VARCHAR(100),
            department VARCHAR(50),
            doctor_phone VARCHAR(15)
        )""")

cursor.execute("""
        CREATE TABLE patients (
            patient_id INT AUTO_INCREMENT PRIMARY KEY,
            patient_name VARCHAR(100),
            age INT,
            disease VARCHAR(100),
            doctor_id VARCHAR(10),
            FOREIGN KEY (doctor_id) REFERENCES department(doctor_id)
        )
    """)

cursor.execute("""
        CREATE TABLE hbills (
            bill_id INT AUTO_INCREMENT PRIMARY KEY,
            d_visit FLOAT,
            medicine FLOAT,
            toopv FLOAT,
            total_bill FLOAT,
            patient_id INT,
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
        )
    """)


cursor.execute("""
        CREATE TABLE workers (
            worker_id INT AUTO_INCREMENT PRIMARY KEY,
            worker_name VARCHAR(100),
            position VARCHAR(100),
            salary FLOAT
        )
    """)

conn.commit()
print("✅ Tables created successfully!")
conn.close()
def insert_mock_data():
    """Inserts mock data for testing."""


    # Insert mock data into Doctors table
    cursor.execute("""
        INSERT INTO department (doctor_id, doctor_name, department, doctor_phone)
        VALUES
        ('101', 'Dr. A Sharma', 'Cardiology', '9876543210'),
        ('102', 'Dr. B Patel', 'Orthopedics', '9123456789'),
        ('103', 'Dr. C Gupta', 'Dermatology', '9988776655')
    """)

    # Insert mock data into Patients table
    cursor.execute("""
        INSERT INTO patients (patient_name, age, disease, doctor_id)
        VALUES
        ('John Doe', 34, 'Heart Disease', '101'),
        ('Jane Smith', 28, 'Bone Fracture', '102'),
        ('Alice Johnson', 45, 'Skin Allergy', '103')
    """)

    # Insert mock data into Bills table
    cursor.execute("""
        INSERT INTO hbills (d_visit, medicine, toopv, total_bill, patient_id)
        VALUES
        (500, 200, 50, 750, 1),
        (300, 150, 40, 490, 2),
        (200, 100, 30, 330, 3)
    """)

    # Insert mock data into Workers table
    cursor.execute("""
        INSERT INTO workers (worker_name, position, salary)
        VALUES
        ('Raj Kumar', 'Nurse', 3000),
        ('Neha Singh', 'Lab Technician', 3500),
        ('Vikram Yadav', 'Admin', 4000)
    """)

    conn.commit()
    print("✅ Mock data inserted successfully!")
    conn.close()

if __name__ == "__main__":
    insert_mock_data()
