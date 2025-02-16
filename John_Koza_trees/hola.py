import tkinter as tk
import random
def pintar_bloques(lista):
    """
    Pinta bloques negros y blancos en una ventana de Tkinter.
    - 0: Bloque blanco
    - 1: Bloque negro
    """
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Bloques 1xN")
    
    # Tamaño de cada bloque
    ancho_bloque = 5
    alto_bloque = 5
    
    # Crear un lienzo (Canvas) para dibujar los bloques
    lienzo = tk.Canvas(ventana, width=len(lista) * ancho_bloque, height=alto_bloque)
    lienzo.pack()
    
    # Dibujar los bloques
    for i, valor in enumerate(lista):
        x1 = i * ancho_bloque
        y1 = 0
        x2 = x1 + ancho_bloque
        y2 = alto_bloque
        
        # Elegir el color según el valor
        color = "black" if valor == 1 else "white"
        
        # Dibujar el rectángulo
        lienzo.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
    
    # Iniciar el bucle principal de Tkinter
    ventana.mainloop()

# Ejemplo de uso
lista = [random.choice([0,1]) for _ in range(256)]
pintar_bloques(lista)