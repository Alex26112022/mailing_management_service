import csv
import os


def write_csv(name, phone, message):
    """ Записывает данные формы в csv-файл. """
    csv_file_exists = os.path.isfile('contacts.csv')
    with (open('contacts.csv', 'a', encoding='utf-8', newline='') as
          csvfile):
        fieldnames = ['Имя', 'Телефон', 'Сообщение']
        if not csv_file_exists:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
    with open('contacts.csv', 'a', encoding='utf-8', newline='') as file:
        field = ['Имя', 'Телефон', 'Сообщение']
        wr = csv.DictWriter(file, fieldnames=field)
        wr.writerow({'Имя': name, 'Телефон': phone, 'Сообщение': message})
