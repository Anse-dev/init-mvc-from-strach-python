import tkinter as tk
from tkinter import messagebox

class ContactView:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        self.name_label = tk.Label(root, text="Name")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.email_label = tk.Label(root, text="Email")
        self.email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        self.add_button = tk.Button(root, text="Add Contact")
        self.add_button.pack()
        self.delete_button = tk.Button(root, text="Delete Contact")
        self.delete_button.pack()

        self.contact_listbox = tk.Listbox(root)
        self.contact_listbox.pack()

    def get_contact_info(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        return name, email

    def show_contacts(self, contacts):
        self.contact_listbox.delete(0, tk.END)
        for contact in contacts:
            self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.email}")

    def show_message(self, message):
        messagebox.showinfo("Info", message)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
