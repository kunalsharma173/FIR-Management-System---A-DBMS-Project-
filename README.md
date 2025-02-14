# Police FIR Management System

![Python](https://img.shields.io/badge/Python-3.x-blue)  
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)  
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)  

## Overview
A **Police FIR Management System** developed using Python's **Tkinter** for the GUI and **MySQL** for database management. The system allows users to log in and register **First Information Reports (FIRs)** with details such as complainant name, contact information, incident details, and lost items.

## Features
### 🔑 User Authentication
- Secure login system with username and password.

### 📄 FIR Entry Form
- Collects details like complainant's name, address, contact details, incident details, and description.

### 🗄️ Database Integration
- Stores FIR data in a MySQL database.

### 🔎 Retrieve FIR Details
- Search FIR records based on complainant name.

### 🛠️ Data Management
- Ability to insert, clear, and exit the system.

### 🖥️ GUI Interface
- Built using Tkinter for user-friendly interaction.

## Installation
### Clone the Repository
```bash
git clone https://github.com/your-username/police-fir-management.git
cd police-fir-management
```

### Install Dependencies
Ensure you have **Python 3.x** installed. Then, install the required libraries:
```bash
pip install mysql-connector-python pillow
```

### Run the Application
Execute the Python script to start the application:
```bash
python DBMS_PROJECT1.PY
```

## Database Schema
This project uses **MySQL** for database management. The database schema includes the following table:
```sql
CREATE TABLE fir_entries1 (
    name VARCHAR(100),
    f_name VARCHAR(100),
    address VARCHAR(100),
    c_num BIGINT(10) PRIMARY KEY,
    email_id VARCHAR(100),
    place VARCHAR(100),
    date1 BIGINT(10),
    time1 VARCHAR(10),
    lost VARCHAR(100),
    description VARCHAR(200)
);
```
## Contributing
Contributions are welcome! Follow these steps to contribute:

1. **Fork** the repository.
2. **Create a new branch:**
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Commit your changes:**
   ```bash
   git commit -m 'Add some feature'
   ```
4. **Push to the branch:**
   ```bash
   git push origin feature/YourFeature
   ```
5. **Open a pull request.**


## Contact
For any questions or feedback, feel free to reach out:

---
🚀 Happy Coding! 🎯

