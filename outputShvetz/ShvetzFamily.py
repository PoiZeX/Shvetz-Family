# !/usr/local/bin/python
# -*- coding: utf-8 -*-

import pygame
from time import *
import time
import os
import numpy as np
import cv2
import random
import winsound

pygame.init()
# pygame.mixer.init()

##################################################
###################COLORS#########################
##################################################

red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
##################################################
display_width = 800
display_height = 600
##################################################
##################################################
mom_loc = [(25, 73), (215, 73), (410, 73), (615, 73), (25, 285), (215, 285), (410, 285), (615, 285), (25, 490),
           (215, 490), (410, 490), (615, 490)]
##################################################
level = 0
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Shvetz')
clock = pygame.time.Clock()
crashed = False


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

carImg = pygame.image.load(resource_path('mainC.png'))
goodImg = [pygame.image.load(resource_path('o1.png')), pygame.image.load(resource_path('o2.png'))]
badImg = pygame.image.load(resource_path('o3.png'))
bg = pygame.image.load(resource_path('bg3.png'))
bg_ball = pygame.image.load(resource_path('bg_ball.png'))
introImg = pygame.image.load(resource_path('intro.jpg'))
bg_level1 = pygame.image.load(resource_path('forest.png'))
hole_mom = pygame.image.load(resource_path('mom_hole.png'))
hole_gm1 = pygame.image.load(resource_path('grand_hole1.png'))
hole_gm2 = pygame.image.load(resource_path('grand_hole2.png'))
ball = pygame.image.load(resource_path('ball.png'))
super_dad = pygame.image.load(resource_path('super_dad.png'))
dad = pygame.image.load(resource_path('dad.png'))
pishoto = pygame.image.load(resource_path('pishoto.png'))
strong_pishoto = pygame.image.load(resource_path('strongpishoto.png'))
strong_pishoto2 = pygame.image.load(resource_path('strongpishoto2.png'))


# sword = pygame.image.load(r'C:\Users\lidor\Desktop\Shvetz_Game\sword.png').convert_alpha()

def getVideoSource(source, width, height):
    vid = cv2.VideoCapture(source)
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    return vid


