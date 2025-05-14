# return users who use gmail in the email
contacts = [
    {"name": "Alice", "email": "alice@gmail.com"},
    {"name": "Bob", "email": "bob@yahoo.com"},
    {"name": "Charlie", "email": "charlie@gmail.com"}
]

def searchEmail(contacts):
    def email_with():
        for contact in contacts.values():
            if '@gmail.com' in contact:
                return contact
            else:
                print('you are no using email')
            
new=searchEmail(contacts)
new()            
