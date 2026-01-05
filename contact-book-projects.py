```python
# Display Menu
def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")
        
# 1. Add Contact
def add_contact(contact_book):
    name = input()
    if name in contact_book:
        print("Contact already exists!")
        return
    phone = input()
    email = input()
    address = input()
    contact_book[name] = {
        "phone": phone, 
        "email": email, 
        "address": address
        }
    print("Contact added successfully!")
    return

# 2. View Contact
def view_contact(contact_book):
    name = input()
    if name in contact_book:
        contact = contact_book[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
    else:
        print("Contact not found!")
    
# 3. Edit Contact
def edit_contact(contact_book):
    name = input()
    if name in contact_book:
        contact = contact_book[name]
        phone = input()
        contact["phone"] = phone
        email = input()
        contact["email"] = email
        address = input()
        contact["address"] = address
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

# 4. Delete Contact
def delete_contact(contact_book):
    name = input()
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

# 5. List All Contacts
def list_all_contacts(contact_book):
    if contact_book != {}:
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("")
    else:
        print("No contacts available.")

contact_book = {}

# Run functions
while True:    
    display_menu()    
    choice = input()
    if choice == "1":
        add_contact(contact_book)
    elif choice == "2":
        view_contact(contact_book)
    elif choice == "3":
        edit_contact(contact_book)
    elif choice == "4":
        delete_contact(contact_book)
    elif choice == "5":
        list_all_contacts(contact_book)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")

```