def video_play(vid_file, start_frame, next_level, sound_file):
    cap = cv2.VideoCapture(vid_file)

    #player = MediaPlayer(file_name)
    #player.set_volume(30)
    cap.set(1, start_frame)
    # Check if camera opened successfully
    if cap.isOpened() == False:
        print("Error opening video  file")
    else:
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    # Read until video is completed
    while cap.isOpened():
        #audio_frame, val = player.get_frame()
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame
            cv2.imshow('Shvetz', cv2.resize(frame, (850, 600)))

            cv2.resizeWindow('Shvetz', 850, 600)
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        # Break the loop
        else:
            break
    # the video capture object
    cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()

    intro(next_level)


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def explain_window(levelnum):
    if levelnum == 1:
        gameDisplay.blit(bg_level1, (0, 0))
        font = pygame.font.SysFont('Comic Sans MS', 30)
        tfont = pygame.font.SysFont('Comic Sans MS', 50)
        pygame.draw.rect(gameDisplay, bright_red, [int(display_width / 12), int(display_height / 12), 670, 500])
        pygame.draw.rect(gameDisplay, red, [int(display_width / 12 + 10), int(display_height / 12 + 10), 650, 480])
        title = tfont.render('Hit the grandma!', True, white)
        todo = tfont.render('Press Enter to start', True, white)

        text1 = font.render('+1 Point <---------                    +', True, black)
        text2 = font.render('-1 Points <-------------------', True, black)
        text3 = font.render('Get 30 Points to WIN!', True, black)
        gameDisplay.blit(hole_gm1, (550, 150))
        gameDisplay.blit(hole_gm2, (350, 150))
        gameDisplay.blit(hole_mom, (490, 300))
        gameDisplay.blit(title, (100, 60))
        gameDisplay.blit(text1, (100, 200))
        gameDisplay.blit(text2, (100, 350))
        gameDisplay.blit(text3, (250, 420))
        gameDisplay.blit(todo, (180, 470))

        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            while event.type != pygame.KEYDOWN:
                explain_window(levelnum)
            if event.key == 13:
                level_2()
    elif levelnum == 4:
        gameDisplay.blit(bg_ball, (0, 0))
        font = pygame.font.SysFont('Comic Sans MS', 30)
        tfont = pygame.font.SysFont('Comic Sans MS', 50)
        gfont = pygame.font.SysFont('Comic Sans MS', 20)
        pygame.draw.rect(gameDisplay, bright_red, [int(display_width / 12), int(display_height / 12), 670, 500])
        pygame.draw.rect(gameDisplay, red, [int(display_width / 12 + 10), int(display_height / 12 + 10), 650, 480])
        title = tfont.render('Kill Pishoto and Haim!', True, white)
        todo = tfont.render('Press Enter to start', True, white)

        text1 = font.render('Use the arrows to move', True, black)
        text11 = font.render('and SPACE to throw balls', True, black)
        text2 = font.render('Stay in the red zone', True, black)
        text3 = font.render('Get 10 Points to WIN!', True, black)
        text33 = gfont.render('(try to)', True, black)
        gameDisplay.blit(title, (100, 60))
        gameDisplay.blit(text1, (100, 200))
        gameDisplay.blit(text11, (100, 250))
        gameDisplay.blit(text2, (100, 350))
        gameDisplay.blit(text3, (250, 420))
        gameDisplay.blit(text33, (490, 450))
        gameDisplay.blit(todo, (180, 470))

        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            while event.type != pygame.KEYDOWN:
                explain_window(4)
            if event.key == 13:
                level_4()
    elif levelnum == 6:
        gameDisplay.blit(bg_level1, (0, 0))
        font = pygame.font.SysFont('Comic Sans MS', 30)
        tfont = pygame.font.SysFont('Comic Sans MS', 50)
        pygame.draw.rect(gameDisplay, bright_red, [int(display_width / 12), int(display_height / 12), 670, 500])
        pygame.draw.rect(gameDisplay, red, [int(display_width / 12 + 10), int(display_height / 12 + 10), 650, 480])
        title = tfont.render('Hatzir!', True, white)
        todo = tfont.render('Press Enter to start', True, white)

        text1 = font.render('Use the arrows to collect        ,       ', True, black)
        text2 = font.render('and avoid from:', True, black)
        text3 = font.render('Get 10 Points to WIN!', True, black)
        gameDisplay.blit(goodImg[0], (555, 180))
        gameDisplay.blit(goodImg[1], (460, 200))
        gameDisplay.blit(badImg, (305, 330))
        gameDisplay.blit(title, (100, 60))
        gameDisplay.blit(text1, (100, 200))
        gameDisplay.blit(text2, (100, 350))
        gameDisplay.blit(text3, (250, 420))
        gameDisplay.blit(todo, (180, 470))

        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            while event.type != pygame.KEYDOWN:
                explain_window(6)
            if event.key == 13:
                level_6()


