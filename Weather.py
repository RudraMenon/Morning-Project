from ez_ui_09 import *
from ez_graphics_09 import*
from ez_touchscreen_09 import*
from ez_hardware_09 import *
from urllib2 import Request, urlopen, URLError
import ast, time, datetime, sys, math
from ez_wifi_09 import*
from ez_ui_09 import *

#import alarmSelect
# Initialize Global Variables

forecastData= None
currData    = None
hourData    = None
diffDatas   = []
last        = 0 
boxTopX     = 50
boxTopY     = 240
boxLength   = 700
boxHeight   = 210
bg          = None
picker      = 0
sliderLength= 0
sliderX     = 0
scrollSpace = capture_image(boxTopX,boxTopY+boxHeight,boxLength,30)
oldPicker   = None
imageSpace  = capture_image(boxTopX,boxTopY,boxLength,boxHeight)


def getLines():
    """ returns lines from LastData.txt"""
    txtFile = open('LastData.txt', 'r')
    lines = txtFile.readlines()
    txtFile.close()
    return lines

def getWeather():
    """ modifies global variables hourDta, currData, and forecastData from API
    or written text file"""
    
    global hourData,currData,forecastData,last, diffDatas
    print 'getweather'
    
    lines = getLines()
    now = time.time()
    
    if lines == [] or (len(lines) > 0 and now-float(lines[0])>3600):
        hourData = getHourData()
        currData = getCurrentData()
        forecastData = getForecastData()
        writeFile(hourData,currData,forecastData)
    
    else:
        hourData = eval(lines[1])
        currData = eval(lines[2])
        forecastData = eval(lines[3])
    
    diffDatas       = [hourData,forecastData]
    
def writeFile(hourData,currData,forecastData):
    'writing file'
    txtFile = open('LastData.txt', 'w')
    txtFile.write('')
    txtFile.close()
    
    txtFile = open('LastData.txt', 'w')
    txtFile.write(str(time.time()))
    txtFile.write('\n')
    txtFile.write(str(hourData))
    txtFile.write('\n')
    txtFile.write(str(currData))
    txtFile.write('\n')
    txtFile.write(str(forecastData))
    txtFile.close()

def getCurrentData():
    print 'getCurrentData'
    checkWifi()
    request = Request('http://api.wunderground.com/api/0e060f345881cb0b/conditions/q/CA/college_park.json')
    
    try:
        response = urlopen(request)
        
    except URLError, e:
        return []
        
    weather = eval(response.read().replace('null',"None"))['current_observation']

        
    currTemp = weather['temp_f']
    currWind = weather['wind_mph']
    currWindDir = weather['wind_degrees']
    currFeel = weather['feelslike_f']
    visibility = weather['visibility_mi']
    currRain = weather['precip_today_in']
    humidity = weather['relative_humidity']
    icon = weather['icon_url']
    icon = icon[icon.find('k/')+2:-4]
    return {'currTemp':currTemp,'currWind':currWind,'currFeel':currFeel,'visibility':visibility,'currRain':currRain,'humidity':humidity,'icon':icon, 'windDir':currWindDir}
    #return weather
    
def getHourData():
    print 'getHourData'
    checkWifi()
    request = Request('http://api.wunderground.com/api/0e060f345881cb0b/hourly/q/CA/college_park.json')
    try:
        response = urlopen(request)
    except URLError,e:
        return []
    weatherHours = eval(response.read().replace('null',"'nothing'"))['hourly_forecast']
    hourForecast = []
    for weather in weatherHours:
        condition = weather['condition']
        temp = weather['temp']['english']
        humidity = weather['humidity']
        icon = weather['icon_url']
        icon = icon [icon.find('k/')+2:-4]
        wspd = weather['wspd']['english']
        qpf = weather['qpf']['english']
        month = weather['FCTTIME']['mon_abbrev']
        time = weather['FCTTIME']['civil']
        day = weather['FCTTIME']['weekday_name_abbrev']
        hourForecast.append({'Temp':temp,'Conditions':condition,'Humidity':humidity,'icon':icon,'WSPD':wspd,'QPF':qpf,'Month':month,'Time':time,'Day':day})
    return hourForecast
    
