from microbit import *
import music
music.set_tempo(bpm = 550)
playerx = 2
bullety = 3
bulletx = 0
bulletcreate = False
bulletop = 9
int = 0
starttime = running_time()
start = running_time()
wave = 0
wavestart = False
alienInt = 0
aliencap = False
startscreen = True
alienpic = Image("90009:""09990:""90909:""99999:""90909")

x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0
y1 = 0
y2 = 0
y3 = 0
y4 = 0
y5 = 0
y6 = 0

al1 = False
al2 = False
al3 = False
al4 = False
al5 = False
al6 = False

op1 = 0
op2 = 0
op3 = 0
op4 = 0
op5 = 0
op6 = 0

def playermove():
    global playerx
    display.set_pixel(playerx, 4, 9)
    if button_a.was_pressed():
       music.play('g4', wait = False)
       playerx -= 1
       if playerx < 0:
            playerx = 0
    if button_b.was_pressed():
       music.play('g4', wait = False)
       playerx += 1
       if playerx > 4:
           playerx = 4
def bulletmake():
    global bulletx
    global bullety
    global starttime
    global bulletcreate
    global bulletop
    global int
    global bulletswitch
    display.set_pixel(bulletx, bullety, bulletop)
    if running_time() - starttime  > 200:
        int += 1
        if bullety > 0:
            bullety -= 1
            bulletop = 9
            display.set_pixel(bulletx, bullety, bulletop)
        starttime = running_time()
    if int > 4:
        bulletop = 0
        bullety = 4
        bulletcreate = False
        int = 0
