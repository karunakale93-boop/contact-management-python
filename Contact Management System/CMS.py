import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="karuna4590",   
    database="contact_db"
)

cur = con.cursor()

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    sql = "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)"
    cur.execute(sql, (name, phone, email))
    con.commit()
    print("Contact Added Successfully!")

def view_contacts():
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()

    if rows:
        print("\n--- Contact List ---")
        for r in rows:
            print(f"ID: {r[0]}, Name: {r[1]}, Phone: {r[2]}, Email: {r[3]}")
    else:
        print("No contacts found.")

def search_contact():
    name = input("Enter name to search: ")
    sql = "SELECT * FROM contacts WHERE name LIKE %s"
    cur.execute(sql, ('%' + name + '%',))
    rows = cur.fetchall()

    if rows:
        for r in rows:
            print(f"ID: {r[0]}, Name: {r[1]}, Phone: {r[2]}, Email: {r[3]}")
    else:
        print("Contact not found.")

def update_contact():
    id = input("Enter Contact ID to update: ")
    phone = input("Enter new phone: ")
    email = input("Enter new email: ")

    sql = "UPDATE contacts SET phone=%s, email=%s WHERE id=%s"
    cur.execute(sql, (phone, email, id))
    con.commit()
    print("Contact Updated Successfully!")

def delete_contact():
    id = input("Enter Contact ID to delete: ")
    sql = "DELETE FROM contacts WHERE id=%s"
    cur.execute(sql, (id,))
    con.commit()
    print("Contact Deleted Successfully!")

while True:
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

con.close()