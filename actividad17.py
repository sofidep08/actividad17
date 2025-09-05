import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("600x500")
ventana.configure(bg="light blue")

fondo=tk.Frame(ventana,width=400, height=430, bg="pink")
fondo.place(x=100, y=20)

etiqueta1 = tk.Label(ventana, text="Ingrese el primer numero",font=("Bookman Old Style",14,"bold"), fg="turquoise")
etiqueta1.pack(pady=(70,4))

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
    if numero2== 0 or numero1 == 0:
        etiqueta3.config(text="No se puede dividir entre 0",font=("Bookman Old Style",14,"bold"), fg="turquoise")
    else:
        etiqueta3.config(text=f"El resultado es: {numero1 / numero2}!", font=("Bookman Old Style", 14, "bold"), fg="turquoise")



def limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    etiqueta3.config(text="Resultado",font=("Bookman Old Style",14,"bold"), fg="turquoise")

boton_suma=tk.Button(ventana,text="SUMAR +",command=sumar,font=("Bookman Old Style",12,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
boton_suma.place(x=150,y=250)

boton_resta=tk.Button(ventana,text="RESTAR -",command=restar,font=("Bookman Old Style",12,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
boton_resta.place(x=350,y=250)

boton_multiplicar=tk.Button(ventana,text="MULTIPLICAR *",command=multiplicar,font=("Bookman Old Style",12,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
boton_multiplicar.place(x=150,y=300)

boton_dividir=tk.Button(ventana,text="DIVIDIR /",command=dividir,font=("Bookman Old Style",12,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
boton_dividir.place(x=350,y=300)

boton_limpiar = tk.Button(ventana, text="LIMPIAR", command=limpiar,font=("Bookman Old Style",12,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
boton_limpiar.place(x=150,y=350)

boton_salir = tk.Button(ventana, text="SALIR", command=ventana.quit,font=("Bookman Old Style",12,"bold"),fg="turquoise",activebackground="gray",relief="raised", bd=3)
boton_salir.place(x=350,y=350)

ventana.mainloop()