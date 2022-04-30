import pywhatkit

numCel = input("Digite su numero de celular: ")
mensaje = input("Digite el mensaje: ")
hora = int(input("Digite la hora: "))
minuto = int(input("Digite el minuto: "))
tiempo_de_espera = int(input("Digite el tiempo de espera: "))
segundos_de_cierre = int(input("Digite los segundos de cierre: "))

cerrar = input("Desea cerrar la pestaña de wspp?: (s/n)")
if cerrar == "s":
    pywhatkit.sendwhatmsg(numCel, mensaje, hora, minuto, tiempo_de_espera,True, segundos_de_cierre)
else:
    pywhatkit.sendwhatmsg(numCel, mensaje, hora, minuto, tiempo_de_espera,False, segundos_de_cierre)