def getForecastData():
    checkWifi()
    print 'forecastdata'
    request = Request('http://api.wunderground.com/api/0e060f345881cb0b/forecast10day/q/CA/college_park.json')
    try:
        response = urlopen(request)
        weather = response.read().replace('null',"'nothing'")
        weatherDict = eval(weather)['forecast']['simpleforecast']['forecastday']
        days = []
        for day in weatherDict:
            temp        = day['high']['fahrenheit']
            conditions  = day['conditions']
            icon        = day['icon_url']
            icon        = icon[icon.find('k/')+2:-4]
            weekDay     = day['date']['weekday_short']
            month       = day['date']['monthname_short']
            date        = str(month) + '/' + str(day['date']['day'])
            days.append({'Temp':temp,'Conditions':conditions,'icon':icon,'Week Day':weekDay, 'Month':month, 'Date':date})
        return days
    except URLError, e:
        return []

def plotData(data,yRecord,xRecord,coords, color):
    """Displays Graph of data within coords"""


    #clear_screen('white')
    set_text_size(12)
    # Define size and position vars
    xPos            = 0
    yPos            = 0
    width           = coords[0]
    height          = coords[1]
    
   # y value is list of dataPoints at i's index
    if yRecord not in data[0]:
        return
    print 'Displaying ', yRecord
    yValue = []
    for i in data:
        yValue.append(float(i[yRecord]))
    tick        = int(width/len(data))               # = distance between tick marks on graph
    ValRange    = max(yValue)-min(yValue)                       # = the range of values
    smallest    = min(yValue) - ((ValRange)/4)                  # = lowest y value on Graph
    largest     = max(yValue) + ((ValRange)/4)                  # = largest y value on Graph
    ValRange    = largest-smallest                              # = redefinition of ValRange
    oldX        = x = xPos
    oldY        = int(yPos+height-(((height)/ValRange)*(yValue[0]-smallest)))
    y           = yPos



    for index in range(len(data)):
        set_color(color)
        dataPoint = data[index]
        #define values of this Data Point
        yVar        = float(dataPoint[yRecord])
        icon        = dataPoint['icon']
        condition   = dataPoint['Conditions']
        y           = int(yPos+height-((height/ValRange)*(yVar-smallest)))
        draw_line(oldX,oldY,x,y)
        iconImage   = load_image('WeatherPic/'+icon+'.jpg')
        iconImage   = resize_image(iconImage,tick,tick,RESIZE_FAST)
        draw_image(iconImage,x,yPos)
        # draw text of y Value if it is new
        if dataPoint[yRecord] != data[index-1][yRecord] or index == 0:
            draw_text(str(dataPoint[yRecord]),x,y-15)
        # Format the Time
        
        if xRecord == 'Time':
            if int(dataPoint['Time'].split(':')[0])%3 == 0:
                set_color(200,200,200)
                draw_line(x,yPos,x+1,yPos+height)
                draw_text(str(dataPoint['Time']),x,yPos+height-30)
        else:
            set_color(200,200,200)
            draw_line(x,yPos,x+1,yPos+height)
            draw_text(str(dataPoint[xRecord]),x,yPos+height-30)
        
        # Save values as variables to be used in next iteration
        oldX = x
        oldY = y
        x = x + tick

        
def checkWifi():
    global forecastData, currData, hourData
    print 'checkwifi', wifi_get_state()
    while wifi_get_state() != 'COMPLETED':
        wifi_connect_transient_network('umd-secure', False, 1, 'WPA-WPA2-PEAP', password='Lordoftheflies3!', identity='rmenon20')        
        
def round_to(n, precision):
    correction = 0.5 if n >= 0 else -0.5
    return int( n/precision+correction ) * precision
    
