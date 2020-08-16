from tkinter import *



class tablero():


    color1 = "#DDB88C"  # es la casilla blanca
    color2 = "#A66D4F"  # es la casilla oscura
    sombra_color1 = "#696969"
    sombra_color2 = "#A9A9A9"
    color_casillas_tablero = {}
    dim_casilla = 48  # 64



    def __init__(self, raiz,ncas):
        self.filas = ncas
        self.columnas = ncas
        canvas_width = self.columnas * self.dim_casilla
        canvas_height = self.filas * self.dim_casilla
        panes = PanedWindow(raiz, bg='grey', width=canvas_width)
        panes.pack()

        self.canvas = Canvas(panes, width=canvas_width, height=canvas_height)
        self.canvas.pack(padx=8, pady=8)
        self.dibuja_tablero(ncas)


        panes.add(self.canvas)


    def dibuja_tablero(self,num):
        self.canvas.delete("area")
        color = self.color1
        for r in range(self.filas):
            color = self.color1 if color == self.color2 else self.color2
            num_casilla = str(r + 1)
            for c in range(self.columnas):
                letra_casilla = chr(97 + c)
                x1 = (c * self.dim_casilla)
                y1 = (((num-1) - r) * self.dim_casilla)
                x2 = x1 + self.dim_casilla
                y2 = y1 + self.dim_casilla
                # x1 y y1 es el vertice superior izquierdo
                # x2 e y2 es el vertice inferior derecho
                id_casilla = str(x1) + '-' + str(y1) + '-' + str(x2) + '-' + str(y2)

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags=(id_casilla, "area"))
                color = self.color1 if color == self.color2 else self.color2
                color_sombreado = None
                if color == self.color1:
                    color_sombreado = self.sombra_color1
                else:
                    color_sombreado = self.sombra_color2
                estruct_casilla = {'color_sin_sombra': color, 'color_con_sombra': color_sombreado,
                                   'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2}
                self.color_casillas_tablero[letra_casilla + num_casilla] = estruct_casilla
def inicia_programa():
    numero_de_casillas=8
    root = Tk()
    root.title("N-REINAS")
    gui = tablero(root, numero_de_casillas)


    root.mainloop()


if __name__ == "__main__":
    #primero la posición inicial del tablero

    inicia_programa()
