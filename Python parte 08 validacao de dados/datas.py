from datetime import datetime, timedelta

print(datetime.today())
print(datetime.today().strftime("%d/%m/%Y"))
print(datetime.today().strftime("%d/%m/%Y %H:%M"))
print(datetime.today().strftime("%Y"))
print(datetime.today().strftime("%y"))
print(datetime.today().strftime("%d"))
print(datetime.today().strftime("%m"))

hoje = datetime.today()
amanha = datetime.today() + timedelta(days=1, hours=20)
print(hoje - amanha)

print(timedelta(days=15, minutes=20,seconds=30))