def message_display(text):
    largeText = pygame.font.SysFont('david', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (int(display_width / 2), int(display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)


def Credits():
    gameDisplay.blit(bg, (0, 0))
    font = pygame.font.SysFont('david', 40)
    gfont = pygame.font.SysFont('david', 20)
    tfont = pygame.font.SysFont('david', 90)
    pygame.draw.rect(gameDisplay, white, [int(display_width / 12), int(display_height / 12), 670, 500])
    pygame.draw.rect(gameDisplay, red, [int(display_width / 12 + 10), int(display_height / 12 + 10), 650, 480])

    title = tfont.render('!תודות', True, white)

    text1 = font.render('ץווש תחפשמ', True, black)
    text2 = font.render('הווקנא רודיל', True, black)
    text3 = gfont.render('האיציל רטנא ץחל', True, black)

    gameDisplay.blit(title, (280, 80))
    gameDisplay.blit(text1, (300, 200))
    gameDisplay.blit(text2, (295, 350))
    gameDisplay.blit(text3, (90, 520))

    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        while event.type != pygame.KEYDOWN:
            Credits()
        if event.key == 13:
            quit()


def message_btn(text, x, y, size):
    largeText = pygame.font.SysFont(r'david', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (int(x), int(y))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


def crash():
    message_display('חורבל רוסא')


def ball_obst(immg, x, y):
    gameDisplay.blit(immg, (x, y))


def obst_1(immg, x, y):
    gameDisplay.blit(immg, (x, y))


def obst_2(immg, x, y):
    gameDisplay.blit(immg, (x, y))


def obst_3(immg, x, y):
    gameDisplay.blit(immg, (x, y))


def obst_4(immg, x, y):
    gameDisplay.blit(immg, (x, y))


def obst_5(immg, x, y):
    gameDisplay.blit(immg, (x, y))


def obst_6(immg, x, y):
    gameDisplay.blit(immg, (x, y))


def obst_7(immg, x, y):
    gameDisplay.blit(immg, (x, y))


def obst_8(immg, x, y):
    gameDisplay.blit(immg, (x, y))


def obst_9(immg, x, y):
    gameDisplay.blit(immg, (x, y))


def obst_10(immg, x, y):
    gameDisplay.blit(immg, (x, y))


def text_score(count):
    font = pygame.font.SysFont('david', 25)
    text = font.render("Score: " + str(count), True, red, black)
    gameDisplay.blit(text, (int(display_width - 90), 0))


def text_time(string):
    font = pygame.font.SysFont('david', 25)
    text = font.render("Time left: " + str(string), True, black, white)
    gameDisplay.blit(text, (int(display_width * 0.7), 0))


def level_4():
    x = int(700)
    y = int(display_height * 0.7)
    y_change, x_change = 0, 0
    crashed = False
    car_width = 47
    car_height = 73
    ##################
    obj_speed = 15
    obj_width = 39
    obj_height = 31
    y_range = []
    x_range = []
    x_ball, y_ball = -display_width, 0
    for i in range(10):
        y_range.append(0)
        x_range.append(random.randint(0, 200))
    ##################
    kill = False
    count = 0
    throw = False
    ###################

    while not crashed:
        if x < 600:  # ZONE CHECK
            x = 700
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            ############################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                if event.key == pygame.K_SPACE:
                    throw = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
            ######################
        x += x_change
        y += y_change
        ##
        gameDisplay.blit(bg_ball, (0, 0))
        pygame.draw.rect(gameDisplay, red, (600, 0, 5, display_height))  # ZONE

        #############################################
        ################### BALLS ###################
        #############################################
        if count == 0:
            y_range[0] += 4
            x_ball -= obj_speed
        elif count == 1:
            y_range[0] += display_height * 2  # זורק את האובייקט הישן קיבינימט
            obst_2(strong_pishoto2, x=x_range[count], y=y_range[count])  # יוצר אובייקט חדש להשמדה
            y_range[count] += 4
            x_ball -= obj_speed

        elif count == 2:
            y_range[count - 1] += display_height * 2  # זורק את האובייקט הישן קיבינימט
            obst_3(strong_pishoto, x=x_range[count], y=y_range[count])  # יוצר אובייקט חדש להשמדה
            y_range[count] += 7
            x_ball -= obj_speed

        elif count == 3:
            y_range[count - 1] += display_height * 2  # זורק את האובייקט הישן קיבינימט
            obst_4(pishoto, x=x_range[count], y=y_range[count])  # יוצר אובייקט חדש להשמדה
            y_range[count] += 8
            x_ball -= obj_speed

        elif count == 4:
            y_range[count - 1] += display_height * 2  # זורק את האובייקט הישן קיבינימט
            obst_5(dad, x=x_range[count], y=y_range[count])  # יוצר אובייקט חדש להשמדה
            y_range[count] += 8
            x_ball -= obj_speed

        elif count == 5:
            y_range[count - 1] += display_height * 2  # זורק את האובייקט הישן קיבינימט
            obst_6(super_dad, x=x_range[count], y=y_range[count])  # יוצר אובייקט חדש להשמדה
            y_range[count] += 10
            x_ball -= obj_speed

        elif count == 6:
            y_range[count - 1] += display_height * 2  # זורק את האובייקט הישן קיבינימט
            obst_7(dad, x=x_range[count], y=y_range[count])  # יוצר אובייקט חדש להשמדה
            y_range[count] += 12
            x_ball -= obj_speed * 1.2

        elif count == 7:
            y_range[count - 1] += display_height * 2  # זורק את האובייקט הישן קיבינימט
            obst_8(pishoto, x=x_range[count], y=y_range[count])  # יוצר אובייקט חדש להשמדה
            y_range[count] += 12
            x_ball -= obj_speed * 1.2
        elif count == 8:
            y_range[count - 1] += display_height * 2  # זורק את האובייקט הישן קיבינימט
            obst_9(dad, x=x_range[count], y=y_range[count])  # יוצר אובייקט חדש להשמדה
            y_range[count] += 16
            x_ball -= obj_speed * 1.5
        elif count == 9:
            y_range[count - 1] += display_height * 2  # זורק את האובייקט הישן קיבינימט
            obst_10(super_dad, x=x_range[count], y=y_range[count])  # יוצר אובייקט חדש להשמדה
            y_range[count] += 16
            x_ball -= obj_speed * 2

        elif count == 10:
            y_range[count - 1] += display_height * 2
            # message_btn("ילש ןמשו בוט ןב", (display_width/2), (display_height/2), 115)
            intro(5)

        #############################################

        text_score(count)
        car(x, y)
        ball_obst(ball, x_ball, y_ball)
        obst_1(pishoto, x_range[0], y_range[0])

        if x > display_width - car_width or x < 0 or y > display_height - car_height or y < 0:  # Boundries
            crash()
            level_4()

        if throw:
            x_ball = x - 80
            y_ball = y
            throw = False
        for i in range(0, 10):
            if x_range[i] - 10 < x_ball < x_range[i] + obj_width + 30 and y_range[i] - obj_height - 30 < y_ball < \
                    y_range[i] + 30:  # Object crash
                # pygame.mixer.music.load(r'sounds\shvetz_tit_sound.mp3')
                winsound.PlaySound(resource_path('shvetz_tit_sound.wav'), winsound.SND_ASYNC)

                car(x, y)
                count += 1
                text_score(count)
                # pygame.mixer.music.play()

        if y_range[0] > display_height:
            y_range[0] = 0
            x_range[0] = random.randint(0, 200)
        if y_range[1] > display_height:
            y_range[1] = 0 - obj_height
            x_range[1] = random.randint(0, 200)
        if y_range[2] > display_height:
            y_range[2] = 0 - obj_height
            x_range[2] = random.randint(0, 200)
        if y_range[3] > display_height:
            y_range[3] = 0 - obj_height
            x_range[3] = random.randint(0, 200)
        if y_range[4] > display_height:
            y_range[4] = 0 - obj_height
            x_range[4] = random.randint(0, 200)
        if y_range[5] > display_height:
            y_range[5] = 0 - obj_height
            x_range[5] = random.randint(0, 200)
        if y_range[6] > display_height:
            y_range[6] = 0 - obj_height
            x_range[6] = random.randint(0, 200)
        if y_range[7] > display_height:
            y_range[7] = 0 - obj_height
            x_range[7] = random.randint(0, 200)
        if y_range[8] > display_height:
            y_range[8] = 0 - obj_height
            x_range[8] = random.randint(0, 200)
        if y_range[9] > display_height:
            y_range[9] = 0 - obj_height
            x_range[9] = random.randint(0, 200)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


def timer(time, func_to_do):
    t = Timer(time, func_to_do)
    t.start()
    t.join()


def level_2(points=0):
    if points == -2:
        # pygame.mixer.music.load(r'sounds\shvetz_1_sound.mp3')
        # pygame.mixer.music.play()
        winsound.PlaySound(resource_path('shvetz_1_sound.wav'), winsound.SND_ASYNC)

        explain_window(1)

    tt, text = 5, '5'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    pygame.mouse.set_cursor(*pygame.cursors.diamond)
    gameDisplay.blit(bg_level1, (0, 0))
    if points < 5:
        tt, text = 1.5, '1.5'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        mom_or_grand = random.choice((hole_gm1, hole_gm2))
        char0 = gameDisplay.blit(mom_or_grand, mom_loc[random.randint(0, 11)])
    elif 5 <= points < 20:
        tt, text = 1.0, '1.0'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 500)
        loc1, loc2, loc3 = mom_loc[random.randint(0, 11)], mom_loc[random.randint(0, 11)], mom_loc[
            random.randint(0, 11)]
        mom_or_grand, mom_or_grand2 = hole_mom, random.choice((hole_gm1, hole_gm2))
        while loc1 == loc2 or loc3 == loc2 or loc2 == loc1:
            loc2 = mom_loc[random.randint(0, 11)]  # change just the grandma
        char1 = gameDisplay.blit(mom_or_grand, loc1)  # MOM
        char3 = gameDisplay.blit(mom_or_grand, loc3)  # MOM
        char2 = gameDisplay.blit(mom_or_grand2, loc2)
    elif 20 <= points < 31:
        tt, text = 0.9, '0.9'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 300)
        loc1, loc2, loc3 = mom_loc[random.randint(0, 11)], mom_loc[random.randint(0, 11)], mom_loc[
            random.randint(0, 11)]
        mom_or_grand, mom_or_grand2 = hole_mom, random.choice((hole_gm1, hole_gm2))
        while loc1 == loc2 or loc3 == loc2 or loc2 == loc1:
            loc2 = mom_loc[random.randint(0, 11)]  # change just the grandma
        while mom_or_grand == mom_or_grand2:
            mom_or_grand = random.choice((hole_gm1, hole_gm2, hole_mom))
        char1 = gameDisplay.blit(mom_or_grand, loc1)  # MOM
        char3 = gameDisplay.blit(mom_or_grand, loc3)  # MOM
        char2 = gameDisplay.blit(mom_or_grand2, loc2)

    text_score(points)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                tt -= 0.5
                text = str(tt).rjust(3) if tt > 0 else level_2(points)
            if event.type == pygame.QUIT:
                quit()
            if points == 30:
                message_display("Win")
                intro(3)
            if points < 5:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if char0.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        # pygame.mixer.music.load(r'sounds\shvetz_1_sound_kill.mp3')
                        # pygame.mixer.music.play()
                        winsound.PlaySound(resource_path('shvetz_1_sound_kill.wav'), winsound.SND_ASYNC)
                        points += 1
                        level_2(points)
            elif points >= 5 and points < 31:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if char1.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]) or char3.collidepoint(
                            pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        points -= 1
                        level_2(points)
                    elif char2.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                        points += 1
                        level_2(points)

        # text_time(text)
        pygame.display.update()
        clock.tick(60)


def level_6():
    gameDisplay.blit(bg, (0, 0))

    x = int(display_width * 0.45)
    y = int(display_height * 0.7)
    x, y = int(x), int(y)
    y_change, x_change = 0, 0
    crashed = False
    car_width = 47
    car_height = 73
    ##################
    obj_width = 55
    obj_height = 72
    y_range = [random.randrange(-600, -100), random.randrange(-600, -100), random.randrange(-600, -100),
               random.randrange(-600, -100), random.randrange(-600, -100), random.randrange(-600, -100),
               random.randrange(-600, -100), random.randrange(-600, -100), random.randrange(-600, -100),
               random.randrange(-600, -100)]
    x_range = [random.randrange(0, display_width - obj_width), random.randrange(0, display_width - obj_width),
               random.randrange(0, display_width - obj_width), random.randrange(0, display_width - obj_width),
               random.randrange(0, display_width - obj_width), random.randrange(0, display_width - obj_width),
               random.randrange(0, display_width - obj_width), random.randrange(0, display_width - obj_width),
               random.randrange(0, display_width - obj_width), random.randrange(0, display_width - obj_width)]
    ##################
    count = 0

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            ############################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
            ######################
        x += x_change
        y += y_change
        ##
        gameDisplay.blit(bg, (0, 0))

        if count == 0:
            y_range[0] += random.randrange(4, 8)

        elif count == 1:
            y_range[0] += display_height * 2
            obst_2(goodImg[1], x=x_range[1], y=y_range[1])
            y_range[1] += 6

        elif count == 2:
            y_range[1] += display_height * 2
            obst_3(goodImg[0], x=x_range[2], y=y_range[2])
            y_range[2] += 7

        elif count == 3:
            y_range[2] += display_height * 2
            obst_4(goodImg[0], x=x_range[3], y=y_range[3])
            y_range[3] += 8
        elif count == 4:
            y_range[3] += display_height * 2
            obst_5(badImg, x=x_range[4], y=y_range[4])
            y_range[4] += 3
        elif count == 5:
            y_range[4] += display_height * 2
            obst_6(goodImg[0], x=x_range[5], y=y_range[5])
            y_range[5] += 8
        elif count == 6:
            y_range[5] += display_height * 2
            obst_7(goodImg[0], x=x_range[6], y=y_range[6])
            y_range[6] += 9
        elif count == 7:
            y_range[6] += display_height * 2
            obst_8(goodImg[0], x=x_range[7], y=y_range[7])
            y_range[7] += 11
        elif count == 8:
            y_range[7] += display_height * 2
            obst_9(goodImg[1], x=x_range[8], y=y_range[8])
            y_range[8] += 12
        elif count == 9:
            y_range[8] += display_height * 2
            obst_10(goodImg[1], x=x_range[9], y=y_range[9])
            y_range[9] += 13
        elif count == 10:
            y_range[9] += display_height * 2
            message_btn("ילש ןמשו בוט ןב", int(display_width / 2), int(display_height / 2), 115)
            time.sleep(3)
            intro(7)

        text_score(count)
        car(x, y)
        obst_1(goodImg[0], x_range[0], y_range[0])

        if x > display_width - car_width or x < 0 or y > display_height - car_height or y < 0:  # Boundries
            crash()
            explain_window(6)

        for i in range(0, 10):
            if x_range[i] - 20 < x < x_range[i] + obj_width + 20 and y_range[i] - obj_height - 20 < y < y_range[i] \
                    + 20:  # Object crash
                if i == 4:
                    # pygame.mixer.music.load(r'sounds\shvetz_mural.mp3')
                    # pygame.mixer.music.play()
                    winsound.PlaySound(resource_path('shvetz_mural.wav'), winsound.SND_ASYNC)
                    message_display('!לערומ הז')
                    explain_window(6)

                car(x, y)
                count += 1
                text_score(count)
                pygame.display.update()

        if y_range[0] > display_height:
            y_range[0] = 0
            x_range[0] = random.randrange(0, display_width)
        if y_range[1] > display_height:
            y_range[1] = 0 - obj_height
            x_range[1] = random.randrange(0, display_width)
        if y_range[2] > display_height:
            y_range[2] = 0 - obj_height
            x_range[2] = random.randrange(0, display_width)
        if y_range[3] > display_height:
            y_range[3] = 0 - obj_height
            x_range[3] = random.randrange(0, display_width)
        if y_range[4] > display_height:
            y_range[4] = -7000
            x_range[4] = random.randrange(0, display_width)
            count = 5
        if y_range[5] > display_height:
            y_range[5] = 0 - obj_height
            x_range[5] = random.randrange(0, display_width)
        if y_range[6] > display_height:
            y_range[6] = 0 - obj_height
            x_range[6] = random.randrange(0, display_width)
        if y_range[7] > display_height:
            y_range[7] = 0 - obj_height
            x_range[7] = random.randrange(0, display_width)
        if y_range[8] > display_height:
            y_range[8] = 0 - obj_height
            x_range[8] = random.randrange(0, display_width)
        if y_range[9] > display_height:
            y_range[9] = 0 - obj_height
            x_range[9] = random.randrange(0, display_width)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

def intro(level):
    if level == 0:
        winsound.PlaySound(resource_path('shvetz_intro_sound.wav'), winsound.SND_ASYNC)
        #pygame.mixer.music.load(r'sounds\shvetz_intro_sound.mp3')
        #pygame.mixer.music.play()

    if level == 6:
        sleep(1)
        # pygame.mixer.music.load(r'sounds\shvetz_bat.mp3')
        # pygame.mixer.music.play()
        winsound.PlaySound(resource_path('shvetz_bat.wav'), winsound.SND_ASYNC)



    while level == 0:

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if btn.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    intro(1)
        gameDisplay.blit(introImg, (-200, 0))
        btn = pygame.draw.rect(gameDisplay, green, (200, 550, 300, 40))
        message_btn("?ץימא קיפסמ היהי ימ", 205 + 150, 555 + 18, 30)

        if btn.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
            pygame.mouse.set_cursor((8, 8), (4, 4), (24, 24, 24, 231, 231, 24, 24, 24), (0, 0, 0, 0, 0, 0, 0, 0))
            pygame.draw.rect(gameDisplay, bright_green, (205, 555, 290, 30))
            message_btn("?ץימא קיפסמ היהי ימ", 205 + 150, 555 + 18, 30)
        else:
            pygame.mouse.set_cursor((16, 19), (0, 0), (
                128, 0, 192, 0, 160, 0, 144, 0, 136, 0, 132, 0, 130, 0, 129, 0, 128, 128, 128, 64, 128, 32, 128, 16,
                129,
                240, 137, 0, 148, 128, 164, 128, 194, 64, 2, 64, 1, 128), (
                                        128, 0, 192, 0, 224, 0, 240, 0, 248, 0, 252, 0, 254, 0, 255, 0, 255, 128, 255,
                                        192,
                                        255, 224, 255, 240, 255, 240, 255, 0, 247, 128, 231, 128, 195, 192, 3, 192, 1,
                                        128))

        pygame.display.update()
        clock.tick(60)
    while level == 1:  # סרטון מעבר
        video_play(resource_path('Shvetz_1.mp4'), 0, 2, resource_path('Shvetz_1.wav'))

    while level == 2:  # להרוג את סבתא
        level_2(-2)

    while level == 3:  # סרטון מעבר - השתלטות על השרביט
        video_play(resource_path('Shvetz_2.mp4'), 0, 4, resource_path('Shvetz_2.wav'))

    while level == 4:  # משחק כלשהו
        explain_window(4)
        level_4()

    while level == 5:  # סרטון כלשהו
        video_play(resource_path('Shvetz_tit.mp4'), 0, 6, resource_path('Shvetz_tit.wav'))

    while level == 6:  # הבצורת
        explain_window(6)
        level_6()

    while level == 7:  # סרטון קובה
        video_play(resource_path('Shvetz_kube.mp4'), 1, 8, resource_path('Shvetz_kube.wav'))

    while level == 8:
        Credits()

    pygame.quit()
    quit()


#######
intro(0)

# level_1(-2)


###############################################
# oo = [obj(obj_startx, obj_starty, obj_width, obj_height, black), obj(obj_startx2, obj_starty2, obj_width, obj_height, green)]

# if obj_starty2 > display_height:
#   obj_starty = 0 - obj_height
#   obj_startx = random.randrange(0, display_width)

# for element in obst:
#  if element.collidepoint((x, y)) or element.collidepoint((x, y + car_height)) or element.collidepoint((x + car_width, y)) or element.collidepoint((x + car_width, y + car_height)):
#       crash()
"""
def countdown():
    global my_timer
    my_timer = 40
    text_time(my_timer)
    for x in range(40):
        my_timer = my_timer - 1
        pygame.time.delay(60)
        text_time(my_timer)
    level_try(-1)
"""
"""countdown_thread = threading.Thread(target = countdown)
countdown_thread.start()"""
