from tkinter import *
from PIL import ImageTk, Image
import nreinas

class tablero():
    color1 = "#DDB88C"  # es la casilla blanca
    color2 = "#A66D4F"  # es la casilla oscura
    #solu = [0,0,0,0]
    # sombra_color1 = "#696969"
    # sombra_color2 = "#A9A9A9"
    def __init__(self, raiz, ncas, img, soloaux):
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
        for row in range(0,ncas):

            mi_Label = Label(grid_frame,image = img)
            mi_Label.grid(row=row, column=soloaux[row*2]-1)





def inicia_programa():
    soluaux=[]
    col = list()
    num =0
    diag45 = list()
    diag135 = list()
    numero_de_casillas = 4
    solu=[0,0,0,0]
    root = Tk()
    root.title("N-REINAS")
    path = "C:/Users/pukay/Documents/9 ciclo/IA/Nueva carpeta/nreinas/piezas/bq.png"
    img = ImageTk.PhotoImage(Image.open(path))

    nreinas.nReinas(numero_de_casillas, 0, col, diag45, diag135, solu,num)
    soluaux = nreinas.soluciones
    gui = tablero(root, numero_de_casillas, img,soluaux)
    root.mainloop()

if __name__ == "__main__":


    inicia_programa()