def windArrow(windStrength,windDir,xOrigin,yOrigin,length):
    set_color('black')
    xTop = xOrigin - length
    yTop = yOrigin - length
    draw_rect(xTop,yTop,length*2,length*2)
    draw_line(xTop+length,yTop+15,xTop+length,yTop+length*2-15)
    draw_line(xTop+15,yTop+length,xTop+length*2-15,yTop+length)
    set_text_size(20)
    draw_text('N', xTop+length-30,yTop+10)
    draw_text('E', xTop+length*2-30,yTop+length-30)
    draw_text('S', xTop+length+10,yTop+length*2-30)
    draw_text('W', xTop+10,yTop+length+10)
    
    
    set_color('blue')
    radDirection = math.radians(windDir)
    tipLength = length / 4
    endX = int(math.cos(radDirection)*length + xOrigin)
    endY = int(math.sin(radDirection)*length + yOrigin)
    draw_line(xOrigin,yOrigin,endX,endY)
    tipX1 = int(math.cos(math.radians(windDir-145))*tipLength + endX)
    tipY1 = int(math.sin(math.radians(windDir-145))*tipLength + endY)
    tipX2 = int(math.cos(math.radians(windDir+145))*tipLength + endX)
    tipY2 = int(math.sin(math.radians(windDir+145))*tipLength + endY)
    draw_line(endX,endY,tipX1,tipY1)
    draw_line(endX,endY,tipX2,tipY2)
    set_text_size(15)
    draw_text(str(windStrength) + ' mph',tipX2,tipY2)
panel = None

oldPlotFilter = []
def displayPage():
    global oldPicker, panel, oldPlotFilter
    data = diffDatas[picker]
    set_drawing_image(bg)
    set_color('white')
    fill_rect(0,0,800,450)
    interval = ['Time','Week Day'][picker]
    set_color('black')
    draw_rect(0,0,100,50)
    set_text_alignment(CENTER_CENTER)
    draw_text("back",50,25)
    set_text_alignment(LEFT_TOP)
    print 1
    fill_rect(3,240,44,210, 'yellow')
    print 2
    set_drawing_image(imageSpace)
    print 'plot just the one yes white'

    if picker == oldPicker:
        draw_image(imageSpace, 0, 0)
    if oldPlotFilter != plotFilterList or picker != oldPicker:
        clear_screen('white')
        if plotFilterList[0]:
            plotData(data, 'Temp', interval, [boxLength, boxHeight], 'red')

        if plotFilterList[1]:
            plotData(data, 'WSPD', interval, [boxLength, boxHeight], 'blue')

        if plotFilterList[2]:
            plotData(data, 'QPF', interval, [boxLength, boxHeight], 'green')

        if plotFilterList[3]:
            plotData(data, 'Humidity', interval, [boxLength, boxHeight], 'purple')
        oldPlotFilter = plotFilterList

    oldPicker = picker
    set_drawing_image(bg)
    draw_image(imageSpace,boxTopX,boxTopY)
    
    draw_rect(boxTopX,boxTopY,boxLength+20,boxHeight,'blue')
    currTemp    = currData['currTemp']
    currWind    = currData['currWind']
    windDir     = currData['windDir']
    currFeel    = currData['currFeel']
    visibility  = currData['visibility']
    currRain    = currData['currRain']
    humidity    = currData['humidity']
    icon        = currData['icon']
    now         = datetime.datetime.now()
    date        = now.strftime('%Y-%m-%d')
    time        = str(now.hour%12 +3) + now.strftime(':%M')
    
    windArrow(currWind,windDir-90,675,120,90)
    set_color('black')
    set_text_size(50)
    draw_text(date,50,50)
    draw_text(time,50,100)
    set_text_size(30)
    draw_text('Temperature: ' + str(currTemp),50,150)
    set_text_size(20)
    draw_text(' (Feels Like: '+str(currFeel)+')', 60,180)
    
    draw_text('Visibility: '+ str(visibility),430,50)
    draw_text('Wind: '      + str(currWind)  ,430,70)
    draw_text('Rain: '      + str(currRain)  ,430,90)
    draw_text('Humidity: '  + str(humidity)  ,430,110)
    
    iconImage = load_image('WeatherPic/'+ icon +'.jpg')
    fill_rect(450,150,get_image_width(iconImage)+20,get_image_height(iconImage)+20,'blue')
    draw_image(iconImage,460,160)

