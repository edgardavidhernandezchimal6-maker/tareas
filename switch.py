import tkinter as tk

# Función SWITCH
def programa_switch():
    opcion = int(entry_num.get())

    match opcion:
        case 1:
            resultado.config(text="Elegiste suma")
        case 2:
            resultado.config(text="Elegiste resta")
        case 3:
            resultado.config(text="Elegiste multiplicación")
        case _:
            resultado.config(text="Elegiste otro numero")

# Crear ventana
ventana = tk.Tk()
ventana.title("Programa SWITCH")
ventana.geometry("350x220")

# Etiqueta
label = tk.Label(ventana, text="Ingresa una opción:")
label.pack(pady=10)

# Entrada
entry_num = tk.Entry(ventana)
entry_num.pack(pady=5)

# Botón
boton = tk.Button(ventana, text="Verificar", command=programa_switch)
boton.pack(pady=10)

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
