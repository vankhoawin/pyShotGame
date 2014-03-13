# gameLogic.py

'''
-----THINGS TO FIX-----





'''


import sys
import math

import gui

from random import randint
from initialVariables import *
from pygame.locals import *

from player      import Player

from shot        import Shot
from shot_basic  import Shot_Basic
from shot_double import Shot_Double
from shot_cone   import Shot_Cone

from powerup        import Powerup
from powerup_double import Powerup_Double
from powerup_cone   import Powerup_Cone

from monster     import Monster
from zombie      import Zombie
from ghoul       import Ghoul
from abomination import Abomination
from bat         import Bat




pygame.init()

# GAME CLOCK
run = True
clock = pygame.time.Clock()

# INITIAL VARIABLES
keyX, keyY = SCREEN_DIMENSIONS_X//2 , SCREEN_DIMENSIONS_Y//2
moveX, moveY = 0, 0
shot_type = 'BASIC'
shot_timer = 0

objects = set()

p_timer_on = True
timer_on   = True
fps_on     = True
kills_on   = True
pause      = False
kill_count = 0



def get_key_c():
    return (keyX + mouse_c.get_width()//2,
            keyY + mouse_c.get_height()//2)


#CREATES THE PLAYER
p = Player(get_key_c()[0], get_key_c()[1])
objects.add(p)


def get_mouse_c():
    return (pygame.mouse.get_pos())
    

def check_key():
    global moveX, moveY, p_timer_on, timer_on, fps_on, kills_on, pause
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_w:
                moveY -= PLAYER_MOVE_SPEED
            elif event.key == K_s:
                moveY += PLAYER_MOVE_SPEED
            elif event.key == K_a:
                moveX -= PLAYER_MOVE_SPEED
            elif event.key == K_d:
                moveX += PLAYER_MOVE_SPEED
            # DEBUGGING
            elif event.key == K_1:
                p_timer_on = not p_timer_on
            elif event.key == K_2:
                timer_on = not timer_on
            elif event.key == K_3:
                fps_on = not fps_on
            elif event.key == K_4:
                kills_on = not kills_on
            elif event.key == K_z:
                create_powerup('Double')
            elif event.key == K_x:
                create_powerup('Cone')
            elif event.key == K_v:
                objects.add(Zombie(get_mouse_c()[0],get_mouse_c()[1]))
            elif event.key == K_b:
                objects.add(Ghoul(get_mouse_c()[0],get_mouse_c()[1]))
            elif event.key == K_n:
                objects.add(Abomination(get_mouse_c()[0],get_mouse_c()[1]))
            elif event.key == K_m:
                objects.add(Bat(get_mouse_c()[0],get_mouse_c()[1]))
            elif event.key == K_p:
                pause = not pause
                    
        elif event.type == KEYUP:
            if event.key == K_w or event.key == K_s:
                moveY = 0
            elif event.key == K_a or event.key == K_d:
                moveX = 0
                
        elif event.type == MOUSEBUTTONDOWN:
            angle = angle_between_points(p.get_location(),get_mouse_c())
            
            if shot_type == 'BASIC':
                shot = Shot_Basic(p.get_x(),p.get_y(),angle,seconds)
                objects.add(shot)
                
            elif shot_type == 'DOUBLE':
                shot1 = Shot_Double(p.get_x()+25*math.cos(angle),
                                    p.get_y()-25*math.sin(angle),
                                    angle,seconds)
                shot2 = Shot_Double(p.get_x()-25*math.cos(angle),
                                    p.get_y()+25*math.sin(angle),
                                    angle,seconds)
                
                objects.add(shot1)
                objects.add(shot2)
                
            elif shot_type == 'CONE':
                shot1 = Shot_Cone(p.get_x(),p.get_y(),
                                  angle*(1-SHOT_CONE_SPREAD),seconds)
                shot2 = Shot_Cone(p.get_x(),p.get_y(),
                                  angle*(1+SHOT_CONE_SPREAD),seconds)
                shot3 = Shot_Cone(p.get_x(),p.get_y(),
                                  angle,seconds)
                
                objects.add(shot1)
                objects.add(shot2)
                objects.add(shot3)
            

    p.change_x(moveX)
    p.change_y(moveY)
    check_boundaries()



def check_boundaries():
    global keyX, keyY
    x = mouse_c.get_width()//2
    y = mouse_c.get_width()//2
    
    if p.get_x() < x:
        p.set_x(x)
    elif p.get_x()> SCREEN_DIMENSIONS_X-x:
        p.set_x(SCREEN_DIMENSIONS_X-x)
    if p.get_y() < y:
        p.set_y(y)
    elif p.get_y() > SCREEN_DIMENSIONS_Y-y:
        p.set_y(SCREEN_DIMENSIONS_Y-y)


def check_shot_boundaries(s):
    if s._x < 0 or                   \
       s._x > SCREEN_DIMENSIONS_X or \
       s._y < 0 or                   \
       s._y > SCREEN_DIMENSIONS_Y:
        objects.remove(s)


def create_powerup(p):
    eval('objects.add(Powerup_{}(randint(SCREEN_DIMENSIONS_X*.1, SCREEN_DIMENSIONS_X*.9),\
                        randint(SCREEN_DIMENSIONS_Y*.1, SCREEN_DIMENSIONS_Y*.9), \
                        seconds))'.format(p))

def pickup_powerup(p):
    global shot_type, shot_timer
    shot_type = p
    shot_timer = seconds

def check_power_timer(p):
    global shot_timer
    timer = eval('SHOT_{}_TIMER'.format(p))
    if seconds - shot_timer >= timer:
        global shot_type
        shot_type = 'BASIC'
        shot_timer = 0

def create_monster():
    def _pick_monster(m):
        side = randint(1, 4)
        
        if side == 1: #left
                pos = (0, randint(0, SCREEN_DIMENSIONS_Y))
        elif side == 2: #top
                pos = (randint(0, SCREEN_DIMENSIONS_X), 0)
        elif side == 3: #right
                pos = (SCREEN_DIMENSIONS_X, randint(0, SCREEN_DIMENSIONS_Y))
        else: #bot
                pos = (randint(0, SCREEN_DIMENSIONS_X), SCREEN_DIMENSIONS_Y)
        
        eval('objects.add({}(pos[0], pos[1]))'.format(m))

    def _spawn_conditions(m, spawn_chance):
        return eval('spawn_chance<{0}_SPAWN_RATE and seconds>{0}_SPAWN_DELAY'.format(m))

    # MONSTER TEST ON/OFF
    #spawn_chance = 10000
    spawn_chance = randint(1, 10000)

    # MONSTER SPAWNS
    
    if _spawn_conditions('ZOMBIE',spawn_chance):
        _pick_monster('Zombie')
        
    if _spawn_conditions('GHOUL',spawn_chance):
        _pick_monster('Ghoul')

    if _spawn_conditions('ABOM',spawn_chance):
        _pick_monster('Abomination')

    if _spawn_conditions('BAT',spawn_chance):
        _pick_monster('Bat')
    
    # POWERUP SPAWNS
    
    check_power = sum([isinstance(o, Powerup) for o in objects])
    if not check_power and shot_type == 'BASIC':
        if spawn_chance < POWERUP_CONE_SPAWN_RATE:
            create_powerup('Cone')
        elif spawn_chance < POWERUP_DOUBLE_SPAWN_RATE:
            create_powerup('Double')

def angle_between_points(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return math.atan2(y,x) - math.pi

def update_objects():
    if shot_type != 'BASIC':
        check_power_timer(shot_type)
        
    for o in objects.copy():
        o.update()
        o.display()
            
        if isinstance(o, Monster):
            update_monster(o)
            shot_list = [s for s in objects if isinstance(s, Shot)]
            
            for s in shot_list:
                if o.contains(s):
                    remove_monster(o)
                    objects.remove(s)
            if o.contains(p):
                end_game()

        elif isinstance(o, Shot):            
            if o in objects:
                if o.timer_expire(pygame.time.get_ticks()/1000):
                    objects.remove(o)
                else:
                    check_shot_boundaries(o)
            
        elif isinstance(o, Powerup):
            if o.contains(p):
                pickup_powerup(o.get_type())
                objects.remove(o)
            elif o.timer_expire(seconds):
                objects.remove(o)              

def update_monster(m):
    monster_angle = angle_between_points(m.get_location(), p.get_location())
    m.change_angle(monster_angle)

def remove_monster(m):
    m.damage_hp()
    if m.get_hp() == 0:
        objects.remove(m)
        global kill_count
        kill_count += 1

def display_powerup_timer():
    if p_timer_on and shot_type != 'BASIC':
        p_timeFont = pygame.font.SysFont("bold", P_TIMER_FONT_SIZE)
        p_timeDisplay = p_timeFont.render(str(eval('SHOT_{}_TIMER'.format(shot_type))-
                                          (seconds-shot_timer)),1,P_TIMER_FONT_COLOR)
        screen.blit(p_timeDisplay, (p.get_x()-P_TIMER_X,
                                    p.get_y()+P_TIMER_Y))

def display_timer():
    if timer_on:
        timeFont = pygame.font.SysFont("bold", TIMER_FONT_SIZE)
        timeDisplay = timeFont.render(str(seconds), 1, TIMER_FONT_COLOR)
        screen.blit(timeDisplay, (SCREEN_DIMENSIONS_X//2,
                                  SCREEN_DIMENSIONS_Y*.1))

def display_fps():
    if fps_on:
        fpsFont = pygame.font.SysFont("bold", FPS_FONT_SIZE)
        fpsDisplay = fpsFont.render(str(clock.get_fps()), 1, FPS_FONT_COLOR)
        screen.blit(fpsDisplay, (SCREEN_DIMENSIONS_X*.9,
                                 SCREEN_DIMENSIONS_Y*.1))

def display_kills():
    if kills_on:
        killsFont = pygame.font.SysFont("bold", KILLS_FONT_SIZE)
        killsDisplay = killsFont.render("Kills: "+str(kill_count), 1, KILLS_FONT_COLOR)
        screen.blit(killsDisplay, (SCREEN_DIMENSIONS_X*.1,
                                   SCREEN_DIMENSIONS_Y*.1))
    
def end_game():
    global run
    
    screen.fill(ENDGAME_BG_COLOR)
    endFont = pygame.font.SysFont("bold", ENDGAME_FONT_SIZE)
    endDisplay = endFont.render("GAME OVER", 1, ENDGAME_FONT_COLOR)
    screen.blit(endDisplay, (SCREEN_DIMENSIONS_X//2 - ENDGAME_FONT_SIZE*2,
                             SCREEN_DIMENSIONS_Y*.25))
    
    run = False
    


while run:
    #uncomment for custom background
    #screen.blit(background, (0,0))
    screen.fill(SCREEN_BG_COLOR)
    
    check_key()
    if not pause:
        global seconds
        seconds = pygame.time.get_ticks()//1000
        
        create_monster()
        update_objects()
        
        display_timer()
        display_fps()
        display_kills()
        display_powerup_timer()
        
        pygame.display.update()

        clock.tick(CLOCK_TICK)
        
pygame.time.wait(3000)
pygame.quit()
sys.exit()
