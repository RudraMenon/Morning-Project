from ez_ui_09 import *
from ez_graphics_09 import*
from ez_touchscreen_09 import*
from ez_hardware_09 import *
from urllib2 import Request, urlopen, URLError
import ast, time, datetime, sys, math
from ez_wifi_09 import*
panel = None
forecastData = None
currData = None
hourData = None
last = 0 
boxTopX     = 50
boxTopY     = 240
boxLength   = 700
boxHeight   = 240


class output:
    def __init__(self):
        self.content = []
    def write(self, string):
        self.content.append(string)
def epochTime(sinceEpoch):
    sinceEpoch = int(sinceEpoch)
    return time.strftime('%H:%M:%S', time.localtime(sinceEpoch))
def getWeather():
    global hourData,currData,forecastData,last
    print 'getweather'
    
    txtFile = open('LastData.txt', 'r')
    lines = txtFile.readlines()
    txtFile.close()
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
def writeFile(hourData,currData,forecastData):
    print 'writeFile'
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
    request = Request('http://api.wunderground.com/api/0e060f345881cb0b/conditions/q/CA/la_canada.json')
    
    try:
        response = urlopen(request)
        
    except URLError, e:
        return []
        
#    weather = eval(response.read().replace('null',"None"))['current_observation']
    weather = eval({
  "response": {
  "version":"0.1",
  "termsofService":"http://www.wunderground.com/weather/api/d/terms.html",
  "features": {
  "hourly": 1
  }
    }
		,
	"hourly_forecast": [
		{
		"FCTTIME": {
		"hour": "19","hour_padded": "19","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "21","mday_padded": "21","yday": "354","isdst": "0","epoch": "1450753200","pretty": "7:00 PM PST on December 21, 2015","civil": "7:00 PM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Monday","weekday_name_night": "Monday Night","weekday_name_abbrev": "Mon","weekday_name_unlang": "Monday","weekday_name_night_unlang": "Monday Night","ampm": "PM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "51", "metric": "11"},
		"dewpoint": {"english": "49", "metric": "9"},
		"condition": "Overcast",
		"icon": "cloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_cloudy.gif",
		"fctcode": "4",
		"sky": "92",
		"wspd": {"english": "4", "metric": "6"},
		"wdir": {"dir": "WSW", "degrees": "251"},
		"wx": "Cloudy",
		"uvi": "0",
		"humidity": "91",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "51", "metric": "11"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "3",
		"mslp": {"english": "30.06", "metric": "1018"}
		}
		,
		{
		"FCTTIME": {
		"hour": "20","hour_padded": "20","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "21","mday_padded": "21","yday": "354","isdst": "0","epoch": "1450756800","pretty": "8:00 PM PST on December 21, 2015","civil": "8:00 PM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Monday","weekday_name_night": "Monday Night","weekday_name_abbrev": "Mon","weekday_name_unlang": "Monday","weekday_name_night_unlang": "Monday Night","ampm": "PM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "51", "metric": "11"},
		"dewpoint": {"english": "50", "metric": "10"},
		"condition": "Overcast",
		"icon": "cloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_cloudy.gif",
		"fctcode": "4",
		"sky": "96",
		"wspd": {"english": "3", "metric": "5"},
		"wdir": {"dir": "SW", "degrees": "220"},
		"wx": "Cloudy",
		"uvi": "0",
		"humidity": "94",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "51", "metric": "11"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "7",
		"mslp": {"english": "30.06", "metric": "1018"}
		}
		,
		{
		"FCTTIME": {
		"hour": "21","hour_padded": "21","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "21","mday_padded": "21","yday": "354","isdst": "0","epoch": "1450760400","pretty": "9:00 PM PST on December 21, 2015","civil": "9:00 PM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Monday","weekday_name_night": "Monday Night","weekday_name_abbrev": "Mon","weekday_name_unlang": "Monday","weekday_name_night_unlang": "Monday Night","ampm": "PM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "52", "metric": "11"},
		"dewpoint": {"english": "51", "metric": "11"},
		"condition": "Overcast",
		"icon": "cloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_cloudy.gif",
		"fctcode": "4",
		"sky": "97",
		"wspd": {"english": "5", "metric": "8"},
		"wdir": {"dir": "S", "degrees": "190"},
		"wx": "Cloudy",
		"uvi": "0",
		"humidity": "96",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "52", "metric": "11"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "11",
		"mslp": {"english": "30.05", "metric": "1018"}
		}
		,
		{
		"FCTTIME": {
		"hour": "22","hour_padded": "22","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "21","mday_padded": "21","yday": "354","isdst": "0","epoch": "1450764000","pretty": "10:00 PM PST on December 21, 2015","civil": "10:00 PM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Monday","weekday_name_night": "Monday Night","weekday_name_abbrev": "Mon","weekday_name_unlang": "Monday","weekday_name_night_unlang": "Monday Night","ampm": "PM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "50", "metric": "10"},
		"dewpoint": {"english": "50", "metric": "10"},
		"condition": "Overcast",
		"icon": "cloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_cloudy.gif",
		"fctcode": "4",
		"sky": "95",
		"wspd": {"english": "3", "metric": "5"},
		"wdir": {"dir": "S", "degrees": "172"},
		"wx": "Cloudy",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "50", "metric": "10"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "2",
		"mslp": {"english": "30.04", "metric": "1017"}
		}
		,
		{
		"FCTTIME": {
		"hour": "23","hour_padded": "23","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "21","mday_padded": "21","yday": "354","isdst": "0","epoch": "1450767600","pretty": "11:00 PM PST on December 21, 2015","civil": "11:00 PM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Monday","weekday_name_night": "Monday Night","weekday_name_abbrev": "Mon","weekday_name_unlang": "Monday","weekday_name_night_unlang": "Monday Night","ampm": "PM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "50", "metric": "10"},
		"dewpoint": {"english": "50", "metric": "10"},
		"condition": "Overcast",
		"icon": "cloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_cloudy.gif",
		"fctcode": "4",
		"sky": "97",
		"wspd": {"english": "4", "metric": "6"},
		"wdir": {"dir": "S", "degrees": "173"},
		"wx": "Cloudy",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "50", "metric": "10"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "21",
		"mslp": {"english": "30.03", "metric": "1017"}
		}
		,
		{
		"FCTTIME": {
		"hour": "0","hour_padded": "00","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450771200","pretty": "12:00 AM PST on December 22, 2015","civil": "12:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "51", "metric": "11"},
		"dewpoint": {"english": "51", "metric": "11"},
		"condition": "Overcast",
		"icon": "cloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_cloudy.gif",
		"fctcode": "4",
		"sky": "99",
		"wspd": {"english": "4", "metric": "6"},
		"wdir": {"dir": "S", "degrees": "172"},
		"wx": "Cloudy",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "51", "metric": "11"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "24",
		"mslp": {"english": "30.01", "metric": "1016"}
		}
		,
		{
		"FCTTIME": {
		"hour": "1","hour_padded": "01","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450774800","pretty": "1:00 AM PST on December 22, 2015","civil": "1:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "51", "metric": "11"},
		"dewpoint": {"english": "51", "metric": "11"},
		"condition": "Chance of Rain",
		"icon": "chancerain",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_chancerain.gif",
		"fctcode": "12",
		"sky": "100",
		"wspd": {"english": "5", "metric": "8"},
		"wdir": {"dir": "SSE", "degrees": "167"},
		"wx": "Showers",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "51", "metric": "11"},
		"qpf": {"english": "0.02", "metric": "1"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "51",
		"mslp": {"english": "29.99", "metric": "1016"}
		}
		,
		{
		"FCTTIME": {
		"hour": "2","hour_padded": "02","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450778400","pretty": "2:00 AM PST on December 22, 2015","civil": "2:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "51", "metric": "11"},
		"dewpoint": {"english": "51", "metric": "11"},
		"condition": "Chance of Rain",
		"icon": "chancerain",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_chancerain.gif",
		"fctcode": "12",
		"sky": "100",
		"wspd": {"english": "7", "metric": "11"},
		"wdir": {"dir": "SSE", "degrees": "159"},
		"wx": "Light Rain",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "51", "metric": "11"},
		"qpf": {"english": "0.02", "metric": "1"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "64",
		"mslp": {"english": "29.97", "metric": "1015"}
		}
		,
		{
		"FCTTIME": {
		"hour": "3","hour_padded": "03","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450782000","pretty": "3:00 AM PST on December 22, 2015","civil": "3:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "51", "metric": "11"},
		"dewpoint": {"english": "51", "metric": "11"},
		"condition": "Chance of Rain",
		"icon": "chancerain",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_chancerain.gif",
		"fctcode": "12",
		"sky": "100",
		"wspd": {"english": "6", "metric": "10"},
		"wdir": {"dir": "SSE", "degrees": "153"},
		"wx": "Light Rain",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "51", "metric": "11"},
		"qpf": {"english": "0.02", "metric": "1"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "73",
		"mslp": {"english": "29.95", "metric": "1014"}
		}
		,
		{
		"FCTTIME": {
		"hour": "4","hour_padded": "04","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450785600","pretty": "4:00 AM PST on December 22, 2015","civil": "4:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "50", "metric": "10"},
		"dewpoint": {"english": "50", "metric": "10"},
		"condition": "Chance of Rain",
		"icon": "chancerain",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_chancerain.gif",
		"fctcode": "12",
		"sky": "100",
		"wspd": {"english": "6", "metric": "10"},
		"wdir": {"dir": "SE", "degrees": "146"},
		"wx": "Light Rain",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "50", "metric": "10"},
		"qpf": {"english": "0.02", "metric": "1"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "72",
		"mslp": {"english": "29.92", "metric": "1013"}
		}
		,
		{
		"FCTTIME": {
		"hour": "5","hour_padded": "05","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450789200","pretty": "5:00 AM PST on December 22, 2015","civil": "5:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "50", "metric": "10"},
		"dewpoint": {"english": "50", "metric": "10"},
		"condition": "Chance of Rain",
		"icon": "chancerain",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_chancerain.gif",
		"fctcode": "12",
		"sky": "100",
		"wspd": {"english": "7", "metric": "11"},
		"wdir": {"dir": "SE", "degrees": "143"},
		"wx": "Light Rain",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "50", "metric": "10"},
		"qpf": {"english": "0.02", "metric": "1"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "72",
		"mslp": {"english": "29.91", "metric": "1013"}
		}
		,
		{
		"FCTTIME": {
		"hour": "6","hour_padded": "06","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450792800","pretty": "6:00 AM PST on December 22, 2015","civil": "6:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "51", "metric": "11"},
		"dewpoint": {"english": "51", "metric": "11"},
		"condition": "Chance of Rain",
		"icon": "chancerain",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_chancerain.gif",
		"fctcode": "12",
		"sky": "100",
		"wspd": {"english": "8", "metric": "13"},
		"wdir": {"dir": "SE", "degrees": "146"},
		"wx": "Light Rain",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "51", "metric": "11"},
		"qpf": {"english": "0.02", "metric": "1"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "72",
		"mslp": {"english": "29.89", "metric": "1012"}
		}
		,
		{
		"FCTTIME": {
		"hour": "7","hour_padded": "07","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450796400","pretty": "7:00 AM PST on December 22, 2015","civil": "7:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "51", "metric": "11"},
		"dewpoint": {"english": "51", "metric": "11"},
		"condition": "Chance of Rain",
		"icon": "chancerain",
		"icon_url":"http://icons.wxug.com/i/c/k/chancerain.gif",
		"fctcode": "12",
		"sky": "100",
		"wspd": {"english": "8", "metric": "13"},
		"wdir": {"dir": "SE", "degrees": "137"},
		"wx": "Light Rain",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "51", "metric": "11"},
		"qpf": {"english": "0.01", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "61",
		"mslp": {"english": "29.88", "metric": "1012"}
		}
		,
		{
		"FCTTIME": {
		"hour": "8","hour_padded": "08","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450800000","pretty": "8:00 AM PST on December 22, 2015","civil": "8:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "53", "metric": "12"},
		"dewpoint": {"english": "53", "metric": "12"},
		"condition": "Chance of Rain",
		"icon": "chancerain",
		"icon_url":"http://icons.wxug.com/i/c/k/chancerain.gif",
		"fctcode": "12",
		"sky": "97",
		"wspd": {"english": "7", "metric": "11"},
		"wdir": {"dir": "SE", "degrees": "130"},
		"wx": "Showers",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "53", "metric": "12"},
		"qpf": {"english": "0.01", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "55",
		"mslp": {"english": "29.87", "metric": "1012"}
		}
		,
		{
		"FCTTIME": {
		"hour": "9","hour_padded": "09","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450803600","pretty": "9:00 AM PST on December 22, 2015","civil": "9:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "54", "metric": "12"},
		"dewpoint": {"english": "54", "metric": "12"},
		"condition": "Chance of Rain",
		"icon": "chancerain",
		"icon_url":"http://icons.wxug.com/i/c/k/chancerain.gif",
		"fctcode": "12",
		"sky": "95",
		"wspd": {"english": "6", "metric": "10"},
		"wdir": {"dir": "ESE", "degrees": "116"},
		"wx": "Showers",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "54", "metric": "12"},
		"qpf": {"english": "0.01", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "48",
		"mslp": {"english": "29.87", "metric": "1012"}
		}
		,
		{
		"FCTTIME": {
		"hour": "10","hour_padded": "10","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450807200","pretty": "10:00 AM PST on December 22, 2015","civil": "10:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "55", "metric": "13"},
		"dewpoint": {"english": "55", "metric": "13"},
		"condition": "Chance of Rain",
		"icon": "chancerain",
		"icon_url":"http://icons.wxug.com/i/c/k/chancerain.gif",
		"fctcode": "12",
		"sky": "97",
		"wspd": {"english": "7", "metric": "11"},
		"wdir": {"dir": "ESE", "degrees": "113"},
		"wx": "Showers",
		"uvi": "1",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "55", "metric": "13"},
		"qpf": {"english": "0.01", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "57",
		"mslp": {"english": "29.86", "metric": "1011"}
		}
		,
		{
		"FCTTIME": {
		"hour": "11","hour_padded": "11","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450810800","pretty": "11:00 AM PST on December 22, 2015","civil": "11:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "57", "metric": "14"},
		"dewpoint": {"english": "53", "metric": "12"},
		"condition": "Chance of Rain",
		"icon": "chancerain",
		"icon_url":"http://icons.wxug.com/i/c/k/chancerain.gif",
		"fctcode": "12",
		"sky": "97",
		"wspd": {"english": "8", "metric": "13"},
		"wdir": {"dir": "ESE", "degrees": "113"},
		"wx": "Showers",
		"uvi": "1",
		"humidity": "88",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "57", "metric": "14"},
		"qpf": {"english": "0.01", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "53",
		"mslp": {"english": "29.85", "metric": "1011"}
		}
		,
		{
		"FCTTIME": {
		"hour": "12","hour_padded": "12","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450814400","pretty": "12:00 PM PST on December 22, 2015","civil": "12:00 PM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "PM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "58", "metric": "14"},
		"dewpoint": {"english": "54", "metric": "12"},
		"condition": "Chance of Rain",
		"icon": "chancerain",
		"icon_url":"http://icons.wxug.com/i/c/k/chancerain.gif",
		"fctcode": "12",
		"sky": "97",
		"wspd": {"english": "8", "metric": "13"},
		"wdir": {"dir": "ESE", "degrees": "120"},
		"wx": "Showers",
		"uvi": "1",
		"humidity": "87",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "58", "metric": "14"},
		"qpf": {"english": "0.01", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "47",
		"mslp": {"english": "29.82", "metric": "1010"}
		}
		,
		{
		"FCTTIME": {
		"hour": "13","hour_padded": "13","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450818000","pretty": "1:00 PM PST on December 22, 2015","civil": "1:00 PM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "PM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "59", "metric": "15"},
		"dewpoint": {"english": "53", "metric": "12"},
		"condition": "Chance of Rain",
		"icon": "chancerain",
		"icon_url":"http://icons.wxug.com/i/c/k/chancerain.gif",
		"fctcode": "12",
		"sky": "97",
		"wspd": {"english": "9", "metric": "14"},
		"wdir": {"dir": "ESE", "degrees": "121"},
		"wx": "Showers",
		"uvi": "1",
		"humidity": "81",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "59", "metric": "15"},
		"qpf": {"english": "0.01", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "45",
		"mslp": {"english": "29.8", "metric": "1009"}
		}
		,
		{
		"FCTTIME": {
		"hour": "14","hour_padded": "14","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450821600","pretty": "2:00 PM PST on December 22, 2015","civil": "2:00 PM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "PM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "60", "metric": "16"},
		"dewpoint": {"english": "54", "metric": "12"},
		"condition": "Overcast",
		"icon": "cloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/cloudy.gif",
		"fctcode": "4",
		"sky": "97",
		"wspd": {"english": "7", "metric": "11"},
		"wdir": {"dir": "ESE", "degrees": "121"},
		"wx": "Cloudy",
		"uvi": "1",
		"humidity": "82",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "60", "metric": "16"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "24",
		"mslp": {"english": "29.79", "metric": "1009"}
		}
		,
		{
		"FCTTIME": {
		"hour": "15","hour_padded": "15","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450825200","pretty": "3:00 PM PST on December 22, 2015","civil": "3:00 PM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "PM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "59", "metric": "15"},
		"dewpoint": {"english": "55", "metric": "13"},
		"condition": "Overcast",
		"icon": "cloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/cloudy.gif",
		"fctcode": "4",
		"sky": "97",
		"wspd": {"english": "8", "metric": "13"},
		"wdir": {"dir": "SE", "degrees": "129"},
		"wx": "Cloudy",
		"uvi": "0",
		"humidity": "87",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "59", "metric": "15"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "24",
		"mslp": {"english": "29.77", "metric": "1008"}
		}
		,
		{
		"FCTTIME": {
		"hour": "16","hour_padded": "16","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450828800","pretty": "4:00 PM PST on December 22, 2015","civil": "4:00 PM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "PM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "57", "metric": "14"},
		"dewpoint": {"english": "56", "metric": "13"},
		"condition": "Overcast",
		"icon": "cloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/cloudy.gif",
		"fctcode": "4",
		"sky": "94",
		"wspd": {"english": "7", "metric": "11"},
		"wdir": {"dir": "SE", "degrees": "139"},
		"wx": "Cloudy",
		"uvi": "0",
		"humidity": "97",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "57", "metric": "14"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "14",
		"mslp": {"english": "29.77", "metric": "1008"}
		}
		,
		{
		"FCTTIME": {
		"hour": "17","hour_padded": "17","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450832400","pretty": "5:00 PM PST on December 22, 2015","civil": "5:00 PM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "PM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "54", "metric": "12"},
		"dewpoint": {"english": "54", "metric": "12"},
		"condition": "Overcast",
		"icon": "cloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_cloudy.gif",
		"fctcode": "4",
		"sky": "89",
		"wspd": {"english": "7", "metric": "11"},
		"wdir": {"dir": "WSW", "degrees": "247"},
		"wx": "Cloudy",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "54", "metric": "12"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "5",
		"mslp": {"english": "29.77", "metric": "1008"}
		}
		,
		{
		"FCTTIME": {
		"hour": "18","hour_padded": "18","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450836000","pretty": "6:00 PM PST on December 22, 2015","civil": "6:00 PM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "PM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "53", "metric": "12"},
		"dewpoint": {"english": "53", "metric": "12"},
		"condition": "Mostly Cloudy",
		"icon": "mostlycloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_mostlycloudy.gif",
		"fctcode": "3",
		"sky": "77",
		"wspd": {"english": "7", "metric": "11"},
		"wdir": {"dir": "N", "degrees": "355"},
		"wx": "Mostly Cloudy",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "53", "metric": "12"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "4",
		"mslp": {"english": "29.78", "metric": "1008"}
		}
		,
		{
		"FCTTIME": {
		"hour": "19","hour_padded": "19","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450839600","pretty": "7:00 PM PST on December 22, 2015","civil": "7:00 PM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "PM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "54", "metric": "12"},
		"dewpoint": {"english": "54", "metric": "12"},
		"condition": "Mostly Cloudy",
		"icon": "mostlycloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_mostlycloudy.gif",
		"fctcode": "3",
		"sky": "62",
		"wspd": {"english": "7", "metric": "11"},
		"wdir": {"dir": "WNW", "degrees": "294"},
		"wx": "Mostly Cloudy",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "54", "metric": "12"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "4",
		"mslp": {"english": "29.78", "metric": "1008"}
		}
		,
		{
		"FCTTIME": {
		"hour": "20","hour_padded": "20","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450843200","pretty": "8:00 PM PST on December 22, 2015","civil": "8:00 PM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "PM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "53", "metric": "12"},
		"dewpoint": {"english": "53", "metric": "12"},
		"condition": "Partly Cloudy",
		"icon": "partlycloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_partlycloudy.gif",
		"fctcode": "2",
		"sky": "54",
		"wspd": {"english": "5", "metric": "8"},
		"wdir": {"dir": "W", "degrees": "269"},
		"wx": "Partly Cloudy",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "53", "metric": "12"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "3",
		"mslp": {"english": "29.79", "metric": "1009"}
		}
		,
		{
		"FCTTIME": {
		"hour": "21","hour_padded": "21","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450846800","pretty": "9:00 PM PST on December 22, 2015","civil": "9:00 PM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "PM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "53", "metric": "12"},
		"dewpoint": {"english": "53", "metric": "12"},
		"condition": "Partly Cloudy",
		"icon": "partlycloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_partlycloudy.gif",
		"fctcode": "2",
		"sky": "53",
		"wspd": {"english": "6", "metric": "10"},
		"wdir": {"dir": "W", "degrees": "269"},
		"wx": "Partly Cloudy",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "53", "metric": "12"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "3",
		"mslp": {"english": "29.79", "metric": "1009"}
		}
		,
		{
		"FCTTIME": {
		"hour": "22","hour_padded": "22","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450850400","pretty": "10:00 PM PST on December 22, 2015","civil": "10:00 PM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "PM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "52", "metric": "11"},
		"dewpoint": {"english": "52", "metric": "11"},
		"condition": "Partly Cloudy",
		"icon": "partlycloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_partlycloudy.gif",
		"fctcode": "2",
		"sky": "43",
		"wspd": {"english": "4", "metric": "6"},
		"wdir": {"dir": "W", "degrees": "274"},
		"wx": "Partly Cloudy",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "52", "metric": "11"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "3",
		"mslp": {"english": "29.79", "metric": "1009"}
		}
		,
		{
		"FCTTIME": {
		"hour": "23","hour_padded": "23","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "22","mday_padded": "22","yday": "355","isdst": "0","epoch": "1450854000","pretty": "11:00 PM PST on December 22, 2015","civil": "11:00 PM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Tuesday","weekday_name_night": "Tuesday Night","weekday_name_abbrev": "Tue","weekday_name_unlang": "Tuesday","weekday_name_night_unlang": "Tuesday Night","ampm": "PM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "52", "metric": "11"},
		"dewpoint": {"english": "52", "metric": "11"},
		"condition": "Partly Cloudy",
		"icon": "partlycloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_partlycloudy.gif",
		"fctcode": "2",
		"sky": "52",
		"wspd": {"english": "3", "metric": "5"},
		"wdir": {"dir": "WNW", "degrees": "284"},
		"wx": "Partly Cloudy",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "52", "metric": "11"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "3",
		"mslp": {"english": "29.78", "metric": "1008"}
		}
		,
		{
		"FCTTIME": {
		"hour": "0","hour_padded": "00","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "23","mday_padded": "23","yday": "356","isdst": "0","epoch": "1450857600","pretty": "12:00 AM PST on December 23, 2015","civil": "12:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Wednesday","weekday_name_night": "Wednesday Night","weekday_name_abbrev": "Wed","weekday_name_unlang": "Wednesday","weekday_name_night_unlang": "Wednesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "51", "metric": "11"},
		"dewpoint": {"english": "51", "metric": "11"},
		"condition": "Partly Cloudy",
		"icon": "partlycloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_partlycloudy.gif",
		"fctcode": "2",
		"sky": "59",
		"wspd": {"english": "4", "metric": "6"},
		"wdir": {"dir": "NW", "degrees": "305"},
		"wx": "Partly Cloudy",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "51", "metric": "11"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "2",
		"mslp": {"english": "29.78", "metric": "1008"}
		}
		,
		{
		"FCTTIME": {
		"hour": "1","hour_padded": "01","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "23","mday_padded": "23","yday": "356","isdst": "0","epoch": "1450861200","pretty": "1:00 AM PST on December 23, 2015","civil": "1:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Wednesday","weekday_name_night": "Wednesday Night","weekday_name_abbrev": "Wed","weekday_name_unlang": "Wednesday","weekday_name_night_unlang": "Wednesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "51", "metric": "11"},
		"dewpoint": {"english": "51", "metric": "11"},
		"condition": "Mostly Cloudy",
		"icon": "mostlycloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_mostlycloudy.gif",
		"fctcode": "3",
		"sky": "62",
		"wspd": {"english": "5", "metric": "8"},
		"wdir": {"dir": "NW", "degrees": "312"},
		"wx": "Mostly Cloudy",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "51", "metric": "11"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "2",
		"mslp": {"english": "29.78", "metric": "1008"}
		}
		,
		{
		"FCTTIME": {
		"hour": "2","hour_padded": "02","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "23","mday_padded": "23","yday": "356","isdst": "0","epoch": "1450864800","pretty": "2:00 AM PST on December 23, 2015","civil": "2:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Wednesday","weekday_name_night": "Wednesday Night","weekday_name_abbrev": "Wed","weekday_name_unlang": "Wednesday","weekday_name_night_unlang": "Wednesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "51", "metric": "11"},
		"dewpoint": {"english": "51", "metric": "11"},
		"condition": "Partly Cloudy",
		"icon": "partlycloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_partlycloudy.gif",
		"fctcode": "2",
		"sky": "55",
		"wspd": {"english": "7", "metric": "11"},
		"wdir": {"dir": "NW", "degrees": "325"},
		"wx": "Partly Cloudy",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "51", "metric": "11"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "1",
		"mslp": {"english": "29.77", "metric": "1008"}
		}
		,
		{
		"FCTTIME": {
		"hour": "3","hour_padded": "03","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "23","mday_padded": "23","yday": "356","isdst": "0","epoch": "1450868400","pretty": "3:00 AM PST on December 23, 2015","civil": "3:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Wednesday","weekday_name_night": "Wednesday Night","weekday_name_abbrev": "Wed","weekday_name_unlang": "Wednesday","weekday_name_night_unlang": "Wednesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "50", "metric": "10"},
		"dewpoint": {"english": "50", "metric": "10"},
		"condition": "Partly Cloudy",
		"icon": "partlycloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_partlycloudy.gif",
		"fctcode": "2",
		"sky": "45",
		"wspd": {"english": "7", "metric": "11"},
		"wdir": {"dir": "NNW", "degrees": "334"},
		"wx": "Partly Cloudy",
		"uvi": "0",
		"humidity": "100",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "50", "metric": "10"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "1",
		"mslp": {"english": "29.77", "metric": "1008"}
		}
		,
		{
		"FCTTIME": {
		"hour": "4","hour_padded": "04","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "23","mday_padded": "23","yday": "356","isdst": "0","epoch": "1450872000","pretty": "4:00 AM PST on December 23, 2015","civil": "4:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Wednesday","weekday_name_night": "Wednesday Night","weekday_name_abbrev": "Wed","weekday_name_unlang": "Wednesday","weekday_name_night_unlang": "Wednesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "50", "metric": "10"},
		"dewpoint": {"english": "49", "metric": "9"},
		"condition": "Partly Cloudy",
		"icon": "partlycloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_partlycloudy.gif",
		"fctcode": "2",
		"sky": "40",
		"wspd": {"english": "7", "metric": "11"},
		"wdir": {"dir": "NNW", "degrees": "340"},
		"wx": "Partly Cloudy",
		"uvi": "0",
		"humidity": "98",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "50", "metric": "10"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "0",
		"mslp": {"english": "29.77", "metric": "1008"}
		}
		,
		{
		"FCTTIME": {
		"hour": "5","hour_padded": "05","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "23","mday_padded": "23","yday": "356","isdst": "0","epoch": "1450875600","pretty": "5:00 AM PST on December 23, 2015","civil": "5:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Wednesday","weekday_name_night": "Wednesday Night","weekday_name_abbrev": "Wed","weekday_name_unlang": "Wednesday","weekday_name_night_unlang": "Wednesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "49", "metric": "9"},
		"dewpoint": {"english": "47", "metric": "8"},
		"condition": "Partly Cloudy",
		"icon": "partlycloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_partlycloudy.gif",
		"fctcode": "2",
		"sky": "38",
		"wspd": {"english": "7", "metric": "11"},
		"wdir": {"dir": "NNW", "degrees": "344"},
		"wx": "Partly Cloudy",
		"uvi": "0",
		"humidity": "92",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "49", "metric": "9"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "0",
		"mslp": {"english": "29.77", "metric": "1008"}
		}
		,
		{
		"FCTTIME": {
		"hour": "6","hour_padded": "06","min": "00","min_unpadded": "0","sec": "0","year": "2015","mon": "12","mon_padded": "12","mon_abbrev": "Dec","mday": "23","mday_padded": "23","yday": "356","isdst": "0","epoch": "1450879200","pretty": "6:00 AM PST on December 23, 2015","civil": "6:00 AM","month_name": "December","month_name_abbrev": "Dec","weekday_name": "Wednesday","weekday_name_night": "Wednesday Night","weekday_name_abbrev": "Wed","weekday_name_unlang": "Wednesday","weekday_name_night_unlang": "Wednesday Night","ampm": "AM","tz": "","age": "","UTCDATE": ""
		},
		"temp": {"english": "48", "metric": "9"},
		"dewpoint": {"english": "43", "metric": "6"},
		"condition": "Partly Cloudy",
		"icon": "partlycloudy",
		"icon_url":"http://icons.wxug.com/i/c/k/nt_partlycloudy.gif",
		"fctcode": "2",
		"sky": "37",
		"wspd": {"english": "8", "metric": "13"},
		"wdir": {"dir": "NNW", "degrees": "346"},
		"wx": "Partly Cloudy",
		"uvi": "0",
		"humidity": "81",
		"windchill": {"english": "-9999", "metric": "-9999"},
		"heatindex": {"english": "-9999", "metric": "-9999"},
		"feelslike": {"english": "48", "metric": "9"},
		"qpf": {"english": "0.0", "metric": "0"},
		"snow": {"english": "0.0", "metric": "0"},
		"pop": "0",
		"mslp": {"english": "29.78", "metric": "1008"}
		}
	]
})
        
    #weatherDict = eval(weather)['forecast']['simpleforecast']['forecastdaya ']
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
    request = Request('http://api.wunderground.com/api/0e060f345881cb0b/hourly/q/CA/la_canada.json')
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
    request = Request('http://api.wunderground.com/api/0e060f345881cb0b/forecast10day/q/CA/la_canada.json')
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
def plotData(data,yRecord,xRecord,coords,zoomPercent,xDisp):
    set_text_size(12)
    xStart = int(coords[0] - xDisp*zoomPercent)
    yStart = coords[1]
    width = coords[2]
    height = coords[3]
    yValue = []
    for i in data:
        yValue.append(int(i[yRecord]))
    tick      = int(width/len(data) * zoomPercent)
    print tick
    diff      = max(yValue)-min(yValue)
    smallest  = min(yValue) - ((diff)/4)
    largest   = max(yValue) + ((diff)/4)
    diff      = largest-smallest
    
    oldX      = xStart
    oldY      = int(yStart+height-(((height)/diff)*(yValue[0]-smallest)))
    y         = yStart
    x         = xStart
    for instance in data:
        set_color('black')
        yVar = int(instance[yRecord])
        icon = instance['icon']
        condition = instance['Conditions']
        y = int(yStart+height-((height/diff)*(yVar-smallest)))
        draw_line(oldX,oldY,x,y)
        iconImage = load_image('WeatherPic/'+icon+'.jpg')
        iconImage = resize_image(iconImage,tick,tick,RESIZE_FAST)
        draw_image(iconImage,x,yStart)
        index = data.index(instance)
        if instance[yRecord] != data[index-1][yRecord] or index == 0:
            draw_text(str(instance[yRecord]),x,y-15)
        if xRecord == 'Time':
            if int(instance['Time'].split(':')[0])%3 == 0:
                set_color(200,200,200)
                draw_line(x,yStart,x+1,yStart+height)
                draw_text(str(instance['Time']),x,yStart+height-30)
                set_color('white')
        else:
            set_color(200,200,200)
            draw_line(x,yStart,x+1,yStart+height)
            draw_text(str(instance[xRecord]),x,yStart+height-30)
            set_color('white')
        
        oldX = x
        oldY = y
        x = x + tick
def checkWifi():
    global forecastData, currData, hourData
    print 'checkwifi'
#    while wifi_get_state() != 'COMPLETED':
#        wifi_connect_transient_network('chromologic', False, 1, 'WPA-WPA2-PSK', password='41rainINspain02')        
def round_to(n, precision):
    correction = 0.5 if n >= 0 else -0.5
    return int( n/precision+correction ) * precision
    
    
def windArrow(windStrength,windDir,xOrigin,yOrigin,length):
    set_color('black')
    xTop = xOrigin - length
    yTop = yOrigin - length
    draw_rect(xTop,yTop,length*2,length*2)
    draw_line(xTop+length,yTop+15,xTop+length,yTop+length*2-15)
    draw_line(xTop,yTop+length+15,xTop+length*2-15,yTop+length)
    set_text_size(20)
    draw_text('N', xTop+length-30,yTop+10)
    draw_text('E', xTop+length*2-30,yTop+length-30)
    draw_text('S', xTop+length+10,yTop+length*2-30)
    draw_text('W', xTop+10,yTop+length+10)
    
    
    radDirection = math.radians(windDir)
    tipLength = length / 4
    endX = int(math.cos(radDirection)*length + xOrigin)
    endY = int(math.sin(radDirection)*length + yOrigin)
    draw_line(xOrigin,yOrigin,endX,endY)
    tipX1 = int(math.cos(math.radians(windDir-145))*tipLength + endX)
    tipY1 = int(math.sin(math.radians(windDir-145))*tipLength + endY)
    tipX2 = int(math.cos(math.radians(windDir+145))*tipLength + endX)
    tipY2 = int(math.sin(math.radians(windDir+145))*tipLength + endY)
    set_color('red')
    draw_line(endX,endY,tipX1,tipY1)
    draw_line(endX,endY,tipX2,tipY2)
    set_text_size(15)
    draw_text(str(windStrength) + ' mph',tipX2,tipY2)
    
#    def windArrow(windStrength,windDir,xOrigin,yOrigin,length):
def displayPage(currData,data,picker,zoomPercent,xDisp):
    
    clear_screen('white')
    interval = ['Time','Week Day'][picker]
    plotData(data,'Temp',interval,[boxTopX,boxTopY,boxLength,boxHeight],zoomPercent,xDisp)
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
    time        = str(now.hour%12) + now.strftime(':%M')
    
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
diffDatas   = []

def flipPage(currData,dataPicker,picker,zoomPercent,xDisp):
    set_drawing_image(bg)
    displayPage(currData,dataPicker,picker,zoomPercent,xDisp)
    set_drawing_image(None)
    draw_image(bg,0,0)

bg = None
def main():
    global diffDatas, bg  
    set_brightness(255)
    getWeather()
    diffDatas   = [hourData,forecastData]
    displayPage(currData,forecastData,1,1,0)
    bg = capture_image(0,0,800,480)
    txtFile     = open('LastData.txt', 'r')
    lines       = txtFile.readlines()
    txtFile.close()
    last        = float(lines[0])
    printedTime   = str(datetime.datetime.now().hour%12) + datetime.datetime.now().strftime(':%M')
    picker  = 1
    diffDatas   = [hourData,forecastData]
    diffDataPoints  = [['Day','Time','Temp','Conditions','Humidity','WSPD','QPF'],['Week Day','Date','Temp','Conditions']]
    first = True
    on = True
    swipeTime = time.time()
    zoomPercent = 1
    currTime = str(datetime.datetime.now().hour%12) + datetime.datetime.now().strftime(':%M')
    zoomFirst = True
    xDisp = 0
    while True:
        dataPoints = diffDataPoints[picker]
        multiTouch = touchscreen_finger_points_multitouch()
        if len(multiTouch) == 1:
            currTime = str(datetime.datetime.now().hour%12) + datetime.datetime.now().strftime(':%M')
            if not on:
                set_drawing_image(bg)
                displayPage(currData,diffDatas[picker],picker,zoomPercent,xDisp)
                
                scrub(x,y,dataPoints,picker)
                set_drawing_image(None)
                draw_image(bg,0,0)
                set_brightness(255)
                on = True
            x = multiTouch[0]['x']
            y = multiTouch[0]['y']
            if boxTopY + boxHeight > y > boxTopY and boxTopX < x < boxTopX + boxLength:
                if first:
                    firstY = y
                    first  = False
                lastTouch = time.time()
                set_drawing_image(bg)
                displayPage(currData,diffDatas[picker],picker,zoomPercent,xDisp)
                
                scrub(x,y,dataPoints,picker)
                set_drawing_image(None)
                draw_image(bg,0,0)
            elif y < 50:
                if first:
                    swipeFirstX = x
                    draw_rect(swipeFirstX-255,0,505,20,'red')
                    first  = False
                else:
                    if on:
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
            else:
                flipPage(currData,diffDatas[picker],picker,zoomPercent,xDisp)
        elif len(multiTouch) == 2:
            x1 = multiTouch[0]['x']
            y1 = multiTouch[0]['y']
            x2 = multiTouch[1]['x']
            y2 = multiTouch[1]['y']
            if boxTopY + boxHeight > y1 > boxTopY and boxTopX < x1 < boxTopX + boxLength and boxTopY + boxHeight > y2 > boxTopY and boxTopX < x2 < boxTopX + boxLength:
                if zoomFirst:
                    distanceInit= abs(x1-x2)
                    zoomXAvg =  (x1+x2)/2
                    zoomTime = time.time()
                    zoomFirst   = False
                    initXDisp = xDisp
                else:
                    xDisp = zoomXAvg - (initXDisp + ((x1+x2)/2))
                    print xDisp
                    distance    = abs(x1-x2)
                    distanceDiff= distance - distanceInit
                    zoomPercent = zoomPercent + (distanceDiff / 100.0)
                    print distanceDiff, zoomPercent
                    if xDisp < 0:
                        xDisp = 0
                    if xDisp > zoomPercent*(boxLength-1):
                        xDisp = zoomPercent*(boxLength-1)
                    if zoomPercent > 3:
                        zoomPercent = 3
                    if zoomPercent < 1:
                        zoomPercent = 1
                    flipPage(currData,diffDatas[picker],picker,zoomPercent,xDisp)
                    
                
        elif len(multiTouch) == 0 and time.time()-last > 3600:
            print 'new weather'
            txtFile = open('LastData.txt', 'w')
            txtFile.write('')
            txtFile.close()
            checkWifi()
            getWeather()
            flipPage(currData,diffDatas[picker],picker,zoomPercent,xDisp)
            printedTime = currTime
            txtFile = open('LastData.txt', 'r')
            lines = txtFile.readlines()
            txtFile.close()
            last = float(lines[0])
        elif printedTime != currTime:
            flipPage(currData,diffDatas[picker],picker,zoomPercent,xDisp)
            printedTime = currTime
        else:
            if not first:
                if time.time() - lastTouch > 0.2:
                    if y - firstY > 50:
                        picker = 1 - picker
                        zoomPercent = 1
                        flipPage(currData,diffDatas[picker],picker,zoomPercent,xDisp)
                    first = True
            if not zoomFirst:
                if time.time() - zoomTime > 0.2:
                    print 'zoomFirst = true'
                    zoomFirst = True
                    
        
        
def putToSleep(brightness):
    if brightness > 225:
        brightness = 225
    if brightness < 0:
        brightness = 0
    set_brightness(int(brightness))
    
#
#clear_screen('white')   
#plotData(forecastData,'temp','weekDay',[50,240,700,240])
#set_color('black')
#set_text_size(20)
#draw_text("TOUCH TO SEE WEATHER TODAY IN LA CANADA",10,10)

def scrub(x,y,dataPoints,picker):
    print 'scrub'
    infoBoxLength = 200
    infoBoxHeight = 120
    infoBoxX = x-infoBoxLength/2
    infoBoxY = boxTopY-infoBoxHeight/2
    
    draw_line(x,boxTopY,x,480,'blue')
    fill_rect(infoBoxX,infoBoxY,infoBoxLength,infoBoxHeight,'white')
    draw_rect(infoBoxX,infoBoxY,infoBoxLength,infoBoxHeight,'blue')
    spacing = int(boxLength/len(diffDatas[picker]))
    index = round_to((x-boxTopX)/spacing,1)
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
   

            
        
try:
    main()
except Exception,e:
    print e