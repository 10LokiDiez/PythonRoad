import datetime

#conviete la fecha en fecha
date =  datetime.date(2026,9,20)
print(date)

#Me arroja el dia de hoy
today = datetime.date.today()
print(today)

#convierte este tiempo en fecha
time = datetime.time(12,30,2)
print(time)

#Me da fecha y hora
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %d-%m-%Y")
print(now)

new_date = datetime.datetime(2030,1,2,12,30,1)
current_datetime = datetime.datetime.now()

if new_date < current_datetime:
    print("Te pasaste Pedrito")
else:
    print("No te pasaste Pedrito")