from tkinter import *

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        # Set the background color of the main window
        self.root.configure(bg='#f0f0f0')
        
        # Maximize the main window
        self.root.state('zoomed')

        # Variables to store contact information
        self.contacts = []

        # Title label
        self.title_label = Label(self.root, text='Contact Book', bg='#f0f0f0', fg='#333333', font=('Arial', 30, 'bold'))
        self.title_label.pack(pady=20)

        # Frame for buttons
        self.button_frame = Frame(self.root, bg='#f0f0f0')
        self.button_frame.pack(pady=10)

        # Add Contact button
        self.add_button = Button(self.button_frame, text='Add Contact', font=('Arial', 18), bg='#4287f5', fg='white', padx=20, pady=10, command=self.add_contact)
        self.add_button.grid(row=0, column=0, padx=10)

        # View Contact List button
        self.view_button = Button(self.button_frame, text='View Contacts', font=('Arial', 18), bg='#05ca51', fg='white', padx=20, pady=10, command=self.view_contacts)
        self.view_button.grid(row=0, column=1, padx=10)

        # Search Contact button
        self.search_button = Button(self.button_frame, text='Search Contact', font=('Arial', 18), bg='#f6b830', fg='white', padx=20, pady=10, command=self.search_contact)
        self.search_button.grid(row=0, column=2, padx=10)

        # Update Contact button
        self.update_button = Button(self.button_frame, text='Update Contact', font=('Arial', 18), bg='#af67c5', fg='white', padx=20, pady=10, command=self.update_contact)
        self.update_button.grid(row=0, column=3, padx=10)

        # Delete Contact button
        self.delete_button = Button(self.button_frame, text='Delete Contact', font=('Arial', 18), bg='#f5334b', fg='white', padx=20, pady=10, command=self.delete_contact)
        self.delete_button.grid(row=0, column=4, padx=10)

        # Clear Display button
        self.clear_button = Button(self.root, text='CLEAR', font=('Arial', 18), bg='#d63230', fg='white', padx=20, pady=10, command=self.clear_display)
        self.clear_button.pack(pady=20)

        # Display area for contact list
        self.contact_list_label = Label(self.root, text='', bg='#f0f0f0', font=('Arial', 18))
        self.contact_list_label.pack(pady=20)

    def add_contact(self):
        """Open a window to add a new contact."""
        add_window = Toplevel(self.root)
        add_window.title("Add Contact")
        add_window.geometry("400x300")

        # Labels and Entry widgets for contact details
        name_label = Label(add_window, text="Name:", font=('Arial', 16), padx=10, pady=10)
        name_label.grid(row=0, column=0)
        self.name_entry = Entry(add_window, font=('Arial', 16), width=30)
        self.name_entry.grid(row=0, column=1)

        phone_label = Label(add_window, text="Phone:", font=('Arial', 16), padx=10, pady=10)
        phone_label.grid(row=1, column=0)
        self.phone_entry = Entry(add_window, font=('Arial', 16), width=30)
        self.phone_entry.grid(row=1, column=1)

        email_label = Label(add_window, text="Email:", font=('Arial', 16), padx=10, pady=10)
        email_label.grid(row=2, column=0)
        self.email_entry = Entry(add_window, font=('Arial', 16), width=30)
        self.email_entry.grid(row=2, column=1)

        address_label = Label(add_window, text="Address:", font=('Arial', 16), padx=10, pady=10)
        address_label.grid(row=3, column=0)
        self.address_entry = Entry(add_window, font=('Arial', 16), width=30)
        self.address_entry.grid(row=3, column=1)

        # Add button to confirm contact addition
        add_button = Button(add_window, text="Add", font=('Arial', 16), bg='#4287f5', fg='white', padx=10, pady=5, command=self.save_contact)
        add_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Close button to close the add window
        close_button = Button(add_window, text="CLOSE", font=('Arial', 16), bg='#d63230', fg='white', padx=20, pady=10, command=add_window.destroy)
        close_button.grid(row=5, column=0, columnspan=2, pady=20)

    def save_contact(self):
        """Save the contact details."""
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts.append({'Name': name, 'Phone': phone, 'Email': email, 'Address': address})
            self.name_entry.delete(0, 'end')
            self.phone_entry.delete(0, 'end')
            self.email_entry.delete(0, 'end')
            self.address_entry.delete(0, 'end')

    def view_contacts(self):
        """View the list of contacts."""
        contact_text = ""
        for contact in self.contacts:
            contact_text += f"Name: {contact['Name']}, Phone: {contact['Phone']}\n"
        self.contact_list_label.config(text=contact_text)

    def search_contact(self):
        """Search for a contact by name or phone number."""
        search_window = Toplevel(self.root)
        search_window.title("Search Contact")
        search_window.geometry("400x150")

        search_label = Label(search_window, text="Search by Name or Phone:", font=('Arial', 16), padx=10, pady=10)
        search_label.grid(row=0, column=0)
        self.search_entry = Entry(search_window, font=('Arial', 16), width=30)
        self.search_entry.grid(row=0, column=1)

        search_button = Button(search_window, text="Search", font=('Arial', 16), bg='#05ca51', fg='white', padx=10, pady=5, command=self.perform_search)
        search_button.grid(row=1, column=0, columnspan=2, pady=10)

    def perform_search(self):
        """Perform the search for the contact."""
        search_term = self.search_entry.get().lower()
        search_result = []

        for contact in self.contacts:
            if search_term in contact['Name'].lower() or search_term in contact['Phone']:
                search_result.append(contact)

        search_result_text = ""
        for contact in search_result:
            search_result_text += f"Name: {contact['Name']}, Phone: {contact['Phone']}\n"

        if search_result_text:
            search_result_label = Label(self.root, text=search_result_text, bg='#f0f0f0', font=('Arial', 18))
            search_result_label.pack(pady=20)
        else:
            no_result_label = Label(self.root, text="No matching contacts found.", bg='#f0f0f0', font=('Arial', 18))
            no_result_label.pack(pady=20)

    def update_contact(self):
        """Update contact details."""
        update_window = Toplevel(self.root)
        update_window.title("Update Contact")
        update_window.geometry("400x300")

        update_label = Label(update_window, text="Enter Contact Name to Update:", font=('Arial', 16), padx=10, pady=10)
        update_label.grid(row=0, column=0)
        self.update_entry = Entry(update_window, font=('Arial', 16), width=30)
        self.update_entry.grid(row=0, column=1)

        update_button = Button(update_window, text="Update", font=('Arial', 16), bg='#af67c5', fg='white', padx=10, pady=5, command=self.perform_update)
        update_button.grid(row=1, column=0, columnspan=2, pady=20)

    def perform_update(self):
        """Perform the update of contact details."""
        update_name = self.update_entry.get().lower()

        for contact in self.contacts:
            if update_name == contact['Name'].lower():
                # Open a window to update the contact details
                update_contact_window = Toplevel(self.root)
                update_contact_window.title("Update Contact")
                update_contact_window.geometry("400x300")

                name_label = Label(update_contact_window, text="Name:", font=('Arial', 16), padx=10, pady=10)
                name_label.grid(row=0, column=0)
                name_entry = Entry(update_contact_window, font=('Arial', 16), width=30)
                name_entry.grid(row=0, column=1)
                name_entry.insert(0, contact['Name'])

                phone_label = Label(update_contact_window, text="Phone:", font=('Arial', 16), padx=10, pady=10)
                phone_label.grid(row=1, column=0)
                phone_entry = Entry(update_contact_window, font=('Arial', 16), width=30)
                phone_entry.grid(row=1, column=1)
                phone_entry.insert(0, contact['Phone'])

                email_label = Label(update_contact_window, text="Email:", font=('Arial', 16), padx=10, pady=10)
                email_label.grid(row=2, column=0)
                email_entry = Entry(update_contact_window, font=('Arial', 16), width=30)
                email_entry.grid(row=2, column=1)
                email_entry.insert(0, contact['Email'])

                address_label = Label(update_contact_window, text="Address:", font=('Arial', 16), padx=10, pady=10)
                address_label.grid(row=3, column=0)
                address_entry = Entry(update_contact_window, font=('Arial', 16), width=30)
                address_entry.grid(row=3, column=1)
                address_entry.insert(0, contact['Address'])

                # Update button to confirm contact update
                update_button = Button(update_contact_window, text="Update", font=('Arial', 16), bg='#4287f5', fg='white', padx=10, pady=5, command=lambda: self.save_update(contact, name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get()))
                update_button.grid(row=4, column=0, columnspan=2, pady=20)

                break

    def save_update(self, contact, name, phone, email, address):
        """Save the updated contact details."""
        contact.update({'Name': name, 'Phone': phone, 'Email': email, 'Address': address})

    def delete_contact(self):
        """Delete a contact."""
        delete_window = Toplevel(self.root)
        delete_window.title("Delete Contact")
        delete_window.geometry("400x150")

        delete_label = Label(delete_window, text="Enter Contact Name to Delete:", font=('Arial', 16), padx=10, pady=10)
        delete_label.grid(row=0, column=0)
        self.delete_entry = Entry(delete_window, font=('Arial', 16), width=30)
        self.delete_entry.grid(row=0, column=1)

        delete_button = Button(delete_window, text="Delete", font=('Arial', 16), bg='#f5334b', fg='white', padx=10, pady=5, command=self.perform_delete)
        delete_button.grid(row=1, column=0, columnspan=2, pady=10)

    def perform_delete(self):
        """Perform the deletion of contact."""
        delete_name = self.delete_entry.get().lower()

        for contact in self.contacts:
            if delete_name == contact['Name'].lower():
                self.contacts.remove(contact)
                break

    def clear_display(self):
        """Clear the displayed contact list."""
        self.contact_list_label.config(text='')

def main():
    root = Tk()
    ui = ContactBook(root)
    root.mainloop()

if __name__ == "__main__":
    main()