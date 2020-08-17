import verificacion

soluciones=[]

def nReinas(nr, k, col, diag45, diag135, sol, num):

    global soluciones
    if k == nr:

        soluciones+=sol
        print(sol)

    else:
        for j in range(1,nr+1):
            if (not verificacion.verificar.contiene(col, j) and
                not verificacion.verificar.contiene(diag45, j-k) and
                not verificacion.verificar.contiene(diag135, j+k)):
                sol[k]=j
                col.append(j)
                diag45.append(j - k)
                diag135.append(j + k)
                nReinas(nr, k + 1, col, diag45, diag135, sol,num)
                col.pop()
                diag45.pop()
                diag135.pop()
