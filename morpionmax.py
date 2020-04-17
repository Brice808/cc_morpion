morpion = [[''for x in range (3)]for y in range (3)]
joueur1 = 'x'
joueur2 = 'o'
tour = 0
j1 = 0
j2 = 0
morpion.insert ([0][0])

print (morpion)

while tour !=4:
    morpion = [[''for x in range (3)]for y in range (3)]
    print ('saisissez votre choix x et y de coordonées pour le tour')
    position1 = input ()
    morpion.insert(position1,joueur1)
    print('votre choix' + position1)
    j1 += 1
    print (morpion)
    print ('saisissez votre choix x et y de coordonées pour le tour')
    position2 = input ()
    print('votre choix' + position2)
    morpion.insert(position2,joueur2)
    j2  += 1
    tour += 1
    print (morpion)
