import threading
import time

def walk_dog(first):
    time.sleep(8)
    print("You finish walking the {first}")
    
    
def take_out_trash():
    time.sleep(2)
    print("You take out the trash")
    
def get_mail():
    time.sleep(4)
    print("You get the mail")
    
#Hay que declarar que args es una tupla por eso la coma
tarea1 = threading.Thread(target=walk_dog, args=("Scooby",))
tarea1.start()

tarea2 =threading.Thread(target=take_out_trash)
tarea2.start()

tarea3 = threading.Thread(target=get_mail)
tarea3.start()

#Sirve para esperar a las tareas a que terminen
tarea1.join()
tarea2.join()
tarea3.join()

print("LAS TAREAS ESTAN LISTAS")