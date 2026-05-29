import tkinter as tk

# Función DICCIONARIOS
def programa_diccionario():
    alumno = {
        "nombre": "David",
        "edad": 15,
        "grupo": "2BMPG"
    }

    texto = (
        "Nombre: " + alumno["nombre"] + "\n"
        + "Edad: " + str(alumno["edad"]) + "\n"
        + "Grupo: " + alumno["grupo"]
    )

    resultado.config(text=texto)

# Crear ventana
ventana = tk.Tk()
ventana.title("Programa DICCIONARIO")
ventana.geometry("300x250")

# Botón
boton = tk.Button(ventana, text="Mostrar alumno", command=programa_diccionario)
boton.pack(pady=10)

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
