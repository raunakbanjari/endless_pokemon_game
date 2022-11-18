# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 21:48:33 2022

@author: raunak
"""

from tkinter import *
from PIL import ImageTk, Image
import random

root= Tk()
root.title("Endless Pokemon game")
root.geometry("600x400")
root.configure(background= "green")

img_abra= ImageTk.PhotoImage(Image.open ("abra.jpg"))

img_bulbasour= ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
img_button= ImageTk.PhotoImage(Image.open("button.jpg"))
img_charmender= ImageTk.PhotoImage(Image.open("charmender.jpg"))
img_iyvasour= ImageTk.PhotoImage(Image.open("iyvasour.jpg"))
img_jigglypuff= ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
img_kadabra= ImageTk.PhotoImage(Image.open("kadabra.jpg"))
img_ratata= ImageTk.PhotoImage(Image.open("ratata.jpg"))
img_pikachu= ImageTk.PhotoImage(Image.open("pikachu.jpg"))
img_persion= ImageTk.PhotoImage(Image.open("persion.jpg"))
img_meowth= ImageTk.PhotoImage(Image.open("meowth.jpg"))
img_nidoking= ImageTk.PhotoImage(Image.open("nidoking.jpg"))
img_paras= ImageTk.PhotoImage(Image.open("paras.jpg"))
img_squirtle= ImageTk.PhotoImage(Image.open("squirtle.jpg"))

label_heading= Label(root, text= "ENDLESS POKEMON CARDS GAME", font=("Arial", 20), bg= "green", fg= "yellow")

label_player_1= Label(root, text= "player 1", bg= "chocolate1", fg= "white")
label_player_2= Label(root, text= "player 2", bg= "chocolate1", fg= "white")
label_player_1.place(relx= 0.1, rely= 0.3, anchor= CENTER)
label_player_2.place(relx= 0.9, rely= 0.3, anchor= CENTER)

label_score_1= Label(root, bg= "chocolate1", fg= "white")
label_score_1.place(relx= 0.1, rely= 0.4, anchor= CENTER)

label_score_2= Label(root, bg= "chocolate1", fg= "white")
label_score_2.place(relx= 0.9, rely= 0.4, anchor= CENTER)

label_main= Label(root, bg= "navy", fg= "white")
label_main.place(relx= 0.5, rely= 0.5, anchor= CENTER)

label_heading.place(relx= 0.5, rely= 0.1, anchor= CENTER)

label_turn= Label(root, bg= "crimson", fg= "white")
label_turn.place(relx= 0.5, rely= 0.2, anchor= CENTER)



pokemon_list= [img_abra, img_bulbasour, img_charmender, img_iyvasour, img_jigglypuff, img_kadabra, img_ratata, img_pikachu, img_persion, img_meowth, img_nidoking, img_paras, img_squirtle]
power_list= [30,60,50,100,70,70,40,200,70,60,90,40,50]

player_1_score= 0
player_2_score= 0

turn= 1

label_turn["text"]= "Player 1 turn"


label_img= Label(root)
label_img.place(relx= 0.5, rely= 0.6, anchor= CENTER) 

def player_1():
    
    global player_1_score
    global turn
    global status
  
    if turn == 1:
       
       
        label_turn["text"]= "Player 2 turn"
        btn_1["state"]= DISABLED
        btn_2["state"]= ACTIVE
        turn = 2
    
    ran_1= random.randint(0,12)
    random_pokemon= pokemon_list[ran_1]
    random_power= power_list[ran_1]
    player_1_score= player_1_score + random_power
    label_score_1["text"]= player_1_score
    label_img["image"]= random_pokemon

btn_1= Button(root, image= img_button, command= player_1)
btn_1.place(relx= 0.1, rely= 0.6, anchor= CENTER)

def player_2():
    global player_2_score
    global turn
    global status
    
    if turn == 2:
       
       
        label_turn["text"]= "Player 1 turn"
        btn_2["state"]= DISABLED
        btn_1["state"]= ACTIVE
        turn = 1
   
    
    ran_2= random.randint(0,12)
    random_pokemon_2= pokemon_list[ran_2]
    random_power_2= power_list[ran_2]
    player_2_score= player_2_score + random_power_2
    label_score_2["text"]= player_2_score
    label_img["image"]= random_pokemon_2

btn_2= Button(root, image= img_button, command= player_2)
btn_2.place(relx= 0.9, rely= 0.6, anchor= CENTER)
btn_2["state"]= DISABLED




root.mainloop()
