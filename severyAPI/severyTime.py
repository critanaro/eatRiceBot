"north", "seibel", "baker", "sidrich", "south", "west"

dayToNum = {
	"U" : 0,
	"M" : 1,
	"T" : 2,
	"W" : 3,
	"R" : 4,
	"F" : 5,
	"S" : 6

}

mealToNum = {
	"breakfast" : 0,
	"brunch" : 1,
	"lunch" : 2,
	"dinner" : 3
}

#0 is sunday, 1 workday, 6 is saturday
serveryByDay =	{
	"0": [(), ("north", "south", "seibel", "west"), (), ("north", "south", "seibel", "west")],
	"1": [("north", "seibel", "baker", "sidrich", "south", "west"), (), ("north", "seibel", "baker", "sidrich", "south", "west"), ("north", "seibel", "baker", "sidrich", "south", "west")],
    "6": [("north", "seibel"), (), ("north", "seibel"), ("north", "seibel")]
}

serveryByTime = {
	"baker" : [[(), (), (), ()], [(timeFormat ("07:30:00"), timeFormat ("09:30:00")), (), (timeFormat ("11:30:00"), timeFormat ("13:30:00")), (timeFormat ("17:30:00"), timeFormat ("19:30:00"))], [(), (), (), ()]],
	"north" : [[(), (timeFormat ("11:30:00"), timeFormat ("14:00:00")), (), (timeFormat ("17:00:00"), timeFormat ("19:00:00"))], [(timeFormat ("07:30:00"), timeFormat ("09:30:00")), (), (timeFormat ("11:30:00"), timeFormat ("13:30:00")), (timeFormat ("17:30:00"), timeFormat ("19:30:00"))], [(timeFormat ("09:00:00"), timeFormat ("11:00:00")), (), (timeFormat ("11:30:00"), timeFormat ("2:00:00")), (timeFormat ("16:45:00"), timeFormat ("18:15:00"))]],
	"sidrich" : [[(), (), (), ()], [(timeFormat ("07:30:00"), timeFormat ("09:30:00")), (), (timeFormat ("11:30:00"), timeFormat ("13:30:00")), (timeFormat ("17:30:00"), timeFormat ("19:30:00"))], [(), (), (), ()]],
	"south" : [[(), (timeFormat ("11:30:00"), timeFormat ("14:00:00")), (), (timeFormat ("17:00:00"), timeFormat ("19:00:00"))], [(timeFormat ("07:30:00"), timeFormat ("09:30:00")), (), (timeFormat ("11:30:00"), timeFormat ("13:30:00")), (timeFormat ("17:30:00"), timeFormat ("19:30:00"))], [(), (), (), ()]],
	"west" : [[(), (timeFormat ("11:30:00"), timeFormat ("14:00:00")), (), (timeFormat ("17:00:00"), timeFormat ("19:00:00"))], [(timeFormat ("07:30:00"), timeFormat ("09:30:00")), (), (timeFormat ("11:30:00"), timeFormat ("13:30:00")), (timeFormat ("17:30:00"), timeFormat ("19:30:00"))], [(), (), (), ()]],
	"seibel" : [[(), (timeFormat ("11:30:00"), timeFormat ("14:00:00")), (), (timeFormat ("17:00:00"), timeFormat ("19:00:00"))], [(timeFormat ("07:30:00"), timeFormat ("09:30:00")), (), (timeFormat ("11:30:00"), timeFormat ("13:30:00")), (timeFormat ("17:30:00"), timeFormat ("19:30:00"))], [(timeFormat ("09:00:00"), timeFormat ("11:00:00")), (), (timeFormat ("11:30:00"), timeFormat ("2:00:00")), (timeFormat ("16:45:00"), timeFormat ("18:15:00"))]],
	
}

def getServeryTimeTable (serveryName):
	#input a string for servery name, return a list of tuple of time range, time in ms
	return serveryByTime[serveryName];


def filterByDay (time):
	#input a time string, return list of servery open during these day 
	current_day = timeFormat(time)[1];
	if (1 <= current_day and current_day <= 5):
		return serveryByDay[1]
	return serveryByDay[current_day]



def filterByTime (time):
	#input a time string, return list of servery open during these day
	current_time = timeFormat(time)[0]
	current_day = timeFormat(time)[1]

	available_severy = []
	open_today = filterByDay(time)
	for servery in open_today:
		if(CheckOneServery(time, servery)):
			available_severy.add(servery)
	return available_severy

def CheckOneServery (time, serveryName):
	#input a string for servery name, return a boolean
	current_time = timeFormat(time)[0]
	current_day = timeFormat(time)[1]
	current_servery_time = serveryByTime[serveryName]
	availability = False
	for meal in current_servery_time:
		if(time >= meal[0] and time <= meal[1]):
			availability = True
	return availability


def filterByMeal (time, mealName):
	#input a string fro meal name, breakfast, lunch, dinner, brunch, return a dictionary of servery as key and time range tuple as value
	current_day = timeFormat(time)[1]
	mealNum = mealToNum(mealName)
	open_today = filterByDay(time)

	available_severy = []
	for servery in open_today:
		if(serveryByTime[servery][mealNum]):
			available_severy.add(servery)
	return available_severy


def timeFormat (time):
	#input: a string, 2018-09-15T00:00:00.000-05:00, output: (miliseconds after 00:00:00.000, dayNumber)
	
	raw_time = time[12:20]
	formated_time = hmsToMs(raw_time)
	day = dayToNum(time[10:11]);

	return (formated_time, dayNumber)

def hmsToMs (time):
	#input: a string, 00:00:00, output: a integer, miliseconds after 00:00:00.000
	
	hrs, mins, secs = time.split(':')
	formated_time = int(hrs)*360000 + int(mins) * 6000 + int(sec) * 100

	return formated_time



	
