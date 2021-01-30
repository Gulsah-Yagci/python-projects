# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:25:54 2020

@author: HP

"""

import random as rd
import sys
import time


player_points = 0
game_exit = 'q'

menu = {
        '0':'0',
        '1':'1',
        '2':'2',
        'q':'q'
        }


while True:
    
    
    level = input('Menu \n - 0: easy \n - 1: normal \n - 2: hard \n - q: quit \n ')
    
    
    if level == menu.get('0'):
         
        print('-'*5+ ' easy level ' +'-'*5)
        
        while True:
    
           
            random_number = rd.randint(1, 10) 
            print(random_number) 
            
                    
            player_move = input('make a predict')
            
            
            try:
            
                if int(player_move) == random_number:
                    player_points += 10 
                    print('your guess is right! your points:' + str(player_points))
                
                elif int(player_move) != random_number:
                    print('your guess is not right! your points:' + str(player_points))
            except:
                
                print('your score:',player_points)
                time.sleep(1)
                print('quit')
                time.sleep(1)
                break
                
        
    elif level == menu.get('1'):
       
        print('-'*5+ ' normal level ' +'-'*5)
        
        while True:
    
           
            random_number = rd.randint(1, 100) # 0-10 ile 10 dahil
            print(random_number) 
            
                    
            player_move = input('make a predict')
            
            
            try:
            
                if int(player_move) == random_number:
                    player_points += 10 
                    print('your guess is right! your points:' + str(player_points))
                
                elif int(player_move) != random_number:
                    print('your guess is not right! your points:' + str(player_points))
            except:
                
                print('your score:',player_points)
                time.sleep(1)
                print('quit')
                time.sleep(1)
                break
    
    
    elif level == menu.get('2'):
        print('-'*5+ ' hard level ' +'-'*5)
        
        while True:
    
           
            random_number = rd.randint(1, 10) # 0-10 ile 10 dahil
            print(random_number) 
            
                    
            player_move = input('make a predict')
            
            
            try:
            
                if int(player_move) == random_number:
                    player_points += 10 
                    print('your guess is right! your points:' + str(player_points))
                
                elif int(player_move) != random_number:
                    print('your guess is not right! your points:' + str(player_points))
            except:
                
                print('your score:',player_points)
                time.sleep(1)
                print('quit')
                time.sleep(1)
                break
    
    elif level == menu.get('q'):
        
        print('quiting...')
        time.sleep(1)
        sys.exit()
    

                






            
            
               
               
   