while True:
    if startscreen == False:
        #collisions
        if bulletx == x1 and bullety == y1 and bulletcreate == True:
            music.play(music.JUMP_UP, wait = False)
            op1 = 0
            x1 = 0
            y1 = 0
            al1 = False
        if bulletx == x2 and bullety == y2 and bulletcreate == True:
            music.play(music.JUMP_UP, wait = False)
            op2 = 0
            x2 = 0
            y2 = 0
            al2 = False
        if bulletx == x3 and bullety == y3 and bulletcreate == True:
            music.play(music.JUMP_UP, wait = False)
            op3 = 0
            x3 = 0
            y3 = 0
            al3 = False
        if bulletx == x4 and bullety == y4 and bulletcreate == True:
            music.play(music.JUMP_UP, wait = False)
            op4 = 0
            x4 = 0
            y4 = 0
            al1 = False
        if bulletx == x5 and bullety == y5 and bulletcreate == True:
            music.play(music.JUMP_UP, wait = False)
            op5 = 0
            x5 = 0
            y5 = 0
            al5 = False
        if bulletx == x6 and bullety == y6 and bulletcreate == True:
            music.play(music.JUMP_UP, wait = False)
            op6 = 0
            x6 = 0
            y6 = 0
            al6 = False
        display.clear()
        display.set_pixel(x1, y1, op1)
        display.set_pixel(x2, y2, op2)
        display.set_pixel(x3, y3, op3)
        display.set_pixel(x4, y4, op4)
        display.set_pixel(x5, y5, op5)
        display.set_pixel(x6, y6, op6)
        playermove()
        if running_time() - starttime  > 1000:
            if al1 == True:
                op1 = 9
                if x1 == 4:
                    x1 = -1
                    y1 += 1
                if y1 == 4:
                    music.play(music.POWER_DOWN)
                    reset()
                x1 += 1
            if al2 == True:
                op2 = 9
                if x2 == 4:
                    x2 = -1
                    y2 += 1
                if y2 == 4:
                    music.play(music.POWER_DOWN)
                    reset()
                x2 += 1
            if al3 == True:
                op3 = 9
                if x3 == 4:
                    x3 = -1
                    y3 += 1
                if y3 == 4:
                    music.play(music.POWER_DOWN)
                    reset()
                x3 += 1
            if al4 == True:
                op4 = 9
                if x4 == 4:
                    x4 = -1
                    y4 += 1
                if y4 == 4:
                    music.play(music.POWER_DOWN)
                    reset()
                x4 += 1
            if al5 == True:
                op5 = 9
                if x5 == 4:
                    x5 = -1
                    y5 += 1
                if y5 == 4:
                    music.play(music.POWER_DOWN)
                    reset()
                x5 += 1
            if al6 == True:
                op6 = 9
                if x6 == 4:
                    x6 = -1
                    y6 += 1
                if y6 == 4:
                    music.play(music.POWER_DOWN)
                    reset()
                x6 += 1
            if aliencap != True:
                alienInt += 0.5
                print(alienInt)
            print(wave)
            starttime = running_time()
        if accelerometer.was_gesture('shake'):
            music.play('c5', wait = False)
            bulletcreate = True
            bulletx = playerx
            bullety = 4
        if bulletcreate == True:
            bulletmake()
        if wave == 0:
            if alienInt == 0.5:
                wavestart = True
                al1 = True
            if alienInt == 1.5:
                al2 = True
            if alienInt == 2.5:
                al3 = True
                alienInt += 0.5
                aliencap = True
            if al1 == False and al2 == False and al3 == False and wavestart == True:
                music.play(music.POWER_UP, wait = False)
                wave = 1
                alienInt = 0
                aliencap = False
                wavestart = False    
        if wave == 1:
            if alienInt == 0.5:
                wavestart = True
                al1 = True
            if alienInt == 1.5:
                al2 = True
            if alienInt == 2.5:
                al3 = True
            if alienInt == 3.5:
                al4 = True
            if alienInt == 4.5:
                al5 = True
                alienInt += 0.5
                aliencap = True
            if al1 == False and al2 == False and al3 == False and al4 == False and al5 == False and wavestart == True:
                music.play(music.ENTERTAINER)
                wave = 2
                alienInt = 0
                aliencap = False
                wavestart = False 
        if wave == 2:
            if alienInt == 0.5:
                wavestart = True
                al1 = True
            if alienInt == 1.5:
                al2 = True
            if alienInt == 2.5:
                al3 = True
            if alienInt == 3.5:
                al4 = True
            if alienInt == 3.5:
                al5 = True
            if alienInt == 4.5:
                al6 = True
                alienInt += 0.5
                aliencap = True
            if al1 == False and al2 == False and al3 == False and al4 == False and al5 == False and al6 == False and wavestart == True:
                music.play(music.ENTERTAINER)
                wave = 3
                alienInt = 0
                aliencap = False
                wavestart = False 
        if wave == 3:
            if alienInt == 0.5:
                wavestart = True
                al1 = True
            if alienInt == 1:
                al2 = True
            if alienInt == 1.5:
                al3 = True
            if alienInt == 2:
                al4 = True
            if alienInt == 2.5:
                al5 = True
                alienInt += 0.5
                aliencap = True
            if al1 == False and al2 == False and al3 == False and al4 == False and al5 == False and wavestart == True:
                music.play(music.ENTERTAINER)
                wave = 4
                alienInt = 0
                aliencap = False
                wavestart = False 
        if wave == 4:
            if alienInt == 0.5:
                wavestart = True
                al1 = True
            if alienInt == 1:
                al2 = True
            if alienInt == 1.5:
                al3 = True
            if alienInt == 2.5:
                al4 = True
            if alienInt == 3.5:
                al5 = True
            if alienInt == 4.5:
                al6 = True
                alienInt += 0.5
                aliencap = True
            if al1 == False and al2 == False and al3 == False and al4 == False and al5 == False and al6 == False and wavestart == True:
                music.play(music.ENTERTAINER)
                wave = 5
                alienInt = 0
                aliencap = False
                wavestart = False 
        if wave == 5:
            if alienInt == 0.5:
                wavestart = True
                al1 = True
            if alienInt == 1:
                al2 = True
            if alienInt == 1.5:
                al3 = True
            if alienInt == 2:
                al4 = True
            if alienInt == 2.5:
                al5 = True
            if alienInt == 3:
                al6 = True
            if alienInt == 4:
                al7 = True
            if alienInt == 5:
                al8 = True
                alienInt += 0.5
                aliencap = True
            if al1 == False and al2 == False and al3 == False and al4 == False and al5 == False and al6 == False and wavestart == True:
                music.play(music.ENTERTAINER)
                wave += 1
                alienInt = 0
                aliencap = False
                wavestart = False 
        if wave == 6:
            if alienInt == 0.5:
                wavestart = True
                al1 = True
            if alienInt == 1:
                al2 = True
            if alienInt == 1.5:
                al3 = True
            if alienInt == 2:
                al4 = True
            if alienInt == 2.5:
                al5 = True
            if alienInt == 3:
                al6 = True
            if alienInt == 3.5:
                al7 = True
            if alienInt == 4:
                al7 = True
            if alienInt == 4.5:
                al7 = True
            if alienInt == 5:
                al8 = True
                alienInt += 0.5
                aliencap = True
            if al1 == False and al2 == False and al3 == False and al4 == False and al5 == False and al6 == False and wavestart == True:
                music.play(music.ENTERTAINER)
                reset()
    if startscreen == True:
        display.show(alienpic)
        if button_a.was_pressed() or button_b.was_pressed() or accelerometer.was_gesture('shake'):
            music.play(music.POWER_UP, wait = False)
            display.clear()
            startscreen = False       