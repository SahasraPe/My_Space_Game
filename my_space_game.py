# SEV Advanced - Introduction to Game Development
# start your game code here!    

import pgzrun
import random 

WIDTH = 1000
HEIGHT = 600
SCOREBOX_HEIGHT = 50

score = 0
junk_speed = 10
SATELLITE_SPEED = 3
debris_speed = 4
laser_speed = -5

BACKGROUND_IMG = "space_game_background"
PLAYER_IMG = "satellite2"
JUNK_IMG = "spacejunk"
SATELLITE_IMG = "satellite"
DEBRIS_IMG = "tesla_roadster"
LASER_IMG = "laser_red"

player = Actor(PLAYER_IMG)
player.midright = (WIDTH, HEIGHT/2)

junks = [ ]
for i in range (5):
    junk = Actor(JUNK_IMG)
    x_pos = random.randint(-500, -50)
    y_pos = random.randint(SCOREBOX_HEIGHT, HEIGHT-junk.height)
    junk.topleft = (x_pos, y_pos)
    junks.append(junk)

satellite = Actor(SATELLITE_IMG)
x_sat = random.randint(-500, -50)
y_sat = random.randint(SCOREBOX_HEIGHT, HEIGHT - satellite.height)
satellite.topright = (x_sat, y_sat)

debris = Actor(DEBRIS_IMG)
x_deb = random.randint(-500, -50)
y_deb = random.randint(SCOREBOX_HEIGHT, HEIGHT - debris.height)
debris.topright = (x_deb, y_deb) 

lasers = [ ]


def update() :
    updatePlayer()
    updateJunk()
    updateSatellite()
    updateDebris()
    updateLasers()
    
def draw() :
    screen.clear()  
    screen.blit(BACKGROUND_IMG, (0,0))
    player.draw()
    for junk in junks:
        junk.draw()
    satellite.draw()
    debris.draw()
    for laser in lasers:
        laser.draw()

    show_score = "Score: " + str(score)
    screen.draw.text(show_score, topleft=(750,15), fontsize=35, color="white")
    

    
def updatePlayer() :    
    if keyboard.UP == 1:
        player.y +=  -5
    elif keyboard. DOWN == 1:
        player.y +=  5
            
    if player.top < SCOREBOX_HEIGHT:

        player.top = SCOREBOX_HEIGHT
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
        
    if keyboard.space == 1:
        laser = Actor(LASER_IMG)
        laser.midright = (player.midleft)
        fireLasers(laser)

def updateJunk():
    global score, junk_speed
    for junk in junks:
        junk.x += junk_speed

        collision = player.colliderect(junk)
        if junk.left > WIDTH or collision == 1:
            junk.right = 0
            x_pos = -50
            y_pos = random.randint(SCOREBOX_HEIGHT, HEIGHT-junk.height)
            junk.topleft = (x_pos, y_pos)

            if collision == 1:
                score += 1
                sounds.collect_pep.play()

def updateSatellite():
    global score
    satellite.x += SATELLITE_SPEED

    collision = player.colliderect(satellite)
    if satellite.left > WIDTH or collision == 1:
        x_sat = random.randint(-500, -50)
        y_sat = random.randint(SCOREBOX_HEIGHT, HEIGHT - satellite.height)
        satellite.topright = (x_sat, y_sat)

        if collision == 1:
            score += -5
            sounds.explosion.play()

def updateDebris():
    global score
    debris.x += debris_speed

    collision = player.colliderect(debris)
    if debris.left > WIDTH or collision == 1:
        x_deb = random.randint(-500, -50)
        y_deb = random.randint(SCOREBOX_HEIGHT, HEIGHT - debris.height)
        debris.topright = (x_deb, y_deb)

    if collision == 1:
        score += -5

def updateLasers():
    global score
    for laser in lasers:  # for each item in lasers list
        laser.x += laser_speed

        collision_sat = satellite.colliderect(laser)
        collision_deb = debris.colliderect(laser)

        # remove laser
        if laser.right < 0 or collision_sat == 1 or collision_deb == 1:
            lasers.remove(laser)

        # if collisions occur
        if collision_sat == 1:
            x_sat = random.randint(-500, -50)
            y_sat = random.randint(SCOREBOX_HEIGHT, HEIGHT - satellite.height)
            satellite.topright = (x_sat, y_sat)
            score += -5
            sounds.explosion.play()
        if collision_deb == 1:
            x_deb = random.randint(-500, -50)
            y_deb = random.randint(SCOREBOX_HEIGHT, HEIGHT - debris.height)
            debris.topright = (x_deb, y_deb)
            score += 5
            
        # if collisions occur
        if collision_sat == 1:
            x_sat = random.randint(-500, -50)
            y_sat = random.randint(SCOREBOX_HEIGHT, HEIGHT - satellite.height)
            satellite.topright = (x_sat, y_sat)
            score += -5
            sounds.explosion.play()
        if collision_deb == 1:
            x_deb = random.randint(-500, -50)
            y_deb = random.randint(SCOREBOX_HEIGHT, HEIGHT - debris.height)
            debris.topright = (x_deb, y_deb)
            score += 5

player.laserActive = 1     
def makeLaserActive():  
    global player
    player.laserActive = 1 
 
   

def fireLasers(laser):
    if player.laserActive == 1:  
        player.laserActive = 0
        clock.schedule(makeLaserActive, 0.2)  
        sounds.laserfire02.play()  
        lasers.append(laser) 
        

pgzrun.go()
