import tkinter as tk
import automata

##
# Interfaz del buscador
def show(root, estado_inicial, conjunto_estados_finales, transiciones):
    farm_validador = tk.Frame(root)
    farm_validador.pack()

    tk.Label(farm_validador, text="Ingrese palabra:").grid(row=0, column=0)
    palabra = tk.Entry(farm_validador)
    palabra.grid(row=0, column=1)

    resultado_label = tk.Label(farm_validador, text="")
    resultado_label.grid(row=2, columnspan=2)

    boton_buscar = tk.Button(farm_validador, text="verificar", command=lambda: revisar_palabra(
        resultado_label,transiciones, palabra.get(), estado_inicial, conjunto_estados_finales))
    boton_buscar.grid(row=1, columnspan=2)

    # Botón para volver al formulario
    boton_volver = tk.Button(farm_validador, text="Nuevo Automata",
                              command=lambda: volver_al_formulario(root, farm_validador))
    boton_volver.grid(row=3, columnspan=2)


# Función para volver al formulario
def volver_al_formulario(root, farm_validador):
    print("Presiono Volver al automata")
    farm_validador.pack_forget()
    automata.reset_variables()  # Resetea entry_fields
    automata.show(root)
    ##resert all variables
    
    # Función para buscar el apellido en la lista

def revisar_palabra(resultado_label,transiciones, palabra, estado_inicial, conjunto_estados_finales):
    resultado = evaluar_palabra(transiciones, palabra, estado_inicial, conjunto_estados_finales)
    if resultado:
        resultado_label.config(text=f"La palabra: {palabra} es aceptada por el automata!")
    else:
        resultado_label.config(text=f"La palabra: {palabra} NO! es aceptada por el automata!")

def evaluar_palabra(transiciones, palabra, estado_inicial, conjunto_estados_finals):
    estado_actual = estado_inicial
    
    for simbolo in palabra:
        transicion = (estado_actual, simbolo)
        if transicion not in transiciones:
            return False  # No hay transición definida para el estado actual y el símbolo
        estado_actual = transiciones[transicion]
    return estado_actual in conjunto_estados_finals