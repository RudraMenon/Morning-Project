from ez_graphics_09 import*
from ez_touchscreen_09 import*
import time
from datetime import datetime,timedelta
import math


class Time():
    def __init__(self):
        self.timeString = getTimeFormat()
        timeSplit       = self.timeString.split(':')
        self.hours      = int(timeSplit[0])
        self.minutes    = int(timeSplit[1])
        self.seconds    = int(timeSplit[2])
        self.amPm       = 'am'
        self.changeAble = True
        self.activated  = False
        self.on         = True

        self.realMinutes= self.minutes
        if self.hours > 12:
            self.amPm = 'pm'

    def zeroSec(self):
        self.seconds = 0

    def addMinutes(self,min):
        self.minutes += min
        while self.minutes > 60:
            self.hours += 1
            self.minutes -= 60

    def updateTime(self, timeString):
        self.timeString = timeString
        timeSplit       = self.timeString.split(':')
        print timeSplit
        self.hours      = int(timeSplit[0])
        self.minutes    = int(timeSplit[1])
        self.seconds    = int(timeSplit[2])        
        if self.hours > 12:
            self.amPm = 'pm'
    
    def getTimeInt(self):
        return (self.hours*3600)+(self.minutes*60)+self.seconds
    
    def compareTimes(self, otherTime):
        return self.getTimeInt() - otherTime.getTimeInt()
    
    def setTime(self, hour,minute,second):
        self.hours = hour
        self.minutes = minutes
        self.seconds = seconds
        
    def toString(self):
        return "%02d:%02d:%02d" % (self.hours,self.minutes,self.seconds)
    
    def toggleAmPm(self):
        if self.amPm == 'am':
            self.amPm = 'pm'
            self.hours += 12
        else:
            self.amPm = 'am'
            self.hours -= 12
        touch_point = touchscreen_finger_point()
        while touch_point != None:
            touch_point = touchscreen_finger_point()
            
def getTimeFormat():
    currTime = datetime.now()+timedelta(hours=3)
    return '{:%H:%M:%S}'.format(currTime)


def getTimeInt(string):
    timeSplit = string.split(':')
    hours = int(timeSplit[0])
    minutes = int(timeSplit[1])
    seconds = int(timeSplit[2])
    return (hours*3600)+(minutes*60)+seconds
        
        
    

masterTime = Time()
masterTime.changeAble = False
class showClock():
    def __init__(self, clock):
        self.clock = clock
        self.SIZE = 175
        self.border = 300
        
        self.centX, self.centY = 550,240
        
    
    def drawBaseClock(self):
        if self.clock.amPm == 'pm':
            fill_rect(300,0,500,480,'black')
            set_color('white')
        
        if self.clock.amPm == 'am':
            fill_rect(300,0,500,480,'white')
            set_color('black')


        draw_circle(self.centX,self.centY,int(self.SIZE*0.5))
        draw_circle(self.centX,self.centY,self.SIZE)

        fill_circle(self.centX,self.centY,self.SIZE/2 - int((self.clock.seconds/60.0) * (self.SIZE/2.0)),'blue')

        startA = -90
        endA = int(360*(self.clock.minutes/60.0)-90.0)
        for i in range(15):
            smallSize = self.SIZE-(2*i)
            draw_arc(self.centX-self.SIZE/2+i,self.centY-self.SIZE/2+i,smallSize,smallSize,startA,endA)
        
        endA = int(360*((self.clock.hours%12)/12.0)-90.0) + (int(30*(self.clock.minutes/60.0)))
        for i in range(5):
            bigSize = self.SIZE*2-(2*i)
            draw_arc(self.centX-self.SIZE+i,self.centY-self.SIZE+i,bigSize,bigSize,startA,endA)
        greyColor = int(245*(self.clock.seconds/60.0)) + 10

        draw_text(self.clock.toString(),self.centX,20)

    def drawMinuteArc(self,x,y):
        startA = -90
        endA = int(math.degrees(math.atan2(y-self.centY, x-self.centX)))
        if endA < startA:
            endA += 360    
        draw_rect(x,y,10,10)
        self.clock.minutes = int(60*(endA+90.0)/360)
        
    def drawHourArc(self,x,y):
        startA = -90
        endA = int(math.degrees(math.atan2(y-self.centY, x-self.centX)))
        if endA < startA:
            endA += 360    
        draw_rect(x,y,10,10)
        self.clock.hours = int((12*(endA+90.0))/360)
        if self.clock.amPm == 'pm':
            self.clock.hours += 12
        
    def runClock(self,x,y):
        if x > self.border and self.clock.changeAble:
            if (math.hypot(x-self.centX, y-self.centY) < self.SIZE/2):
               self.clock.toggleAmPm() 
            elif (math.hypot(x-self.centX, y-self.centY) < self.SIZE):
                self.drawMinuteArc(x,y)
            else:
                self.drawHourArc(x,y)
        
        self.drawBaseClock()
    def showTime(self,currTime):
        self.clock = masterTime
        masterTime.updateTime(currTime)
        self.drawBaseClock()

