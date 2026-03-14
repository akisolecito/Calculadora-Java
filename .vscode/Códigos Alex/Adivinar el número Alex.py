#Importar librerias 
import tkinter as tk
from random import randint
#Empezar a definir las ventanas
ventana = tk.Tk()
ventana.title("Adivinar el Número")
# Entry para el rango mínimo y máximo
label_min = tk.Label(ventana, text="Rango Mínimo 1-100")
label_min.pack()
entrada_min = tk.Entry(ventana)
entrada_min.pack()
label_max = tk.Label(ventana, text="Rango Máximo 1-100")
label_max.pack()
entrada_max = tk.Entry(ventana)
entrada_max.pack()
# Boton para establecer el rango, global significa que es una variable que se puede modificar dentro de esta función
def establecer_rango():
    global numero_random
    minimo = int(entrada_min.get())
    maximo = int(entrada_max.get())
    numero_random = randint(minimo, maximo)
#Este botón llama a la funcion establecer rango al presionarlo
boton_establecer_rango = tk.Button(ventana, text="Establecer Rango", command=establecer_rango)
boton_establecer_rango.pack()
intentos = 0
label_rango = tk.Label(ventana, text = "Adivina el número, tienes 10 intentos")
label_rango.pack()
entrada_usuario = tk.Entry(ventana)
entrada_usuario.pack()
#Esta linea crea un label vacio para mostrar pistas según la condición que se cumpla
label_pistas = tk.Label(ventana, text="")
label_pistas.pack()
#Definir mis condicionales
def enviar_suposicion ():
    global intentos
    intentos += 1
    suposicion = int(entrada_usuario.get()) 
    if intentos > 10:
        label_pistas.config(text="Perdiste")
    elif suposicion == numero_random +1:
        label_pistas.config(text="Casi, te pasaste un poco")
    elif suposicion == numero_random -1:
        label_pistas.config(text="Casi, te falta un poco")
    elif suposicion < numero_random:
        label_pistas.config(text="Demasiado bajo")
    elif suposicion > 100 :
        label_pistas.config(text="No puede ser un número mayor a 100")
    elif suposicion > numero_random:
        label_pistas.config(text="Demasiado alto")
    elif intentos < 7:
        label_pistas.config(text="Que rápido, muy bien")
        boton_enviar.config(state="disabled")
    else:
        label_pistas.config(text=f"¡Correcto! Has adivinado el número en {intentos} intentos ", fg ="green")     
        boton_enviar.config(state="disabled")
boton_enviar = tk.Button(ventana, text="Enviar Suposición", command=enviar_suposicion)
boton_enviar.pack()
#Esta parte es para reiniciar el juego
def reiniciar_juego():
    global numero_random, intentos
    numero_random = randint (1, 100)
    intentos = 0
    label_pistas.config(text="")
    entrada_usuario.delete(0, tk.END)
    boton_enviar.config(state="normal")
boton_reiniciar = tk.Button(ventana, text="Reiniciar Juego", command=reiniciar_juego)
boton_reiniciar.pack()
#Iniciar el bucle/mostrar la pantalla
ventana.mainloop()
