from tinydb import TinyDB, Query


db = TinyDB('db.json')

Form = Query()

data = [
    {'name': 'CustomerForm', 'fields': {
        'info': 'text',
        'address': 'email',
        'organization': 'email',
        'cooperation': 'phone'
    }, },
    {'name': 'ClientForm', 'fields': {
        'info': 'text',
        'address': 'email',
        'organization': 'phone',
        'cooperation': 'date'
    }, },
    {'name': 'ManagerForm', 'fields': {
        'info': 'date',
        'address': 'text',
        'organization': 'text',
        'cooperation': 'phone'
    }, },
    {'name': 'StaffForm', 'fields': {
        'info': 'text',
        'address': 'email',
        'organization': 'text',
        'cooperation': 'phone'
    }, },
    {'name': 'MegaForm', 'fields': {
        'info': 'text',
        'address': 'email',
        'organization': 'phone',
        'cooperation': 'text'
    }, },
]

# for i in data:
#     db.insert(i)

for i in db:
    i = dict(i)
    print(type(i))
    print(i)

