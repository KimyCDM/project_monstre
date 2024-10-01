"""
tp3
Par Yul Kim
Groupe:405
on doit tuer le monstre
"""
import random
import time
niveau_vie = 20
main_game = True
game = True
difficulty = 1
numero_adversaire = 1
numero_combat = 0
numero_defait = 0
numero_victoire = 0
victore_c = 0
level = 6
while main_game:
    if numero_victoire == 3:
        print('\nBoss!')
        difficulty+2
    if difficulty > 7:
        print('Merci d avoir jouer.')
        exit()
    else:
        force_adversaire = random.randint(1, difficulty) + random.randint(1, difficulty)
        game = True
        while game:
            if niveau_vie <= 0:
                print('Vous etes mort...')
                exit()
            else:
                print(f'Adversaire:{numero_adversaire}\nForce de l’adversaire:{force_adversaire}')
                print(f'Niveau de vie de l’usager:{niveau_vie} \nCombat:{numero_combat}')
                print(f'Victoire:{numero_victoire} Defait:{numero_defait} Victoire consecutive:{victore_c}')
                print(f'Lv:{level-5}')
                choix = int(input('\nQue voulez-vous faire ? \n  1- Combattre cet adversaire\n '
                                  ' 2- Contourner cet adversaire et aller ouvrir une autre porte\n'
                                  '  3- Afficher les règles du jeu\n  4- Quitter la partie\n   :'))
                if choix == 1:
                    force_user = random.randint(1, level) + random.randint(1, level)
                    print(f'Votre degat:{force_user}| Degat ennemi:{force_adversaire}\n------------------------')
                    if force_user > force_adversaire:
                        niveau_vie = niveau_vie + force_adversaire
                        numero_combat = numero_combat+1
                        numero_victoire = numero_victoire+1
                        numero_adversaire = numero_adversaire + 1
                        difficulty = difficulty + 1
                        victore_c = victore_c+1
                        print('Victoire\n')
                        print(f'Niveau de vie {niveau_vie - force_adversaire}->{niveau_vie}')
                        level = level + 1
                        time.sleep(2)
                        game = False
                    elif force_user <= force_adversaire:
                        niveau_vie = niveau_vie - force_adversaire
                        numero_combat = numero_combat + 1
                        numero_defait = numero_defait + 1
                        victore_c = 0
                        print('Defait')
                        time.sleep(2)
                        game = False
                elif choix == 2:
                    niveau_vie = niveau_vie-1
                    print('Vous avez contourner l adversaire et ouvert une autre porte.'
                          f'\nNiveau de vie {niveau_vie+1}->{niveau_vie}\n')
                    time.sleep(2)
                elif choix == 3:
                    print('Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure\n'
                          'à la force de l’adversaire.Dans ce cas, le niveau de vie de l’usager est \n'
                          'augmenté de la force de l’adversaire.Une défaite a lieu lorsque la valeur \n'
                          'du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire\n'
                          '.Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n'
                          'La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n'
                          'L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement,\n'
                          'il y a une pénalité de 1 point de vie.\n')
                    time.sleep(10)
                elif choix == 4:
                    exit()
