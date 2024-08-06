import tkinter as tk

class ContactController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.add_button.config(command=self.add_contact)
        self.view.delete_button.config(command=self.delete_contact)
        self.update_view()

    def add_contact(self):
        name, email = self.view.get_contact_info()
        if name and email:
            self.model.add_contact(name, email)
            self.update_view()
            self.view.clear_entries()
            self.view.show_message("Contact added successfully")
        else:
            self.view.show_message("Please enter both name and email")

    def delete_contact(self):
        selected_contact = self.view.contact_listbox.get(tk.ACTIVE)
        if selected_contact:
            email = selected_contact.split(" - ")[1]
            self.model.delete_contact(email)
            self.update_view()
            self.view.show_message("Contact deleted successfully")
        else:
            self.view.show_message("Please select a contact to delete")

    def update_view(self):
        contacts = self.model.get_contacts()
        self.view.show_contacts(contacts)
