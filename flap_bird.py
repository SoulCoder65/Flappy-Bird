import pygame
import random
from pygame.locals import *
pygame.init()
pygame.mixer.init()


#GLOBALS VARIALS DECLARATION
SCREEN_WIDTH=289
SCREEN_HIGHT=511
FPS=45
CLOCK=pygame.time.Clock()
GAME_SPIRTES={}
GAME_MUSIC={}
GROUNDY=SCREEN_HIGHT*0.8

#IMAGES MANIPULATION
img_width=30
img_height=30
zero_img=pygame.image.load("/home/akshay/Downloads/PYTHON/images/flappy_birds_images/0-Number-PNG.png")
zero_img=pygame.transform.scale(zero_img,(img_width,img_height))
one_img=pygame.image.load("/home/akshay/Downloads/PYTHON/images/flappy_birds_images/1-Number-PNG.png")
one_img=pygame.transform.scale(one_img,(img_width,img_height))
two_img=pygame.image.load("/home/akshay/Downloads/PYTHON/images/flappy_birds_images/2-Number-PNG.png")
two_img=pygame.transform.scale(two_img,(img_width,img_height))
three_img=pygame.image.load("/home/akshay/Downloads/PYTHON/images/flappy_birds_images/3-Number-PNG.png")
three_img=pygame.transform.scale(three_img,(img_width,img_height))
four_img=pygame.image.load("/home/akshay/Downloads/PYTHON/images/flappy_birds_images/4-Number-PNG.png")
four_img=pygame.transform.scale(four_img,(img_width,img_height))
five_img=pygame.image.load("/home/akshay/Downloads/PYTHON/images/flappy_birds_images/5-Number-PNG.png")
five_img=pygame.transform.scale(five_img,(img_width,img_height))
six_img=pygame.image.load("/home/akshay/Downloads/PYTHON/images/flappy_birds_images/6-Number-PNG.png")
six_img=pygame.transform.scale(six_img,(img_width,img_height))
seven_img=pygame.image.load("/home/akshay/Downloads/PYTHON/images/flappy_birds_images/7-Number-PNG.png")
seven_img=pygame.transform.scale(seven_img,(img_width,img_height))
eight_img=pygame.image.load("/home/akshay/Downloads/PYTHON/images/flappy_birds_images/8-Number-PNG.png")
eight_img=pygame.transform.scale(eight_img,(img_width,img_height))
nine_img=pygame.image.load("/home/akshay/Downloads/PYTHON/images/flappy_birds_images/9-Number-PNG.png")
nine_img=pygame.transform.scale(nine_img,(img_width,img_height))



#GAME SPIRTES

GAME_SPIRTES['background']=pygame.image.load('/home/akshay/Downloads/PYTHON/images/flappy_birds_images/background-day.png')
GAME_SPIRTES['bird']=pygame.image.load('/home/akshay/Downloads/PYTHON/images/flappy_birds_images/bluebird-downflap.png')
GAME_SPIRTES['pipe_down']=pygame.image.load('/home/akshay/Downloads/PYTHON/images/flappy_birds_images/pipegreen.png')
GAME_SPIRTES['pipe_up']=pygame.transform.rotate(GAME_SPIRTES['pipe_down'],180)
GAME_SPIRTES['base']=pygame.image.load('/home/akshay/Downloads/PYTHON/images/flappy_birds_images/base.png')
GAME_SPIRTES['game_icon']=pygame.image.load('/home/akshay/Downloads/PYTHON/images/flappy_birds_images/game_icon.png')
GAME_SPIRTES['name_icon']=pygame.image.load('/home/akshay/Downloads/PYTHON/images/flappy_birds_images/my_name_logo.png')
GAME_SPIRTES['enter_to_play']=pygame.image.load('/home/akshay/Downloads/PYTHON/images/flappy_birds_images/enter_to_play.png')
GAME_SPIRTES['game_over']=pygame.image.load('/home/akshay/Downloads/PYTHON/images/flappy_birds_images/gameover.png')
GAME_SPIRTES['score']=(
    zero_img,one_img,two_img,three_img,four_img,five_img,six_img,seven_img,eight_img,nine_img
)

#FLAPPYBIRD MUSIC
die="/home/akshay/Downloads/PYTHON/audios/flappybirds_music/sfx_die.wav"
hit="/home/akshay/Downloads/PYTHON/audios/flappybirds_music/sfx_hit.wav"
point="/home/akshay/Downloads/PYTHON/audios/flappybirds_music/sfx_point.wav"
wing="/home/akshay/Downloads/PYTHON/audios/flappybirds_music/sfx_wing.wav"
swoosh="/home/akshay/Downloads/PYTHON/audios/flappybirds_music/sfx_swooshing.wav"

