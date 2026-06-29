# Database Operations using Python and PostgreSQL

## Assignment Overview

This project demonstrates how to perform basic database operations in PostgreSQL using Python and the `psycopg2` library.

## Objectives

- Connect Python to a PostgreSQL database.
- Create a table in PostgreSQL.
- Insert static and user-provided data into the table.
- Fetch and display records from the table.
- Execute SELECT queries with WHERE conditions.
- Perform the TRUNCATE TABLE operation.
- Close the database connection properly.

---

## Technologies Used

- Python 3.x
- PostgreSQL
- psycopg2 Library
- pgAdmin 4

---

## Prerequisites

- Python installed
- PostgreSQL installed and running
- pgAdmin 4
- psycopg2 library installed

Install psycopg2 using:

```bash
pip install psycopg2-binary
```

---

## Database Setup

1. Open pgAdmin.
2. Create a database named:

```sql
CREATE DATABASE studentdb;
```

3. Update the connection details in the Python file:

```python
host = "localhost"
database = "studentdb"
user = "postgres"
password = "your_password"
```

---

## Features Implemented

- Connect to PostgreSQL database
- Create `students` table
- Insert predefined records
- Insert records using user input
- Display all records
- Display records using a WHERE condition
- Truncate the table
- Close database connection

---

## Project Structure

```
Database_Operations/
│
├── db_operations.py
├── README.md
└── screenshots/
```

---

## Expected Output

The program performs the following operations:

- Connects to PostgreSQL successfully.
- Creates the students table (if it does not already exist).
- Inserts static and dynamic records.
- Displays all stored records.
- Displays filtered records using a WHERE condition.
- Truncates the table.
- Closes the database connection.

---

## Sample Output

```
Connected to database successfully
Table created successfully
Static record inserted

Enter name: Rahul
Enter age: 21
Enter course: CSE

User record inserted

All Records:
(1, 'Amit', 20, 'CSE')
(2, 'Rahul', 21, 'CSE')

Students with age > 18:
(1, 'Amit', 20, 'CSE')
(2, 'Rahul', 21, 'CSE')

Table truncated successfully
Connection closed
```

---

## Learning Outcomes

- Python and PostgreSQL integration
- Database connectivity using psycopg2
- SQL execution from Python
- Parameterized queries
- Fetching and filtering data
- Transaction management using commit()
- Proper resource cleanup using close()

---

