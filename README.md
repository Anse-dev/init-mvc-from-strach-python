
### Structure du projet

```
contact_manager/
│
├── model.py
├── view.py
├── controller.py
└── main.py
```

### model.py

Le modèle (Model) représente les données de l'application et la logique métier. 

```python
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
        self.contacts = [contact for contact in self.contacts si contact.email != email]
```

- `Contact` : Classe représentant un contact avec des attributs `name` et `email`.
- `ContactModel` : Classe gérant la liste des contacts, avec des méthodes pour ajouter (`add_contact`), obtenir (`get_contacts`), et supprimer (`delete_contact`) des contacts.

### view.py

La vue (View) représente l'interface utilisateur de l'application.

```python
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
```

- `ContactView` : Classe gérant l'interface utilisateur avec `tkinter`.
  - `get_contact_info` : Récupère les informations saisies par l'utilisateur.
  - `show_contacts` : Affiche la liste des contacts.
  - `show_message` : Affiche un message d'information.
  - `clear_entries` : Efface les champs de saisie.

### controller.py

Le contrôleur (Controller) gère la logique de contrôle entre le modèle et la vue.

```python
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
```

- `ContactController` : Classe gérant les interactions entre le modèle et la vue.
  - `add_contact` : Ajoute un contact en utilisant les informations saisies dans la vue et met à jour la vue.
  - `delete_contact` : Supprime un contact sélectionné dans la vue et met à jour la vue.
  - `update_view` : Met à jour la vue avec la liste des contacts.

### main.py

Le fichier `main.py` initialise le modèle, la vue et le contrôleur, et lance l'application `tkinter`.

```python
import tkinter as tk
from model import ContactModel
from view import ContactView
from controller import ContactController

if __name__ == "__main__":
    root = tk.Tk()
    model = ContactModel()
    view = ContactView(root)
    controller = ContactController(model, view)
    root.mainloop()
```

### Explications supplémentaires

- **Model (Modèle)** : Représente les données et la logique métier. Dans notre cas, `ContactModel` gère les contacts.
- **View (Vue)** : Représente l'interface utilisateur. Dans notre cas, `ContactView` gère l'affichage et les interactions avec l'utilisateur.
- **Controller (Contrôleur)** : Gère les interactions entre le modèle et la vue. Dans notre cas, `ContactController` gère la logique pour ajouter et supprimer des contacts et met à jour la vue.

Ce pattern sépare clairement les responsabilités, rendant le code plus maintenable et extensible. En lançant `main.py`, vous aurez une application graphique simple permettant d'ajouter et de supprimer des contacts, démontrant ainsi le pattern MVC en action.
