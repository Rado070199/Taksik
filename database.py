# database.py

from peewee import *
import datetime

# Tworzymy połączenie z SQLite
db = SqliteDatabase('taksik.db')

class Task(Model):
    status = BooleanField()
    title = CharField()
    description = TextField(null=True)
    priority = CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Medium')
    startDate = DateTimeField()
    endDate = DateTimeField()

    class Meta:
        database = db  # Określamy bazę danych

# Tworzymy tabelę
db.connect()
db.create_tables([Task], safe=True)

# Funkcja do pobierania wszystkich zadań
def get_all_tasks():
    return list(Task.select())

# Zamykamy połączenie
db.close()
