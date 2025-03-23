import random
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
total_trip_distance = 2000
current_day = 1
current_month = 3
player_distance = 0
player_health = 5
player_food = 500
player_name = ""
game_over = False 


while game_over==False: 
    print("Welcome to the Oregon Trail. You can do the following moves are rest ,quit ,moving , and hunt."
        if user_input == "Hunt":
        player_food += 100
    elif user_input == "Quit":
        game_over = True
    elif user_input == "Moving":
        global player_distance
        travelled = random.randint(30,60)
        days = random.randint(3,7)
    elif user_input == "Rest":
        global player_health
        days = random.randint(2,5)

    if player_health  < 5:
        player_health += 1



def dailyUpdate(days):
    global player_food
    global player_health

    for day in range(days):
        # Move clock
        addDay()
        # Consume 5lbs of food
        player_food -= 5
        # 5% chance of drop in health
        if isHealthDecreased():
            player_health -= 1
def addDay():
    global current_day
    global current_month
    global MONTHS_WITH_31_DAYS

    # 1 Find out how many days are in the month
    days_in_month = 30
    if current_month in MONTHS_WITH_31_DAYS:
        days_in_month = 31

    # Increase the day

    # Is it greater than the number of days in the month?
    #   Yes : Increase month by 1 and set day to 1
    #   No  : Still in same month, it's all good
    if current_day > days_in_month:
        current_month += 1
        current_day = 1
    elif current_day < days_in_month:
        current_month = 1
        current_day +=1

def isHealthDecreased():
    return random.randint(1,100) <= 5

def dailyUpdate(days):
    global player_food
    global player_health



for i in range(10):
    dailyUpdate(5)
    print(current_month,'/', current_day)
    print(player_health, player_food)
    print("")

def travel():
    '''
        moves you randomly between 30-60 miles and 
                     takes 3-7 days (random).
    '''
    global player_distance
    travelled = random.randint(30,60)
    days = random.randint(3,7)

    print("Days Travelled:", days)
    print("Miles Travelled:", travelled)

    player_distance += travelled

    dailyUpdate(days)

def rest():
    '''
    increases health 1 level (up to 5 maximum) and 
                 takes 2-5 days (random).    
    '''
    global player_health
    days = random.randint(2,5)

    if player_health  < 5:
        player_health += 1

    dailyUpdate(days)

def hunt():
    '''
        adds 100 lbs of food and takes 2-5 days (random).
    '''
    global player_food
    days = random.randint(2,5)

    player_food += 100

    dailyUpdate(days)

def status():
    pass

def help():
    pass




