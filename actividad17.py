import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("600x600")
ventana.configure(bg="light blue")

etiqueta1 = tk.Label(ventana, text="Ingrese el primer numero",font=("Bookman Old Style",14,"bold"), fg="turquoise")
etiqueta1.pack(pady=4)

entrada1= tk.Entry(ventana)
entrada1.pack(pady=4)

etiqueta2=tk.Label(ventana, text="Ingrese el segundo numero",font=("Bookman Old Style",14,"bold"), fg="turquoise")
etiqueta2.pack(pady=4)

entrada2=tk.Entry(ventana)
entrada2.pack(pady=4)
#,font=(arial,20,"bold")

etiqueta3=tk.Label(ventana, text="Resultado",font=("Bookman Old Style",14,"bold"), fg="turquoise")
etiqueta3.pack(pady=4)

def sumar():
    numero1=float(entrada1.get())
    numero2=float(entrada2.get())
    etiqueta3.config(text=f"El resultado es: {numero1 + numero2}!",font=("Bookman Old Style",14,"bold"), fg="turquoise")

def restar():
    numero1= float (entrada1.get())
    numero2=float(entrada2.get())
    etiqueta3.config(text=f"El resultado es: {numero1 - numero2}!",font=("Bookman Old Style",14,"bold"), fg="turquoise")

def multiplicar():
    numero1=float(entrada1.get())
    numero2=float(entrada2.get())
    etiqueta3.config(text=f"El resultado es: {numero1 * numero2}!",font=("Bookman Old Style",14,"bold"), fg="turquoise")

def dividir():
    numero1=float(entrada1.get())
    numero2=float(entrada2.get())
    if numero2== 0:
        etiqueta3.config(text="No se puede dividir entre 0",font=("Bookman Old Style",14,"bold"), fg="turquoise")
    else:
        etiqueta3.config(text=f"El resultado es: {numero1 / numero2}!", font=("Bookman Old Style", 14, "bold"), fg="turquoise")



def limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    etiqueta3.config(text="Resultado",font=("Bookman Old Style",14,"bold"), fg="turquoise")

boton_suma=tk.Button(ventana,text="SUMAR +",command=sumar,font=("Bookman Old Style",12,"bold"),fg="turquoise",activebackground="pink")
boton_suma.pack(pady=4)

boton_resta=tk.Button(ventana,text="RESTAR -",command=restar,font=("Bookman Old Style",12,"bold"),fg="turquoise",activebackground="pink")
boton_resta.pack(pady=4)

boton_multiplicar=tk.Button(ventana,text="MULTIPLICAR *",command=multiplicar,font=("Bookman Old Style",12,"bold"),fg="turquoise",activebackground="pink")
boton_multiplicar.pack(pady=4)

boton_dividir=tk.Button(ventana,text="DIVIDIR *",command=multiplicar,font=("Bookman Old Style",12,"bold"),fg="turquoise",activebackground="pink")
boton_dividir.pack(pady=4)

boton_limpiar = tk.Button(ventana, text="LIMPIAR", command=limpiar,font=("Bookman Old Style",12,"bold"),fg="turquoise",activebackground="pink")
boton_limpiar.pack(pady=4)

boton_salir = tk.Button(ventana, text="SALIR", command=ventana.quit,font=("Bookman Old Style",12,"bold"),fg="turquoise",activebackground="pink")
boton_salir.pack(pady=4)

ventana.mainloop()