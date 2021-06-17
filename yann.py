yann = {'equation-differentielle':[19,12,15], 'langage-c':[15,14,18], 'base-de-donne':[12,12,15]}

moyenne = {}
moyenne['equation-differentielle'] = (yann['equation-differentielle'][0] + yann['equation-differentielle'][1] + yann['equation-differentielle'][2])/3
moyenne['langage-c'] = (yann['langage-c'][0] + yann['langage-c'][1] + yann['langage-c'][2])/3
moyenne['base-de-donne'] = (yann['base-de-donne'][0] + yann['base-de-donne'][1] + yann['base-de-donne'][2])/3

moyenne_generale = (moyenne['equation-differentielle'] + moyenne['langage-c'] + moyenne['base-de-donne'])/3

print("Ma moyenne est : ", moyenne_generale)
