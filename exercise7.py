#Exercise 7

def how_far(person_id):
    print('How far did person {} run (in metres)?'.format(person_id))
    return float(input())

def how_long(person_id, distance):
    print('How long (in minutes) did it take person {} to run {} metres?'.format(person_id, distance))
    return float(input())

def get_speed(min, distance):
    return round((distance / (min * 60)),4)



def test_runners():
    distance1 = how_far(1)
    mins1 = how_long(1, distance1)
    speed1 = get_speed(mins1, distance1)

    distance2 = how_far(2)
    mins2 = how_long(2, distance2)
    speed2 = get_speed(mins2, distance2)

    distance3 = how_far(3)
    mins3 = how_long(3, distance3)
    speed3 = get_speed(mins3, distance3)

    
    


test_runners()