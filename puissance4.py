# -*- coding: cp1252 -*-
from Tkinter import *
import tkMessageBox

def jouer(num_j,num_col,tab_jeu):
    val_set = False
    for i,e in enumerate(tab_jeu[num_col]):
        if e == 0 and val_set == False:
            tab_jeu[num_col][i] = num_j
            val_set = True
    return tab_jeu

def affiche_jeu(tableau_de_jeu):
    res = '   0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9'
    tab = list(reversed(inverserLigneCol(tableau_de_jeu)))
    for ligne in tab:
        res += '\n _________________________________________ \n |'
        for e in ligne:
            if e == 0:
                e = ' '
            elif e == 1:
                e = 'O'
            else:
                e = 'X'
            res += ' %s |'%(e)
    res += '\n _________________________________________ \n   0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9'

    win = aGagne(tableau_de_jeu)
    
    if match_nul(tableau_de_jeu):
        res += '\n Match nul'
    elif win != False:
        res += '\n Le joueur %s a gagne!'%(win)

    print(res)

def match_nul(tableau_de_jeu):
    for ligne in tableau_de_jeu:
        for e in ligne:
            if e == 0:
                return False
    return True
    
def aGagne(tableau_de_jeu):
    for i,ligne in enumerate(tableau_de_jeu):
        for j,e in enumerate(ligne):
            if e != 0:
                if(j+3<len(ligne)):
                    if ligne[j+1] == e and ligne[j+2] == e and ligne[j+3] == e:
                        return e
                if(i+3<len(tableau_de_jeu)):
                    if tableau_de_jeu[i+1][j] == e and tableau_de_jeu[i+2][j] == e and tableau_de_jeu[i+3][j] == e:
                        return e
                if(j+3<len(ligne) and i+3<len(tableau_de_jeu)):
                    if tableau_de_jeu[i+1][j+1] == e and tableau_de_jeu[i+2][j+2] == e and tableau_de_jeu[i+3][j+3] == e:
                        return e
                if(j-3>=0 and i+3<len(tableau_de_jeu)):
                    if tableau_de_jeu[i+1][j-1] == e and tableau_de_jeu[i+2][j-2] == e and tableau_de_jeu[i+3][j-3] == e:
                        return e
    return False

def fini(tableau_de_jeu):
    if match_nul(tableau_de_jeu) == True and aGagne != False:
        return True
    else:
        if aGagne(tableau_de_jeu) != False:
            return True
        else:
            return False

def p4():

    tableau_de_jeu = [[0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0]]
    
    j = 1
    while fini(tableau_de_jeu) == False:
        col = input('Tour du joueur %s : Veuillez indiquer une colonne (0-9) \n'%(j))
        affiche_jeu2(jouer(j,col,tableau_de_jeu))
        if j == 1:
            j = 2
        else:
            j = 1
    print 'Partie terminee'
    again = input('Voulez-vous rejouer? (1 : Oui/0 : Non)\n')
    if again == 1:
        p4()
    else:
        print '***Au revoir***'

def affiche_jeu2(tableau_de_jeu):
    global tab_jeu, s1, s2
    tab = tableau_de_jeu
    for i,ligne in enumerate(tab):
        for j,e in enumerate(list(reversed(ligne))):
            #canvas.create_line(i*90,j*90,i*90+90,j*90)
            #canvas.create_line(i*90,j*90,i*90,j*90+90)
            if e == 1:
                #canvas.create_oval(i*90,j*90,i*90+90,j*90+90,width=4,fill='red',outline='black')
                canvas.create_image(i*90+45,j*90+45,image=img_p1)
            elif e == 2:
                #canvas.create_oval(i*90,j*90,i*90+90,j*90+90,width=4,fill='yellow',outline='black')
                canvas.create_image(i*90+45,j*90+45,image=img_p2)
            canvas.create_image(i*90+45,j*90+45,image=img)

    win = aGagne(tableau_de_jeu)

    if win != False:
        tkMessageBox.showwarning('fin de partie','Le joueur %s a gagné!'%(win))
        tab_jeu = [[0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0]]
        canvas.delete("all")
        affiche_jeu2(tab_jeu)

        if win == 1:
            s1 += 1
            label_score_j1.config(text=s1)
        else:
            s2 += 1
            label_score_j2.config(text=s2)
            
        
    
fenetre = Tk()
img = PhotoImage(file='grille_p4.gif')
img_p1 = PhotoImage(file='j1_p4.gif')
img_p2 = PhotoImage(file='j2_p4.gif')
champ_label = Label(fenetre, text="PUISSANCE 4")
canvas = Canvas(fenetre, width=900, height=900, bg='white')

label_j = Label(fenetre, text="Tour du joueur 1")
joueur = 2
label_score_j1 = Label(fenetre, text="0", fg="red", font=("arial",300))
label_score_j2 = Label(fenetre, text="0", fg="yellow", font=("arial",300))

label_score_j1.pack(side=LEFT)
label_score_j2.pack(side=RIGHT)

champ_label.pack()
label_j.pack()

canvas.pack()

col_rect = 'red'

tab_jeu = [[0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0]]

s1 = 0
s2 = 0

def motion(event):
    canvas.delete('rect')
    x, y = event.x/90, event.y/90
    canvas.create_rectangle(x*90,y*90,x*90+90,y*90+90,width=4,outline=col_rect,tag='rect')
    
def click(event):
    global col_rect, joueur, tab_jeu
    col = event.x/90

    if joueur == 1:
        label_j.config(text="Tour du joueur 1")
        canvas.itemconfig('rect', outline='red')
        col_rect = 'red'
        joueur = 2
    else:
        label_j.config(text="Tour du joueur 2")
        canvas.itemconfig('rect', outline='yellow')
        col_rect = 'yellow'
        joueur = 1
    tab_jeu = jouer(joueur,col,tab_jeu)
    canvas.delete("all")
    affiche_jeu2(tab_jeu)

canvas.bind('<Motion>', motion)
canvas.bind('<Button-1>', click)

affiche_jeu2(tab_jeu)

fenetre.mainloop()
