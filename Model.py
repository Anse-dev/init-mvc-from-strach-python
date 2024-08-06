class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class ContactModel:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, email):
        contact = Contact(name, email)
        self.contacts.append(contact)

    def get_contacts(self):
        return self.contacts

    def delete_contact(self, email):
        self.contacts = [contact for contact in self.contacts if contact.email != email]
