class Owner:
    def __init__(self, name, surname, email, birth_date):
        self.name = name
        self.surname = surname
        self.email = email
        self.birth_date = birth_date

    
    def __str__(self):
        return f'Owner{{name={self.name}, surname={self.surname}, email={self.email}, birth_date={self.birth_date}}}'


