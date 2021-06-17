yann = {'equation-differentielle':[19,12,15], 'langage-c':[15,14,18], 'base-de-donne':[12,12,15]}

moyenne = {}
moyenne['equation-differentielle'] = (yann['equation-differentielle'][0] + yann['equation-differentielle'][1] + yann['equation-differentielle'][2])/3
moyenne['langage-c'] = (yann['langage-c'][0] + yann['langage-c'][1] + yann['langage-c'][2])/3
moyenne['base-de-donne'] = (yann['base-de-donne'][0] + yann['base-de-donne'][1] + yann['base-de-donne'][2])/3

moyenne_generale = (moyenne['equation-differentielle'] + moyenne['langage-c'] + moyenne['base-de-donne'])/3

print("Ma moyenne est : ", moyenne_generale)

## Exo E0

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("L : ",list(L))
L[0] = L[0]+11
L[1] = L[1]+11
L[2] = L[2]+11
L[3] = L[3]+11
L[4] = L[4]+11
L[5] = L[5]+11
L[6] = L[6]+11
L[7] = L[7]+11
L[8] = L[8]+11
L[9] = L[9]+11
print('L :', list(L))

L.append(22)
print("L :", list(L))

L.extend([23, 24])
print("L :", list(L))

L1 = L[0:13 :2]
L2 = L[1:13 :2]
print("L1 :", list(L1))
print("L2 :", list(L2))

del L[3]
print("L :", list(L))


## Exercice E1

d = {'nom':"Dupuis", "prenom":"Jacque", "age":30}
print("d : ", d)

d["prenom"] = "Jacques"
print("Apres modification du prenom")
print("d : ", d)

print("La liste des clés : ", list(d.keys()))
