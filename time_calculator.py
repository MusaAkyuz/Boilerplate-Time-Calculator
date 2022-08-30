def add_time(start, duration, startDay="noDay"):

    '''
      Just converting  inputs
      for use in codes
     '''
    #days list
    daysLower = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # days case insensitive
    startDay = startDay.lower()
    #last two words mean AM or PM
    amOrPm = start[-2:]
    #split with : to understand hour and minute
    splitStart = start.split(":")
    # '3:10 PM' converting ['3', '10 PM']
    startHour = int(splitStart[0])
    startMinute = int(splitStart[1][:2])
    #split with : to understand hour and minute
    splitDuration = duration.split(":")
    # '205:45' converting ['205', '45']
    durationHour = int(splitDuration[0])
    durationMinute = int(splitDuration[1])
  
    # initialize values
    nextDay = 0 # to output format 
    howManyTimesChange = 0 # for am pm situation

    # calculates final time with checking
    totalHour = startHour + durationHour
    totalMinute = startMinute + durationMinute


    # add extra day each 24 hour
    nextDay = nextDay + (durationHour // 24)

    # add extra hour if minute is bigger than 59
    # and recalculate minute
    if totalMinute > 59:
        totalHour = totalHour + 1
        totalMinute = totalMinute % 60

    #fill with zeros if minute only have one digit
    # 2 minute ---> 02 minute
    totalMinute = str(totalMinute).zfill(2)

    
    if totalHour >= 12:
        #changing AM or PM situation for each hour jumping 12
        if (totalHour % 24) >= 12:
            howManyTimesChange = howManyTimesChange + 1
        for i in range (howManyTimesChange):
            amOrPm = changeAMPM(amOrPm)
        if amOrPm == "AM" and (howManyTimesChange % 2) == 1:
            nextDay = nextDay + 1
          
        # converts 24 to 12 hour type
        totalHour = totalHour % 12
        # if final hour equal 0
        # convert 12
        if totalHour == 0:
            totalHour = "12"

    '''
        All output format codes
    '''
    if startDay in daysLower:
        index = daysLower.index(startDay)
        index = (index + nextDay) % 7
        new_time = f"{totalHour}:{totalMinute} {amOrPm}, {days[index]}"
        if nextDay == 1:
            new_time = f"{totalHour}:{totalMinute} {amOrPm}, {days[index]} (next day)"
        elif nextDay > 1:
            new_time = f"{totalHour}:{totalMinute} {amOrPm}, {days[index]} ({nextDay} days later)"
    else:
        new_time = f"{totalHour}:{totalMinute} {amOrPm}"
        if nextDay == 1:
            new_time = f"{totalHour}:{totalMinute} {amOrPm} (next day)"
        elif nextDay > 1:
            new_time = f"{totalHour}:{totalMinute} {amOrPm} ({nextDay} days later)"

    return new_time

# changes am pm situation function
def changeAMPM(amOrPm):
    if amOrPm == "AM":
        return "PM"
    if amOrPm == "PM":
        return "AM"