import tkinter as tk
import automata


##
# Interfaz del buscador
def show(root):
    farm_validador = tk.Frame(root)
    farm_validador.pack()


    # Botón para volver al formulario
    boton_volver = tk.Button(farm_validador, text="Volver al Formulario", command=lambda: volver_al_formulario(
        root, farm_validador))
    boton_volver.grid(row=3, columnspan=2)


# Función para volver al formulario
def volver_al_formulario(root, farm_validador):
    farm_validador.pack_forget()
    automata.show(root)