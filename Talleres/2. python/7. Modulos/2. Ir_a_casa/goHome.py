from datetime import datetime

now = datetime.now().strftime('%H:%M:%S')
hora7 = "19:00:00"
t1 = datetime.strptime(now, '%H:%M:%S')
t2 = datetime.strptime(hora7, '%H:%M:%S')

if(t1 > t2):
    print("Es hora de ir a casa")
else:
    diferencia = t2-t1
    print("El tiempo que falta para ir a casa son ", diferencia, " minutos")