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

# Tworzymy tabelę, jeśli jeszcze nie istnieje
db.connect()
db.create_tables([Task], safe=True)  # safe=True zapobiegnie błędom, jeśli tabela już istnieje

# Dodajemy dane do bazy
Task.create(
    status=False,
    title="Dodać commit Taksik",
    description="Utworzenie aplikacji",
    priority="Medium",
    startDate=datetime.datetime.now(),
    endDate=datetime.datetime.now(),
)

Task.create(
    status=False,
    title="Dodać commit Taksik2",
    description="Utworzenie aplikacji2",
    priority="Low",
    startDate=datetime.datetime.now(),
    endDate=datetime.datetime.now(),
)

# Pobieranie wszystkich danych
tasks = Task.select()  # select() zwraca wszystkie rekordy
for task in tasks:
    print(f"Task: {task.title}, Priority: {task.priority}, Status: {task.status}")

# Zamykamy połączenie
db.close()
