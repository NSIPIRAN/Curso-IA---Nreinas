#Nathaly Sipiran Morillo curso IA-UNT

from tkinter import *
from PIL import ImageTk, Image
import nreinas

class tablero():
    color1 = "#DDB88C"
    color2 = "#A66D4F"

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
            mi_Label.grid(row=row, column=soloaux[row+ncas*0]-1) #row+ncas + [#aqui la solucion que queramos]

def inicia_programa():
    soluaux=[]
    col = list()
    num =0
    diag45 = list()
    diag135 = list()
    numero_de_casillas = 8
    solu=[0,0,0,0,0,0,0,0]
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
