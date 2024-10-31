import data
import hw2
import unittest

class TestCases(unittest.TestCase):
    # Part 1
    def testCreateRectangle1(self):
        pointOne = data.Point(5, 0)
        pointTwo = data.Point(9, 3)
        result = hw2.create_rectangle(pointOne, pointTwo)
        expected = data.Rectangle(data.Point(5, 3), data.Point(9, 0))
        self.assertEqual(result, expected)

    def testCreateRectangle2(self):
        pointOne = data.Point(3, 5)
        pointTwo = data.Point(2, -8)
        result = hw2.create_rectangle(pointOne, pointTwo)
        expected = data.Rectangle(data.Point(2, 5), data.Point(3, -8))
        self.assertEqual(result, expected)

    # Part 2
    def testShorterDurationThan1(self):
        dur1 = data.Duration(11, 34)
        dur2 = data.Duration(9, 23)
        result = hw2.shorter_duration_than(dur1, dur2)
        expected = False
        self.assertEqual(result, expected)

    def testShorterDurationThan2(self):
        dur1 = data.Duration(5, 4)
        dur2 = data.Duration(5, 5)
        result = hw2.shorter_duration_than(dur1, dur2)
        expected = True
        self.assertEqual(result, expected)

    # Part 3
    def testSongShorterThan1(self):
        length = data.Duration(5, 52)
        songOne = data.Song('The Weeknd', 'Save Your Tears', data.Duration(6, 32))
        songTwo = data.Song('Tyler, The Creator', 'See You Again', data.Duration(4, 55))
        songThree = data.Song('Travis Scott', 'goosebumps', data.Duration(2, 11))
        songList = [songOne, songTwo, songThree]
        result = hw2.song_shorter_than(songList, length)
        expected = [songTwo, songThree]
        self.assertEqual(result, expected)


    def testSongsShorterThan2(self):
        length = data.Duration(3, 4)
        songOne = data.Song('Baby Keem', 'Honest', data.Duration(1, 0))
        songTwo = data.Song('Kendrick Lamar', 'Humble', data.Duration(3, 4))
        songThree = data.Song('Travis Scott', 'goosebumps', data.Duration(2, 11))
        songList = [songOne, songTwo, songThree]
        result = hw2.song_shorter_than(songList, length)
        expected = [songOne, songThree]
        self.assertEqual(result, expected)


    # Part 4
    def testRunningTime1(self):
        songOne = data.Song("The Weeknd", 'Save Your Tears', data.Duration(15, 23))
        songTwo = data.Song("Tyler, The Creator", 'See You Again', data.Duration(5, 2))
        songThree = data.Song('Travis Scott', 'goosebumps', data.Duration(2, 23))
        songList = [songOne, songTwo, songThree]
        idx = [2, 2, 1, 0, 2]
        result = hw2.running_time(songList, idx)
        expected = data.Duration(27, 34)
        self.assertEqual(result, expected)

    def testRunningTime2(self):
        songOne = data.Song("Kendrick Lamar", 'Humble', data.Duration(7, 54))
        songTwo = data.Song("Baby Keem", 'Honest', data.Duration(3, 49))
        songThree = data.Song('21 Savage', 'redrum', data.Duration(6, 2))
        songList = [songOne, songTwo, songThree]
        idx = [1, 0, 2, 0, 1]
        result = hw2.running_time(songList, idx)
        expected = data.Duration(29, 28)
        self.assertEqual(result, expected)

   # Part 5

    def testValidateRoute1(self):
        cityLinks = [
                    ['san luis obispo', 'santa margarita'],
                     ['san luis obispo', 'pismo beach'],
                     ['atascadero', 'santa margarita'],
                     ['atascadero', 'creston']
                     ]
        cityNames = ['pismo beach', 'creston']
        result = hw2.validate_route(cityLinks, cityNames)
        expected = False
        self.assertEqual(result, expected)


    def testValidateRoute2(self):
        cityLinks = [
                    ['san luis obispo', 'santa margarita'],
                     ['san luis obispo', 'pismo beach'],
                     ['atascadero', 'santa margarita'],
                     ['atascadero', 'creston']
                     ]
        cityNames = ['creston', 'atascadero', 'santa margarita']
        result = hw2.validate_route(cityLinks, cityNames)
        expected = True
        self.assertEqual(result, expected)

    # Part 6
    def testLongestRepetition1(self):
        nums = [4, 2, 5, 5, 5, 5, 2, 2, 2, 4, 4, 4]
        result = hw2.longest_repetition(nums)
        expected = 2
        self.assertEqual(expected, result)

    def testLongestRepetition2(self):
        nums = [9]
        result = hw2.longest_repetition(nums)
        expected = 0
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
