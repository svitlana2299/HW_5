from collections import UserDict

# Цей код визначає класи Field, Name, Phone та Email. Клас Field має атрибут value, який може бути None. Клас Name, Phone та Email є нащадками класу Field.


class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass


class Email(Field):
    pass


class Record:
    def __init__(self, name, phones=None, email=None):
        self.name = Name(name)
        self.phones = [Phone(phone) for phone in phones] if phones else []
        self.email = Email(email) if email else None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, index):
        del self.phones[index]

    def edit_phone(self, index, new_phone):
        self.phones[index] = Phone(new_phone)

    def add_email(self, email):
        self.email = Email(email)

    def remove_email(self):
        self.email = None

    def edit_email(self, new_email):
        self.email = Email(new_email)

    def __str__(self):
        return f"Name: {self.name}\nPhones: {', '.join(str(phone) for phone in self.phones)}"

# Клас AddressBook є нащадком класу UserDict


class AddressBook(UserDict):

    # Метод add_record додає запис до адресної книги.

    def add_record(self, record):
        self.data[record.name.value] = record

    # Метод delete_record видаляє запис з адресної книги за іменем.

    def delete_record(self, name):
        del self.records[name]

    # Метод edit_record редагує запис в адресній книзі за іменем. Якщо виконано зміну імені, то старий запис з іменем видаляється та додається новий зі зміненим іменем.

    def edit_record(self, name, **kwargs):
        record = self.records[name]
        if 'name' in kwargs:
            new_name = kwargs['name']
            record.name.value = new_name
            self.records[new_name] = self.records.pop(name)
            name = new_name
        if 'phones' in kwargs:
            phones = kwargs['phones']
            record.phones = [Phone(phone) for phone in phones]
        if 'email' in kwargs:
            email = kwargs['email']
            record.email = Email(email) if email else None

    # Метод search_records повертає список записів, які задовольняють критерії пошуку. Пошук може бути виконаний за іменем, номером телефону та електронною адресою.

    def search_records(self, **kwargs):
        result = []
        for record in self.data.values():
            for key, value in kwargs.items():
                if key == 'name' and value.lower() in record.name.value.lower():
                    result.append(record)
                elif key == 'phone':
                    for phone in record.phones:
                        if value in phone.value:
                            result.append(record)
                            break
                elif key == 'email' and record.email and value.lower() in record.email.value.lower():
                    result.append(record)
        return result

    # Метод str форматує об'єкт класу Record у вигляді рядка.
    def __str__(self):
        return '\n\n'.join(str(record) for record in self.records.values())
