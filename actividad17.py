import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x400")

etiqueta1 = tk.Label(ventana, text="Ingrese el primer numero",font=("Arial",10,"bold"), fg="violet")
etiqueta1.pack(pady=4)

entrada1= tk.Entry(ventana)
entrada1.pack(pady=4)

etiqueta2=tk.Label(ventana, text="Ingrese el segundo numero",font=("Arial",10,"bold"), fg="violet")
etiqueta2.pack(pady=4)

entrada2=tk.Entry(ventana)
entrada2.pack(pady=4)
#,font=(arial,20,"bold")

etiqueta3=tk.Label(ventana, text="Resultado",font=("Arial",10,"bold"), fg="pink")

def sumar():
    numero1=entrada1.get()
    numero2=entrada2.get()
    etiqueta3.config(text=f"El resultado es: {numero1} + {numero2}!",font=("Arial",10,"bold"), fg="pink")

def restar():
    numero1=entrada1.get()
    numero2=entrada2.get()
    etiqueta3.config(text=f"El resultado es: {numero1} - {numero2}!",font=("Arial",10,"bold"), fg="pink")

def multiplicar():
    numero1=entrada1.get()
    numero2=entrada2.get()
    etiqueta3.config(text=f"El resultado es: {numero1}*{numero2}!",font=("Arial",10,"bold"), fg="pink")

def dividir():
    numero1=entrada1.get()
    numero2=entrada2.get()
    if numero2=="0":
        etiqueta3.config(text="No se puede dividir entre 0",font=("Arial",10,"bold"), fg="pink")
    else:
        etiqueta3.config(text=f"El resultado es: {numero1}/{numero2}!", font=("Arial", 10, "bold"), fg="pink")



def limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    etiqueta3.config(text="Resultado",font=("Arial",10,"bold"), fg="pink")

boton_suma=tk.Button(ventana,text="SUMAR +",command=sumar)
boton_suma.pack(pady=4)

boton_resta=tk.Button(ventana,text="RESTAR -",command=restar)
boton_resta.pack(pady=4)

boton_multiplicar=tk.Button(ventana,text="MULTIPLICAR *",command=multiplicar)
boton_multiplicar.pack(pady=4)

boton_limpiar = tk.Button(ventana, text="LIMPIAR", command=limpiar)
boton_limpiar.pack(pady=4)

boton_salir = tk.Button(ventana, text="SALIR", command=ventana.quit)
boton_salir.pack(pady=4)

ventana.mainloop()