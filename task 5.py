import tkinter as tk
from tkinter import messagebox
class ContactBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = {}
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(self.root, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        tk.Label(self.root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        tk.Label(self.root, text="Address:").grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, pady=10)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=4, column=1, pady=10)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).grid(row=5, column=0, pady=10)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=5, column=1, pady=10)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=6, column=0, pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit).grid(row=6, column=1, pady=10)
    def add_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            messagebox.showerror("Error", "Contact already exists.")
            return
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        messagebox.showinfo("Success", f"Contact '{name}' added successfully.")
        self.clear_entries()
    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Contact List", "No contacts found.")
            return
        contact_list = "\n".join([f"Name: {name}, Phone: {details['phone']}" for name, details in self.contacts.items()])
        messagebox.showinfo("Contact List", contact_list)
    def search_contact(self):
        search = self.name_entry.get()
        found = False
        for name, details in self.contacts.items():
            if search == name or search == details['phone']:
                contact_info = f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}"
                messagebox.showinfo("Contact Found", contact_info)
                found = True
                break
        if not found:
            messagebox.showerror("Error", "Contact not found.")
    def update_contact(self):
        name = self.name_entry.get()
        if name not in self.contacts:
            messagebox.showerror("Error", "Contact not found.")
            return
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        messagebox.showinfo("Success", f"Contact '{name}' updated successfully.")
        self.clear_entries()
    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact '{name}' deleted successfully.")
        else:
            messagebox.showerror("Error", "Contact not found.")
        self.clear_entries()
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookGUI(root)
    root.mainloop()
