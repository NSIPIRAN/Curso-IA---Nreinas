from tkinter import *
class tablero():
    color1 = "#DDB88C"  # es la casilla blanca
    color2 = "#A66D4F"  # es la casilla oscura
    # sombra_color1 = "#696969"
    # sombra_color2 = "#A9A9A9"
    def __init__(self, raiz, ncas):


        mainframe = Frame(raiz, bg="white")
        mainframe.pack()
        grid_frame = Frame(mainframe)
        for row in range(8):
            for column in range(8):
                if (row%2 == 0 and column%2==0) or (row%2 != 0 and column%2!=0):
                    label = Label(grid_frame, bg=self.color1, fg="white", padx=8, pady=8)
                else:
                    label = Label(grid_frame, bg=self.color2, fg="white", padx=8, pady=8)


                label.grid(row=row, column=column)
        grid_frame.pack()

def inicia_programa():
    numero_de_casillas = 8
    root = Tk()
    root.title("N-REINAS")
    gui = tablero(root, numero_de_casillas)

    root.mainloop()


if __name__ == "__main__":
    # primero la posición inicial del tablero

    inicia_programa()
