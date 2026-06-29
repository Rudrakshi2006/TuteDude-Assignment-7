import psycopg2

# ---------------- CONNECT TO POSTGRES ----------------
conn = psycopg2.connect(
    host="localhost",
    database="studentdb",
    user="postgres",
    password="mypassword"
)

cursor = conn.cursor()
print("✅ Connected to database successfully")

# ---------------- CREATE TABLE ----------------
create_table_query = """
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50)
);
"""

cursor.execute(create_table_query)
conn.commit()
print("✅ Table created successfully")

# ---------------- INSERT STATIC DATA ----------------
insert_query = """
INSERT INTO students (name, age, course)
VALUES (%s, %s, %s);
"""

data = ("Amit", 20, "CSE")
cursor.execute(insert_query, data)
conn.commit()
print("✅ Static record inserted")

# ---------------- USER INPUT INSERTION ----------------
name = input("Enter name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

cursor.execute(insert_query, (name, age, course))
conn.commit()
print("✅ User record inserted")

# ---------------- FETCH ALL RECORDS ----------------
cursor.execute("SELECT * FROM students;")
rows = cursor.fetchall()

print("\n📌 All Records:")
for row in rows:
    print(row)

# ---------------- SELECT WITH WHERE CONDITION ----------------
cursor.execute("SELECT * FROM students WHERE age > 18;")
filtered = cursor.fetchall()

print("\n📌 Students with age > 18:")
for row in filtered:
    print(row)

# ---------------- TRUNCATE TABLE ----------------
cursor.execute("TRUNCATE TABLE students;")
conn.commit()
print("\n✅ Table truncated successfully")

# ---------------- CLOSE CONNECTION ----------------
cursor.close()
conn.close()
print("🔒 Connection closed")