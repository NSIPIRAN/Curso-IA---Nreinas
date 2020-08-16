from tkinter import *
from PIL import ImageTk, Image

class tablero():
    color1 = "#DDB88C"  # es la casilla blanca
    color2 = "#A66D4F"  # es la casilla oscura
    # sombra_color1 = "#696969"
    # sombra_color2 = "#A9A9A9"
    def __init__(self, raiz, ncas, img):
        mainframe = Frame(raiz, bg="white")
        mainframe.pack()
        grid_frame = Frame(mainframe)
        for row in range(ncas):
            for column in range(ncas):
                if (row%2 == 0 and column%2==0) or (row%2 != 0 and column%2!=0):
                    label = Label(grid_frame, bg=self.color1, fg="white", width=8, height=4, padx=8, pady=8)
                else:
                    label = Label(grid_frame, bg=self.color2, fg="white", width=8, height=4, padx=8, pady=8)
                label.grid(row=row, column=column)
        grid_frame.pack()
        mi_Label = Label(grid_frame,image = img)
        mi_Label.grid(row=3, column=0)

def inicia_programa():
    numero_de_casillas = 4
    root = Tk()
    root.title("N-REINAS")
    path = "C:/Users/pukay/Documents/9 ciclo/IA/Nueva carpeta/nreinas/piezas/bq.png"
    img = ImageTk.PhotoImage(Image.open(path))
    gui = tablero(root, numero_de_casillas, img)
    root.mainloop()

if __name__ == "__main__":
    # primero la posición inicial del tablero
    
    inicia_programa()