#def flipPage():
#    dataPicker = diffDatas[picker]
#    set_drawing_image(bg)
#    displayPage()
#    set_drawing_image(None)
#    draw_image(bg,0,0)

def scrollBar(x):
    set_drawing_image(scrollSpace)
    sliderLength = int(boxLength)
    sliderX = int(x - sliderLength/2)
    if sliderX < 0:
        sliderX = 0
    if sliderX > boxLength-sliderLength:
        sliderX = boxLength-sliderLength


    clear_screen('black')
    set_color('blue')
    fill_rect(sliderX,0,sliderLength,30)
    set_drawing_image(bg)
    draw_image(scrollSpace,boxTopX,boxTopY+boxHeight)
initY =0
plotFilterList = [1,0,0,0   ]
def on_checkbox_clicked(btn, release_point):
    # set the panel as a global variable
    global panel,plotFilterList
    plotFilterList = [
        panel.get_control('chk_1').value,
        panel.get_control('chk_2').value,
        panel.get_control('chk_3').value,
        panel.get_control('chk_4').value,
    ]

def main():
    global bg, picker, panel
    clear_screen('white')
    set_brightness(255)
    getWeather()
    
    bg              = capture_image(0,0,800,480)
    lines           = getLines()
    last            = float(lines[0])
    currTime        = printedTime = str(datetime.datetime.now().hour%12) + datetime.datetime.now().strftime(':%M')
    #    printedTime     = currTime
    diffDataPoints  = [['Day','Time','Temp','Conditions','Humidity','WSPD','QPF'],['Week Day','Date','Temp','Conditions']]
    first           = True
    firstY          = 0
    on              = True
    swipeTime       = time.time()
    lastTouch       = time.time()
    swipeFirstX     = None
    
    displayPage()
    stableX = 0
    stableY = 0
    while True:
        dataPoints = diffDataPoints[picker]
        multiTouch = touchscreen_finger_points_multitouch()
        if multiTouch != []:
            set_drawing_image(bg)
            displayPage()
            if len(multiTouch) == 1:
                currTime = str(datetime.datetime.now().hour%12) + datetime.datetime.now().strftime(':%M')
                lastTouch = time.time()
                if multiTouch[0]['x'] != None and multiTouch[0]['y'] != None and    stableX != None and stableY != None:
                    if (abs(multiTouch[0]['x'] - stableX) > 10 or abs(multiTouch[0]['y']-stableY) > 10):
                        x = multiTouch[0]['x']
                        y = multiTouch[0]['y']
                        stableX = x
                        stableY = y


                if not on:
                    # Turn on and scrub
                    displayPage()
                    set_brightness(255)
                    on = True