#WINDOW LOOK
SCREEN=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HIGHT])
pygame.display.set_caption("FLAPPY BIRD BY AKSHAY")
pygame.display.update()
pygame.display.update()

#FUN FOR GENERATING RANDOM PIPES
def random_pipes():
    offset=SCREEN_WIDTH/3
    y2=offset+random.randrange(0,int(SCREEN_HIGHT-GAME_SPIRTES['base'].get_height()-1.2*offset))
    x=SCREEN_WIDTH+30
    y1=GAME_SPIRTES['pipe_up'].get_height()-y2+offset
    pipe=[
        {'x':x,'y':-y1},
        {'x':x,'y':y2}
    ]
    return pipe
#GAME OVER SCREEN
def gameover_screen():
    game_exit1=False
    while not game_exit1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_exit1=True
                exit()
            SCREEN.blit(GAME_SPIRTES['background'], (0, 0))
            SCREEN.blit(GAME_SPIRTES['base'], (0, 400))
            bcicon = pygame.image.load("/home/akshay/Downloads/PYTHON/images/flappy_birds_images/gameover.png")
            bcicon = pygame.transform.scale(bcicon, (200, 230)).convert_alpha()
            menulogo = pygame.image.load("/home/akshay/Downloads/PYTHON/images/flappy_birds_images/menu_screen_logo.png")
            menulogo = pygame.transform.scale(menulogo, (250, 250)).convert_alpha()
            SCREEN.blit(menulogo, (40, 180))

            SCREEN.blit(bcicon, (70, 248))
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_KP_ENTER or event.key==pygame.K_TAB or event.key==pygame.K_TAB:
                    menu_screen()
        pygame.display.update()
        CLOCK.tick(FPS)

#FUNCTION WHICH CHECK GAMEOVER
def game0ver(bird_x,bird_y,UPPERPIPESLIST,LOWERPIPESLIST):
    if bird_y>GROUNDY-25 or bird_y<0:
        pygame.mixer.music.load(point)
        pygame.mixer.music.play()
        pygame.mixer.music.load(die)
        pygame.mixer.music.play()
        return True
    for pipe in UPPERPIPESLIST:
        pipeHeight = GAME_SPIRTES['pipe_up'].get_height()
        if (bird_y < pipeHeight + pipe['y']-20 and abs(bird_x - pipe['x']) < GAME_SPIRTES['pipe_up'].get_width()-20):
            pygame.mixer.music.load(point)
            pygame.mixer.music.play()
            pygame.mixer.music.load(die)
            pygame.mixer.music.play()
            return True
    for pipe in LOWERPIPESLIST:
        if (bird_y + GAME_SPIRTES['bird'].get_height() > pipe['y']+20) and abs(bird_x - pipe['x'])+20    < GAME_SPIRTES['pipe_up'].get_width():
            pygame.mixer.music.load(point)
            pygame.mixer.music.play()
            pygame.mixer.music.load(die)
            pygame.mixer.music.play()
            return True

#MENU  WINDOW FUNCTION
def menu_screen():
    exit_menu=False
    while not exit_menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_menu=True
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE or event.key==pygame.K_TAB or event.key==pygame.K_ENTER:
                    game_screen()
        SCREEN.blit(GAME_SPIRTES['background'],(0,0))
        SCREEN.blit(GAME_SPIRTES['base'], (0, 400))
        #SCREEN.blit(GAME_SPIRTES['name_icon'], (100, 350))

        gameicon = pygame.image.load("/home/akshay/Downloads/PYTHON/images/flappy_birds_images/game_icon.png")
        gameicon = pygame.transform.scale(gameicon, (200, 230)).convert_alpha()
        SCREEN.blit(gameicon, (70, 248))
        extra_bird1icon = pygame.image.load("/home/akshay/Downloads/PYTHON/images/flappy_birds_images/bird.png")
        extra_bird1icon = pygame.transform.scale(extra_bird1icon, (80, 90)).convert_alpha()
        SCREEN.blit(extra_bird1icon,(30,300))
        #bcicon = pygame.image.load("/home/akshay/Downloads/PYTHON/images/flappy_birds_images/enter_to_play.png")
        #bcicon = pygame.transform.scale(bcicon, (200, 230)).convert_alpha()
        #SCREEN.blit(bcicon, (70, 70))
        menulogo = pygame.image.load("/home/akshay/Downloads/PYTHON/images/flappy_birds_images/menu_screen_logo.png")
        menulogo = pygame.transform.scale(menulogo, (250, 250)).convert_alpha()
        SCREEN.blit(menulogo,(20,10))
        pygame.display.update()
        CLOCK.tick(FPS)


