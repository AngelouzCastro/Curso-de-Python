c=[]
mensaje=[7,7,7,7,6,6,6,9,9,9,0,8,8,8,4,4,4,3,3,5,6,6,6,None]
mensajee=[2,2,2,2,3,3,3,2,2,None]
suma = 0
i = 0
j = 0
pos = 0
palabra = ""
lon = len(mensaje)


for i in range(len(mensaje)):
    if mensaje[i] == None:
        break
    if mensaje[i] == mensaje[i+1]:
        suma = suma + 1
    else:
        if suma == 0:
            pos = 1
        else:
            pos = suma + 1
        
            
       
        c.append(pos)
        while suma != 0:
            if mensaje[i] == 2:
                while pos != 0:
                    if pos <= 3:
                        if pos == 1:
                            palabra = palabra + 'a'
                        if pos == 2:
                            palabra = palabra + 'b'
                        if pos == 3:
                            palabra = palabra + 'c'
                        pos = 0
                    else:
                        pos = pos - 1
            elif mensaje[i] == 3:
                while pos != 0:
                    if pos <= 3:
                        if pos == 1:
                            palabra = palabra + 'd'
                        if pos == 2:
                            palabra = palabra + 'e'
                        if pos == 3:
                            palabra = palabra + 'f'
                        pos = 0
                    else:
                        pos = pos - 1
            elif mensaje[i] == 4:
                while pos != 0:
                    if pos <= 3:
                        if pos == 1:
                            palabra = palabra + 'g'
                        if pos == 2:
                            palabra = palabra + 'h'
                        if pos == 3:
                            palabra = palabra + 'i'
                        pos = 0
                    else:
                        pos = pos - 1
            elif mensaje[i] == 5:
                while pos != 0:
                    if pos <= 3:
                        if pos == 1:
                            palabra = palabra + 'j'
                        if pos == 2:
                            palabra = palabra + 'k'
                        if pos == 3:
                            palabra = palabra + 'l'
                        pos = 0
                    else:
                        pos = pos - 1
            elif mensaje[i] == 6:
                while pos != 0:
                    if pos <= 3:
                        if pos == 1:
                            palabra = palabra + 'm'
                        if pos == 2:
                            palabra = palabra + 'n'
                        if pos == 3:
                            palabra = palabra + 'o'
                        pos = 0
                    else:
                        pos = pos - 1
                        
            elif mensaje[i] == 7:
                while pos != 0:
                    if pos <= 4:
                        if pos == 1:
                            palabra = palabra + 'p'
                        if pos == 2:
                            palabra = palabra + 'q'
                        if pos == 3:
                            palabra = palabra + 'r'
                        if pos == 4:
                            palabra = palabra + 's'
                        pos = 0
                    else:
                        pos = pos - 1
            elif mensaje[i] == 8:
                while pos != 0:
                    if pos <= 3:
                        if pos == 1:
                            palabra = palabra + 't'
                        if pos == 2:
                            palabra = palabra + 'u'
                        if pos == 3:
                            palabra = palabra + 'v'
                        pos = 0
                    else:
                        pos = pos - 1
            elif mensaje[i] == 9:
                while pos != 0:
                    if pos <= 4:
                        if pos == 1:
                            palabra = palabra + 'w'
                        if pos == 2:
                            palabra = palabra + 'x'
                        if pos == 3:
                            palabra = palabra + 'y'
                        if pos == 4:
                            palabra = palabra + 'z'
                        pos = 0
                    else:
                        pos = pos - 1
            elif mensaje[i] == 0:
                palabra = palabra + ' '
                pos = 0
            else:
                 palabra = palabra + ' '
            suma = 0
            


print(palabra)
                    
