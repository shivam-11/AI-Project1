# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:21:31 2019

@author: Shivam Singh
"""

from tkinter import *
import random


m=0 
def callback(r,c):
    global player
    global m
    global n
    if player =='X' and stop_game == False and states[r][c]==0:
        b[r][c].configure( text = 'X',fg ='red',bg ='black')
        states[r][c]= 'X'
        player = 'O'
        m=m+1
    check_who_won()    
    if(m<5 and stop_game == False):
      n=0
      attack()
      
      if n==0:
          call_next()
         
   # if player =='O' and stop_game == False and states[r][c]==0:
    #    b[r][c].configure(text = 'O',fg ='red',bg ='black')
     #   states[r][c]= 'O'
      #  player = 'X'    
    check_who_won()
def call_next():
     global player
     global n,m
     x=False
     list = [0,1,2]
     
     for i in range(3):
        if states[i][0]=='X' and states[i][1]=='X' and states[i][2]==0:
             b[i][2].configure( text = 'O',fg ='red',bg ='black')
             states[i][2]= 'O'
             player = 'X'
             
             return
     
        if states[i][0]==0 and states[i][1]=='X' and states[i][2]=='X':
             b[i][0].configure( text = 'O',fg ='red',bg ='black')
             states[i][0]= 'O'
             player = 'X'
             
             return
           
        if states[i][0]=='X' and states[i][1]==0 and states[i][2]=='X':
             b[i][1].configure( text = 'O',fg ='red',bg ='black')
             states[i][1]= 'O'
             player = 'X'
             
             return          
    
    
     for i in range(3):
        if states[0][i]=='X' and states[1][i]=='X' and states[2][i]==0:
             b[2][i].configure( text = 'O',fg ='red',bg ='black')
             states[2][i]= 'O'
             player = 'X'
             
             return
     
        if states[0][i]==0 and states[1][i]=='X' and states[2][i]=='X':
             b[0][i].configure( text = 'O',fg ='red',bg ='black')
             states[0][i]= 'O'
             player = 'X'
             
             return
           
        if states[0][i]=='X' and states[1][i]==0 and states[2][i]=='X':
             b[1][i].configure( text = 'O',fg ='red',bg ='black')
             states[1][i]= 'O'
             player = 'X'
             
             return 
         
            
     if states[0][0]=='X' and states[1][1]=='X' and states[2][2]==0:
          b[2][2].configure( text = 'O',fg ='red',bg ='black')
          states[2][2]= 'O'
          player = 'X'
          n=1
          return 
      
     if states[0][0]=='X' and states[1][1]==0 and states[2][2]=='X':
          b[1][1].configure( text = 'O',fg ='red',bg ='black')
          states[1][1]= 'O'
          player = 'X'
          
          return
      
     if states[0][0]==0 and states[1][1]=='X' and states[2][2]=='X':
          b[0][0].configure( text = 'O',fg ='red',bg ='black')
          states[0][0]= 'O'
          player = 'X'
          
          return
      
     if states[0][2]=='X' and states[1][1]=='X' and states[2][0]==0:
          b[2][0].configure( text = 'O',fg ='red',bg ='black')
          states[2][0]= 'O'
          player = 'X'
          
          return
      
     if states[0][2]=='X' and states[1][1]==0 and states[2][0]=='X':
          b[1][1].configure( text = 'O',fg ='red',bg ='black')
          states[1][1]= 'O'
          player = 'X'
          
          return
      
     if states[0][2]==0 and states[1][1]=='X' and states[2][0]=='X':
          b[0][2].configure( text = 'O',fg ='red',bg ='black')
          states[0][2]= 'O'
          player = 'X'
          
          return
      
   
   
    
     while(x==False):
           i = random.choice(list)
           j = random.choice(list)
           if states[i][j]==0:
               x=True
     b[i][j].configure( text = 'O',fg ='red',bg ='black')
     states[i][j]= 'O'
     player = 'X'
     n=1
   

def attack():
    
     global n
    
     for i in range(3):
        if states[i][0]=='O' and states[i][1]=='O' and states[i][2]==0:
             b[i][2].configure( text = 'O',fg ='red',bg ='black')
             states[i][2]= 'O'
             player = 'X'
             n=1
             return
     
        if states[i][0]==0 and states[i][1]=='O' and states[i][2]=='O':
             b[i][0].configure( text = 'O',fg ='red',bg ='black')
             states[i][0]= 'O'
             player = 'X'
             n=1
             return
           
        if states[i][0]=='O' and states[i][1]==0 and states[i][2]=='O':
             b[i][1].configure( text = 'O',fg ='red',bg ='black')
             states[i][1]= 'O'
             player = 'X'
             n=1
             return          
    
    
     for i in range(3):
        if states[0][i]=='O' and states[1][i]=='O' and states[2][i]==0:
             b[2][i].configure( text = 'O',fg ='red',bg ='black')
             states[2][i]= 'O'
             player = 'X'
             n=1
             return
     
        if states[0][i]==0 and states[1][i]=='O' and states[2][i]=='O':
             b[0][i].configure( text = 'O',fg ='red',bg ='black')
             states[0][i]= 'O'
             player = 'X'
             n=1
             return
           
        if states[0][i]=='O' and states[1][i]==0 and states[2][i]=='O':
             b[1][i].configure( text = 'O',fg ='red',bg ='black')
             states[1][i]= 'O'
             player = 'X'
             n=1
             return 
         
            
     if states[0][0]=='O' and states[1][1]=='O' and states[2][2]==0:
          b[2][2].configure( text = 'O',fg ='red',bg ='black')
          states[2][2]= 'O'
          player = 'X'
          n=1
          return 
      
     if states[0][0]=='O' and states[1][1]==0 and states[2][2]=='O':
          b[1][1].configure( text = 'O',fg ='red',bg ='black')
          states[1][1]= 'O'
          player = 'X'
          n=1
          return
      
     if states[0][0]==0 and states[1][1]=='O' and states[2][2]=='O':
          b[0][0].configure( text = 'O',fg ='red',bg ='black')
          states[0][0]= 'O'
          player = 'X'
          n=1
          return
      
     if states[0][2]=='O' and states[1][1]=='O' and states[2][0]==0:
          b[2][0].configure( text = 'O',fg ='red',bg ='black')
          states[2][0]= 'O'
          player = 'X'
          n=1
          return
      
     if states[0][2]=='O' and states[1][1]==0 and states[2][0]=='O':
          b[1][1].configure( text = 'O',fg ='red',bg ='black')
          states[1][1]= 'O'
          player = 'X'
          n=1
          return
      
     if states[0][2]==0 and states[1][1]=='O' and states[2][0]=='O':
          b[0][2].configure( text = 'O',fg ='red',bg ='black')
          states[0][2]= 'O'
          player = 'X'
          n=1
          return
      
        
     
def check_who_won():
    global stop_game

    
    for i in range(3):
        if states[i][0]==states[i][1]==states[i][2]!=0:
            b[i][0].config(bg='grey')
            b[i][1].config(bg='grey')
            b[i][2].config(bg='grey')            
            stop_game =True
            
    for i in range(3):
        if states[0][i]==states[1][i]==states[2][i]!=0:
            b[0][i].config(bg='grey')
            b[1][i].config(bg='grey')
            b[2][i].config(bg='grey')            
            stop_game =True  
            
    if states[0][0]==states[1][1]==states[2][2]!=0:
         b[0][0].config(bg='grey')
         b[1][1].config(bg='grey')
         b[2][2].config(bg='grey')            
         stop_game =True  

    if states[0][2]==states[1][1]==states[2][0]!=0:
         b[0][2].config(bg='grey')
         b[1][1].config(bg='grey')
         b[2][0].config(bg='grey')            
         stop_game =True            
    
    


root =Tk()
root.title("tic tac toe")
 

b= [[0,0,0],
    [0,0,0],
    [0,0,0]]

states = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=("arial",60),width=4,bg='black',command = lambda r=i,c=j: callback(r,c))
        b[i][j].grid(row =i,column =j)
        
        
        
player ='X'
stop_game = False
mainloop()

        