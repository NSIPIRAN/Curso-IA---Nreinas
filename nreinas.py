import verificacion


def nReinas(nr, k, col, diag45, diag135, sol,num):

    if k == nr:
        print(sol)
        print
        # soluciones[num]=sol
        # interfazlab.tablero.setSolu(sol)
    else:
        for j in range(1,nr+1):
            if ( not verificacion.verificar.contiene(col, j) and not verificacion.verificar.contiene(diag45, j-k) and not verificacion.verificar.contiene(diag135, j+k) ):

                sol[k]=j
                col.append(j)
                diag45.append(j - k)
                diag135.append(j + k)

                nReinas(nr, k + 1, col, diag45, diag135, sol,num)

                col.pop()
                diag45.pop()
                diag135.pop()



# solu = [0,0,0,0]
# col = list()
# diag45 = list()
# diag135 = list()
# numero_de_casillas = 4
# nReinas(numero_de_casillas, 0, col, diag45, diag135,solu)