# Display the in-app messages
print("Welcome to your contact book")
print("Here you can create and save contacts")
print("Choose any of the below options to start with your contact books")

# Add new contacts to memory of contact book 
def add(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address}) # attach details to contact
    print(f"Contact {name} added successfully.")

def display(contacts):                      # display saveed contacts
    if not contacts:                                 # empty memory/no saved contacts
        print("No contacts found.")
    else:
        for contact in contacts:                         
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def search(contacts):
    search_term = input("Enter name or phone to search: ")
    results = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    if not results:
        print("No contacts found.")
    else:
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def update(contacts):
    name = input("Enter name of the contact to update: ")
    for contact in contacts:
        if contact['name'] == name:
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email: ")
            contact['address'] = input("Enter new address: ")
            print(f"Contact {name} updated successfully.")
            return
    print(f"Contact {name} not found.")

def delete(contacts):
    name = input("Enter name of the contact to delete: ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print(f"Contact {name} deleted successfully.")
            return
    print(f"Contact {name} not found.")

def main():
    contacts = []
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add(contacts)
        elif choice == '2':
            display(contacts)
        elif choice == '3':
            search(contacts)
        elif choice == '4':
            update(contacts)
        elif choice == '5':
            delete(contacts)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