def game_screen():
    bird_x = 50
    bird_y = 100

    # BOOLEAN VARIABLES DECLARATION
    exit_game = False
    while not exit_game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
                exit()
        pipe1 = random_pipes()
        pipe2 = random_pipes()
        UPPERPIPESLIST=[
            {'x':SCREEN_WIDTH+200,'y':pipe1[0]['y']},
            {'x':SCREEN_WIDTH+200+(SCREEN_WIDTH/2),'y':pipe2[0]['y']}
        ]
        LOWERPIPELIST=[
            {'x':SCREEN_WIDTH+200,'y':pipe1[1]['y']},
            {'x':SCREEN_WIDTH+200+(SCREEN_WIDTH+200/2),'y':pipe2[1]['y']}
        ]
        #VELOCITIES
        pipeVE = -4
        playerVeloY=-8
        playerMAXvel=10
        playerMINvel=-9
        playeACCEV=1
        SCORE = 0

        playerFlap=-9
        isplayerFlap=False

        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                    exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE or event.key==pygame.K_UP:
                        if bird_y>0:
                            playerVeloY=playerFlap
                            isplayerFlap==True
                            pygame.mixer.music.load(wing)
                            pygame.mixer.music.play()

            for upper,lower in zip(UPPERPIPESLIST,LOWERPIPELIST):
                upper['x']+=pipeVE
                lower['x']+=pipeVE

            if 0<UPPERPIPESLIST[0]['x']<5:
                newpipe=random_pipes()
                UPPERPIPESLIST.append(newpipe[0])
                LOWERPIPELIST.append(newpipe[1])

            if UPPERPIPESLIST[0]['x'] < -GAME_SPIRTES['pipe_up'].get_width():
                UPPERPIPESLIST.pop(0)
                LOWERPIPELIST.pop(0)

            SCREEN.blit(GAME_SPIRTES['background'], (0, 0))
            for upper, lower in zip(UPPERPIPESLIST, LOWERPIPELIST):
                SCREEN.blit(GAME_SPIRTES['pipe_up'], ((upper['x'],upper['y'])))
                SCREEN.blit(GAME_SPIRTES['pipe_down'], (lower['x'],lower['y']))
            SCREEN.blit(GAME_SPIRTES['bird'],(bird_x,bird_y))
            SCREEN.blit(GAME_SPIRTES['base'], (0, 400))
            crash = game0ver(bird_x, bird_y, UPPERPIPESLIST, LOWERPIPELIST)
            if crash:
                pygame.mixer.music.load(hit)
                pygame.mixer.music.play()
                gameover_screen()
                return

            #CHECK SCORE
            midbird_x=bird_x+GAME_SPIRTES['bird'].get_width()/2
            for pipe in UPPERPIPESLIST:
                pipemid=pipe['x']+GAME_SPIRTES['pipe_up'].get_width()/2
                if pipemid<=midbird_x<pipemid+4:
                    SCORE+=1
                    pygame.mixer.music.load("/home/akshay/Downloads/PYTHON/audios/flappybirds_music/sfx_point.wav")
                    pygame.mixer.music.play()
            score_list=[int(x) for x in list(str(SCORE))]
            width=0
            for digit in score_list:
                width+=GAME_SPIRTES['score'][digit].get_width()
            Xoffset = (SCREEN_WIDTH - width) / 2

            for digit in score_list:
                SCREEN.blit(GAME_SPIRTES['score'][digit], (Xoffset, SCREEN_HIGHT * 0.12))
                Xoffset += GAME_SPIRTES['score'][digit].get_width()
            if playerVeloY < playerMAXvel and not isplayerFlap:
                playerVeloY += playeACCEV
            if isplayerFlap:
                isplayerFlap = False
            playerheight = GAME_SPIRTES['bird'].get_height()
            bird_y = bird_y + min(playerVeloY, GROUNDY - bird_y - playerheight)

            pygame.display.update()
            CLOCK.tick(FPS)
menu_screen()