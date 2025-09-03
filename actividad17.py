import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x400")

etiqueta1 = tk.Label(ventana, text="Ingrese el primer numero",font=("Arial",20,"bold"), fg="red")
etiqueta1.pack(pady=4)
entrada1= tk.Entry(ventana)

etiqueta2=tk.Label(ventana, text="Ingrese el segundo numero")
etiqueta2.pack(pady=4)
entrada2=tk.Entry(ventana)
#,font=(arial,20,"bold")

etiqueta3=tk.Label(ventana, text="Resultado")

def sumar():
    numero1=entrada1.get()
    numero2=entrada2.get()
    etiqueta3.config(text=f"El resultado es: {numero1} + {numero2}!")

def restar():
    numero1=entrada1.get()
    numero2=entrada2.get()
    etiqueta3.config(text=f"El resultado es: {numero1} - {numero2}!")

def multiplicar():
    numero1=entrada1.get()
    numero2=entrada2.get()
    etiqueta3.config(text=f"El resultado es: {numero1}*{numero2}!")

def limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    etiqueta3.config(text="Resultado")

boton_suma=tk.Button(ventana,text="+",command=sumar)
boton_resta=tk.Button(ventana,text="-",command=sumar)
boton_suma=tk.Button(ventana,text="+",command=sumar)