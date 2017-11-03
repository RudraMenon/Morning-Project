from ez_graphics_09 import*
from ez_touchscreen_09 import*
from ez_sound_09 import*
import time
from datetime import datetime,timedelta
import math
from alarm import*
import Weather

class alarmButton():
    def __init__(self, clock):
        self.clock      = clock
        self.on         = clock.on
        self.isHighlight= False
        self.color      = (150,150,150)
        
        
    def toggle(self):
        self.on = not (self.on)
        self.clock.on = not (self.clock.on)
        touch_point = touchscreen_finger_point()
        while touch_point != None:
            touch_point = touchscreen_finger_point()
        
    def drawAlarm(self,x,y,width):
        set_color(self.color[0],self.color[1],self.color[2])
        fill_rect(x,y,width,60)
        if self.on:
            set_color('green')
        else:
            set_color('red')
        fill_rect(x + int(width*0.75), y, int(width*0.25),60)
        set_color('black')
        draw_rect(x,y,width,60)
        set_text_alignment(CENTER_CENTER)
        set_text_size(40)
        draw_text(self.clock.toString(), int(0.375*width),y+40)
        
    def highlight(self):
        self.isHighlight = True
        self.color = (50,250,90)
    
    def deHighlight(self):
        self.isHighlight = False
        self.color = (150,150,150)
        
class alarmSelect():
    def __init__(self):
        self.alarmList  = []
        self.buttonList = []
        self.collapsed  = True
        self.width      = 300
        self.height     = 480
        self.yOfset     = 0
        self.selectedIndex = 0
        self.timeSelected = True
        self.readFile()
        
    def getAlarm(self):
        return self.alarmList[self.selectedIndex]
        
    def addAlarm(self, alarm):
        alarm.zeroSec()
        alarmButton = createAlarmButton(alarm)

        self.alarmList.append(alarm)
        self.buttonList.append(alarmButton)

    def updateTime(self,currTime):
        if self.timeSelected:
            fill_rect(0,0,300,100,"green")
        else:
            fill_rect(0,0,300,100,"black")
        draw_rect(0,0,300,100,'white')
        set_text_alignment(CENTER_CENTER)
        set_text_size(40)
        set_color('white')
        draw_text("Time: " + currTime, int(self.width/2) ,50)

    def writeFile(self):
        file = open('alarmText.txt','w')
        text = ""
        for alarm in self.alarmList:
            line = alarm.toString() + ' - ' +  str(alarm.on) + "\n"
            text = text + line
        file.write(text)
        file.close()

    def readFile(self):
        try:
            file = open('alarmText.txt','r')
            lines = file.readlines()
            self.alarmList = []
            for line in lines:
                timeString = line.split('-')[0].strip()
                on = line.split('-')[1].strip().replace('\n','') == 'True'
                alarm = Time()
                alarm.updateTime(timeString)
                alarm.on = on
                self.alarmList.append(alarm)
                alarmButton = createAlarmButton(alarm)
                self.buttonList.append(alarmButton)
        except:
            file = open('alarmText.txt','w')

    def drawAlarms(self):
        
        for alarmNum in range(len(self.alarmList)):
            y = 100 + (alarmNum*60)+self.yOfset
            self.buttonList[alarmNum].drawAlarm(0,y,self.width)
    
    def processTouch(self,x,y):
        self.buttonList[self.selectedIndex].deHighlight()
        if (0<x<self.width):
            if y < 100:
                self.buttonList[self.selectedIndex].deHighlight()
                self.timeSelected = True
            else:
                self.timeSelected = False
                index = int((y-100)/60)
                if index >= len(self.alarmList):
                    index = len(self.alarmList)-1
        if self.width*0.75 < x < self.width and y > 100:
            self.buttonList[index].toggle()
        elif x < self.width and y > 100:
            if index >= len(self.alarmList):
                index = len(self.alarmList)-1
            self.timeSelected = False
            self.selectedIndex = index
            showAlarm.clock = self.alarmList[self.selectedIndex]
        if not self.timeSelected:
            self.buttonList[self.selectedIndex].highlight()

        self.drawAlarms()

    def stopAlarm(self, alarm):
        set_text_alignment(CENTER_CENTER)
        set_text_size(40)
        touch = touchscreen_finger_point()
        if touch == None:
            return False
        xOrig = touch['x']
        yOrig = touch['y']
        origImage = capture_image(0,0,800,480)
        sleep = False
        while touch != None:
            touch = touchscreen_finger_point()
            if touch != None:
                x = touch['x']
                y = touch['y']
                hypot = int(math.hypot(xOrig - x, yOrig - y))

                bg = capture_image(0, 0, 800, 480)
                set_drawing_image(bg)
                draw_image(origImage,0,0)
                if hypot < 100:
                    fill_circle(xOrig,yOrig,hypot,'green')
                    draw_text('!',xOrig,yOrig)
                    sleep = False

                else:
                    sleepTime = int(hypot/10)-10
                    fill_circle(xOrig,yOrig,hypot,'red')
                    draw_text(str(sleepTime),xOrig,yOrig)
                    sleep = True
                set_drawing_image(None)
                draw_image(bg, 0, 0)
        if sleep:
            alarm.addMinutes(sleepTime)
        else:
            Weather.main()
        self.drawAlarms()
        return True



    def checkAlarms(self, currTime):

        for alarm in self.alarmList:
            timeInt = getTimeInt(currTime)
            if alarm.getTimeInt() < timeInt:
                alarm.activated = False
            else:
                alarm.activated = True
            if alarm.getTimeInt() <= timeInt and alarm.activated and alarm.on:
                print 'buzz'
                print get_volume()
                set_volume(50)
                snd = load_sound("cow.wav")

                uid = play_sound(snd)
                touch_point = touchscreen_finger_point()
                while 1:
                    if touchscreen_finger_point() != None:
                        stopAlarm = self.stopAlarm(alarm)
                        if not stopAlarm:
                            alarm.minutes = alarm.realMinutes
                        print alarm.minutes
                        self.drawAlarms()
                        break
                    stop_sound(uid)
                    if not is_sound_playing(uid):

                        uid = play_sound(snd)
                    time.sleep(0.1)

                alarm.activated = False




def createAlarmButton(alarm):
    return alarmButton(alarm)


alarmSelect = alarmSelect()
showAlarm = showClock(alarmSelect.getAlarm())
def main():
    clear_screen('black')

    alarmSelect.drawAlarms()
    lastTouch = 0
    written = False
    while True:
        bg = capture_image(0,0,800,480)
        set_drawing_image(bg)
        touch_point = touchscreen_finger_point()
        currTime = getTimeFormat()
        alarmSelect .checkAlarms(currTime)
        alarmSelect.updateTime(currTime)
        if touch_point != None:
            lastTouch = time.time()
            written = False
            # get the x and y coordinates of the touch
            x = touch_point['x']
            y = touch_point['y']
            alarmSelect.processTouch(x,y)
            showAlarm.runClock(x,y)
        if alarmSelect.timeSelected:
            # bg = capture_image(0, 0, 800, 480)
            # set_drawing_image(bg)
            showAlarm.showTime(currTime)
        now = time.time()
        if (now - lastTouch) > 1 and not written:
            alarmSelect.writeFile()
            written = True

        set_drawing_image(None)
        draw_image(bg,0,0)

        
if __name__ == "__main__":
    main()
