import tkinter as tk

# CLASE ALUMNO
class Alumno:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    def mostrar(self):
        return (
            "Nombre: " + self.nombre + "\n"
            + "Edad: " + str(self.edad) + "\n"
            + "Promedio: " + str(self.promedio)
        )

# Función
def programa_clase():
    al1 = Alumno("DAVID", 15, 9.5)
    resultado.config(text=al1.mostrar())

# Crear ventana
ventana = tk.Tk()
ventana.title("Programa CLASE ALUMNO")
ventana.geometry("300x250")

# Botón
boton = tk.Button(ventana, text="Mostrar alumno", command=programa_clase)
boton.pack(pady=10)

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
