import pygame
import time
import random
from tkinter import *

main_window =Tk()
# start_window =Tk()


# def on_click_1():
#     tm = 1.5
#     quit()
# def on_click_2():
#     tm = 1.0
#     quit()
# def on_click_3():
#     tm = 0.05
#     quit()

# Label(start_window,text = "CHOOSE THE DIFFICULTY LEVEL").grid(row =0, column =0)

# Button(start_window,text="EASY",padx =40, pady =20,command =on_click_1).grid(row=1 , column =0 )
# Button(start_window,text="MEDIUM",padx =40, pady =20,command = on_click_2).grid(row=2 , column =0 )
# Button(start_window,text="HARD",padx =40, pady =20,command = on_click_3).grid(row=3 , column =0 )


# start_window.mainloop()

tm = 0.1
score = 0



def change(lst_x,lst_y,x,y,score):

    for i in range(1,score):
        lst_x[score-i] =lst_x[score-i-1]
        lst_y[score-i] =lst_y[score-i-1]

    # lst_x[1] = lst_x[2]
    # lst_x[2] = lst_x[3]
    lst_x[0] = x 

    # lst_y[1] = lst_y[2]
    # lst_y[2] = lst_y[3]
    lst_y[0] = y




def block_movement(background_image,body,screen,food,block,x,y,a,b,lst_x,lst_y,score):
    #screen : object of window
    #block : image object
    
    screen.fill((0,128,128))
    screen.blit(background_image,(0,0))
    screen.blit(block,(x,y))

    for i in range(0,score):
        screen.blit(body[i],(lst_x[i],lst_y[i]))

    # screen.blit(body,(lst_x[3],lst_y[3]))
    # screen.blit(body,(lst_x[2],lst_y[2]))
    # screen.blit(body,(lst_x[1],lst_y[1]))

    screen.blit(food,(a,b))
                
    pygame.display.flip()


def game(score,tm):
    pygame.init()


    size = (700,500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("GAME DEMO")

    #adding background color
    screen.fill((0,128,128))

    background_image = pygame.image.load("bg.jpg").convert()
    food = pygame.image.load("food.jpg").convert()

    screen.blit(background_image,(0,0))

    #load resources
    block_pos_x = pygame.image.load("nsnake_pos_x.jpg").convert()
    block_pos_y = pygame.image.load("nsnake_pos_y.jpg").convert()
    block_neg_y = pygame.image.load("nsnake_neg_y.jpg").convert()
    block_neg_x = pygame.image.load("nsnake_neg_x.jpg").convert()
    block = block_pos_x
    body =[]
    for i in range(2000):
        body.append(pygame.image.load("body.jpg").convert())

    x=40
    y=40

    lst_x = [20]
    lst_y = [20]

    for i in range(0,score):
        screen.blit(body[i],(lst_x[i],y))

    # screen.blit(body,(lst_x[1],y))
    # screen.blit(body,(lst_x[2],y))
    # screen.blit(body,(lst_x[3],y))

    screen.blit(block,(x,y))

    running =True
    run = True
    

    prev_dir = '+'
    prev_key = 'x'

    eat = True

    a =300
    b =300

    while running:

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN:
                    change(lst_x,lst_y,x,y,score)
                    y +=20
                    block = block_neg_y
                    block_movement(background_image,body,screen,food,block,x,y,a,b,lst_x,lst_y,score)
                    prev_key = 'y'
                    prev_dir = '+'
                elif event.key == pygame.K_UP:
                    change(lst_x,lst_y,x,y,score)
                    y -=20
                    block = block_pos_y
                    block_movement(background_image,body,screen,food,block,x,y,a,b,lst_x,lst_y,score)
                    prev_key = 'y'
                    prev_dir = '-'
                elif event.key == pygame.K_LEFT:
                    change(lst_x,lst_y,x,y,score)
                    x -=20
                    block = block_neg_x
                    block_movement(background_image,body,screen,food,block,x,y,a,b,lst_x,lst_y,score)
                    prev_key = 'x'
                    prev_dir = '-'
                elif event.key == pygame.K_RIGHT:
                    change(lst_x,lst_y,x,y,score)
                    x +=20
                    block = block_pos_x
                    block_movement(background_image,body,screen,food,block,x,y,a,b,lst_x,lst_y,score)
                    prev_key = 'x'
                    prev_dir = '+'


            elif event.type == pygame.QUIT:
                running = False


        if (x<40 or x>640) and (y<176 or y>324):
            bg_end_image = pygame.image.load("background.jpg").convert()
            screen.blit(bg_end_image,(0,0))
            pygame.display.flip()
        elif (y<40 or y>440) and (x<273 or x>422):
            bg_end_image = pygame.image.load("background.jpg").convert()
            screen.blit(bg_end_image,(0,0))
            pygame.display.flip()


            

        # if x<=634 and y<=438 and x>=40 and y>=40:
        elif x<=690 and y<=490 and x>=-10 and y>=-10:
            if prev_key == 'x':
                if prev_dir == '+':
                    change(lst_x,lst_y,x,y,score)
                    x += 20
                else:
                    change(lst_x,lst_y,x,y,score)
                    x -= 20
                    
            elif prev_key == 'y':
                if prev_dir == '+':
                    change(lst_x,lst_y,x,y,score)
                    y += 20
                else:
                    change(lst_x,lst_y,x,y,score)
                    y -= 20

            block_movement(background_image,body,screen,food,block,x,y,a,b,lst_x,lst_y,score)
                    
            time.sleep(tm)  

        elif x>690 and y>175 and y<305:
            x = 0
        elif y>490 and x>274 and x<400:
            y=0
        elif x<-10 and y>175 and y<305:
            x = 690
        elif y<-10:
            y = 490

        if eat == True:
            a = random.randint(40,620)
            b = random.randint(40,420)
            eat = False
            score +=1
            tm -= 0.003

            if prev_key == 'x':
                if prev_dir == '+':
                    lst_x.append(a+20)
                    lst_y.append(b+20)
                else:
                    lst_x.append(a-20)
                    lst_y.append(b-20)
                    
            elif prev_key == 'y':
                if prev_dir == '+':
                    lst_x.append(a+20)
                    lst_y.append(b+20)
                else:
                    lst_x.append(a-20)
                    lst_y.append(b-20)

            # lst_x.append(a)
            # lst_y.append(b)
        
        if abs(x-a)<=20 and abs(y-b)<=20:
            eat = True

        # update the screen


        pygame.display.flip()

    return score


if __name__=='__main__':
    score = game(score,tm)




Label(main_window,text = "GAME IS OVER").grid(row =5, column =2)
score_str = "YOUR SCORE IS "+str(score-1)
Label(main_window,text = score_str).grid(row = 10, column = 2)


main_window.mainloop()