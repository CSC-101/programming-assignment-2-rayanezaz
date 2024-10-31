import data
from data import Point, Duration, Song, Rectangle

# Part 1

'''''
This function determines the top left and bottom right points of any two given points, and then
returns a Rectangle object. The input is two points (pointOne, pointTwo) of type Point. The output
is a rectangle with the top left and bottom right points figured out.
'''''
def create_rectangle(pointOne: data.Point, pointTwo: data.Point) -> data.Rectangle:
    if pointOne.x > pointTwo.x:
        right = pointOne.x
        left = pointTwo.x
    else:
        right = pointTwo.x
        left = pointOne.x

    if pointOne.y > pointTwo.y:
        top = pointOne.y
        bottom = pointTwo.y
    else:
        top = pointTwo.y
        bottom = pointOne.y

    top_left = Point(left, top)
    bottom_right = Point(right, bottom)
    rectangle = data.Rectangle(top_left, bottom_right)
    return rectangle

# Part 2

'''''
This function compares to durations in order to determine if the first one is shorter than the second.
The input is two durations (durOne, durTwo) of type Duration. The output returns True if dur1 is less
than dur2, and returns False if dur1 is greater than dur2.
'''''''''
def shorter_duration_than(durOne: data.Duration, durTwo: data.Duration) -> bool:
    totalSecondsOne = (durOne.minutes * 60) + durOne.seconds
    totalSecondsTwo = (durTwo.minutes * 60) + durTwo.seconds
    return totalSecondsOne < totalSecondsTwo


# Part 3

'''
This function has a list of songs, and essentially cuts down and returns the songs with a duration that is
less than the given maximum duration. The input is a list of songs as well as a maximum duration. The output
is a list of songs that are shorter than the maximum duration time.
'''
def song_shorter_than(songs: list[data.Song], limLength: data.Duration) -> list:
    if songs == []:
        return []
    return [track for track in songs if shorter_duration_than(track.duration, limLength)]


# Part 4

''''
This function does math to calculate the total playing time of the given songs in a playlist. The input is a
list of songs and a list of indexes that the playlist. The output is a Duration object that represents the
total running time.
'''''
def running_time(songList: list[Song], songOrder: list[int]) -> data.Duration:
    minutes = 0
    seconds = 0
    for x in songOrder:
        minutes += songList[x].duration.minutes
        seconds += songList[x].duration.seconds
    # Convert total seconds to minutes and remaining seconds
    minutes += (seconds // 60)
    seconds %= 60
    return Duration(minutes, seconds)


# Part 5

'''
This function returns a boolean that will evaluate to see if there is a direct route between values in a list.
The input of this is a list of cities and a list of wanted cities that need to be checked for a direct route.
The output of this is a boolean. It evaluates to True if there is a direct route, and evaluates to False if there isn't
'''
def validate_route(cityLinks: list[list[str]], cityNames: list[str]) -> bool:
    if not cityLinks:
        return False
    for x in range(len(cityNames) - 1):
        # Check for direct connection in either direction
        if not ([cityNames[x], cityNames[x + 1]] in cityLinks or [cityNames[x + 1], cityNames[x]] in cityLinks):
            return False
    return True


# Part 6

'''''''''
This function takes in a list of numbers and then it finds the index of the first occurence of the longest repetition
of a specific number. The input of this is a list of numbers or integers, and then the output is an int that represents
the index value for the inputted list.
'''''''''
def longest_repetition(value: list[int]) -> int:
    if not value:
        return None
    sum = 1
    largest = 1
    index = 0
    for x in range(len(value) - 1):
        if value[x] == value[x + 1]:
            sum += 1
            if sum > largest:
                index = (x + 2) - sum
                largest = sum
        else:
            sum = 1
    return index