#                if x<100 and y < 50:
#                    alarmSelect.main()
                if boxTopY + boxHeight < y < boxTopY + boxHeight + 30 and boxTopX < x < boxTopX + boxLength:
                    scrollBar(x)
                    
                if boxTopY + boxHeight > y > boxTopY:
                    if boxTopX < x < boxTopX + boxLength:
                        if first:
                            firstY = y
                            print firstY,'--------------------------------------'
                        scrub(x,y,dataPoints,picker)

                if 3 < x < 47 and 240 < y < 475:
                    plotPanel= True
                    img = get_drawing_image()
                    set_drawing_image(None)
                    panel = create_panel(0,0,800,480)
                    panel.color_background = 'green'
                    panel.add_checkbox('chk_1', 100,  50, 200,  40, text='Temperature', on_click_handler=on_checkbox_clicked, color_text = 'red'   ,value=plotFilterList[0])
                    panel.add_checkbox('chk_2', 100, 100, 200,  40, text='Wind Speed',  on_click_handler=on_checkbox_clicked, color_text = 'blue'  ,value=plotFilterList[1])
                    panel.add_checkbox('chk_3', 100, 150, 200,  40, text='QPF',         on_click_handler=on_checkbox_clicked, color_text = 'green' ,value=plotFilterList[2])
                    panel.add_checkbox('chk_4', 100, 200, 200,  40, text='Humidity',    on_click_handler=on_checkbox_clicked, color_text = 'purple',value=plotFilterList[3])
                    set_color('white')
                    fill_rect(5,5,150,50)
                    set_color('black')
                    set_text_alignment(CENTER_CENTER)
                    draw_text("EXIT", 80, 30)
                    while plotPanel:
                        touch = touchscreen_finger_point()
                        panel.process_touch(touch)
                        time.sleep(0.05)
                        if touch != None:
                            if touch['x'] < 150 and touch['y'] < 50:
                                plotPanel = False


                    
                elif y < 50:
                    if first:
                        swipeFirstX = x
                        draw_rect(swipeFirstX-255,0,505,20,'red')
                    else:
                        if on and swipeFirstX:
                            swipeProg = 255 - (abs(x-swipeFirstX))
                            if x-swipeFirstX > 0:
                                fill_rect(swipeFirstX,0,255-swipeProg,20,'red')
                            if x-swipeFirstX < 0:
                                fill_rect(x,0,swipeFirstX-x,20,'red')
                            putToSleep(swipeProg)
                            swipeTime = time.time()
                            if swipeProg <=0:
                                on = False
                                time.sleep(1)
                
                    
            elif len(multiTouch) == 0 and time.time()-last > 3600:
                print 'new weather'
                getWeather()
                displayPage()
                printedTime = currTime
                lines       = getLines()
                last        = float(lines[0])
            elif printedTime != currTime:
                displayPage()
                printedTime = currTime
            first = False
            set_drawing_image(None)
            draw_image(bg,0,0) 
        else:   
            if not first:
                if time.time() - lastTouch > 0.2:
                    if firstY != None and y - firstY > 50:
                        picker = 1 - picker
                        print picker, oldPicker
                    firstY = None
                    first = True
                    set_drawing_image(bg)
                    displayPage()
                    set_drawing_image(None)
                    draw_image(bg,0,0) 
            
            
def putToSleep(brightness):
    if brightness > 225:
        brightness = 225
    if brightness < 0:
        brightness = 0
    set_brightness(int(brightness))

def scrub(x,y,dataPoints,picker):
    infoBoxLength = 200
    infoBoxHeight = 120
    infoBoxX = x-infoBoxLength/2
    infoBoxY = boxTopY-infoBoxHeight/2
    
    draw_line(x,boxTopY,x,boxHeight,'blue')
    fill_rect(infoBoxX,infoBoxY,infoBoxLength,infoBoxHeight,'white')
    draw_rect(infoBoxX,infoBoxY,infoBoxLength,infoBoxHeight,'blue')
    spacing = int(boxLength/len(diffDatas[picker]))
    index = round_to(((x-boxTopX))/spacing,1)
    if index >= len(diffDatas[picker]):
        index = len(diffDatas[picker])-1
    textLineY = infoBoxY + 5
    textLineX = infoBoxX + 5
    set_color('black')
    set_text_size(15)
    for data in dataPoints:
        draw_text(data + ': ' + str(diffDatas[picker][index][data]),textLineX,textLineY)
        textLineY += 15
    icon = load_image('WeatherPic/'+ str(diffDatas[picker][index]['icon'])+'.jpg')
    draw_image(icon,x-get_image_width(icon)/2,infoBoxY+infoBoxHeight)




main()