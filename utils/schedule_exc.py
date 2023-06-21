from . import db
from datetime import datetime


# Inserting note in Database
def insert_schedule(info):
    asd = db.DB()
    date = datetime.now().strftime("%d.%m.%Y-%H:%M")
    num = asd.find(table="note", many = True)
    id = 1
    if num:
        id += len(num)
    asd.insert(table="note", data = (id, info.sched_from, info.for_whom, info.name, info.description, date, info.deadline))

def get_list():
    asd = db.DB()
    data = asd.find(table='note', many=True)
    logins = []
    if data:
        for i in data:
            it = asd.find(columns = 'login', table = 'users', where=f"tid = '{i[1]}'", many=False)
            logins.append(it[0])
    else:
        return False
    return data, logins

def delete_schedule(id):
    asd = db.DB()
    data = asd.find(table='note', many=False, where=f'id={id}')
    if data:
        asd.delete(table='note', where=f'id={id}')
        return True
    else:
        return False

def check_for_real(id):
    asd = db.DB()
    data = asd.find(table='note', many=False, where=f'id={id}')
    if data:
        return True
    else:
        return False

def updating(data, columns):
    print(columns, len(columns))
    asd = db.DB()
    for i in range(len(columns)):
        asd.update(table='note', column=columns[i], where=f'id={data[0]}', new_value=f'{data[i+1]}')
