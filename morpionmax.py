a = [[''for x in range (3)]for y in range (3)]
joueur1 = 'x'
joueur2 = 'o'
tour = 0
j1 = 0
j2 = 0

print (a)

while tour !=4:
    a = [[''for x in range (3)]for y in range (3)]
    print ('saisissez votre choix x et y de coordonées pour le tour')
    a = input ()
    print('votre choix' + a)
    j1 += 1
    print (a)
    print ('saisissez votre choix x et y de coordonées pour le tour')
    a = input ()
    print('votre choix' + a)
    j2  += 1
    tour += 1
    print (a)
