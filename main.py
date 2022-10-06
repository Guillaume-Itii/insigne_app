from PIL import Image

with open('../joueur.csv') as f:
    temp = f.readlines()

joueur_list_string = []
for s in temp:
    s = s.replace('\n', '')
    joueur_list_string.append(s)

# Recup les noms de colonne
column = joueur_list_string.pop(0).split(';')
print(column)
print(joueur_list_string)

joueur_list = []
for s in joueur_list_string:
    temp = {}
    for i in range(len(column)):
        temp[column[i]] = s.split(';')[i]
    joueur_list.append(temp)
# la joueur_list contient des dictionnaire avec les colonnes du CSV en clé et les valeurs en valeurs
print(joueur_list)

for i in range(len(joueur_list)):
    for j in column:
        if j != "player":
            if joueur_list[i][j] != '0':
                # On parcours notre joueur liste en remplaçant les valeurs numérique par l'image du ruban associer
                # (0 = pas de ruban pur l'op)
                # On lit l'image en utilisant la clée comme nom d'image puis nombre de fois participé a la campagne
                # exemple "Kit" à participer 2 fois à 2022_Libe_Panthera
                # alors le tuple "2022_Libe_Panthera : 2" devien l'image "2022_Libe_Panthera_2.png"
                joueur_list[i][j] = Image.open('../downsized/' + j + '_' + joueur_list[i][j] + '.png')

img_joueur_list = {}
for i in range(len(joueur_list)):
    # on crée un dictionnaire avec tout les joueurs et on leur donne l'image 128x128 vide
    img_joueur_list[joueur_list[i]["player"]] = Image.open('../Standard.png')

for i in img_joueur_list:
    for j in range(len(joueur_list)):
        if joueur_list[j]["player"] == i:
            x = 18
            y = 0
            for k in column:
                if k != "player":
                    if joueur_list[j][k] != '0':
                        # On viens placer dans notre image standard les differentes image de ruban qu'a le joueur
                        img_joueur_list[i].paste(joueur_list[j][k], (x, y))
                        x += 18
                        if x >= 126:
                            x = 0
                            y += 5

for i in img_joueur_list:
    img_joueur_list[i].save('../icon/' + i + '.png')
