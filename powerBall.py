import random

powerball = [1, 3, 4, 7, 8, 9]
print(random.choice(powerball))

powerball2 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 40, 41, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 64, 65, 66, 67, 68, 69]
print(random.choice(powerball2))
print(random.choice(powerball2))
print(random.choice(powerball2))
print(random.choice(powerball2))






def powerBall():

    #return 5 numbers from 1 to 69, these are for the white balls
        for i in range(5):
            yield random.randint(10, 59)
    #return 1 number from 1 to 26, this is for the red ball
        yield random.randint(1, 26)

for powerBall_number in powerBall():
        print ('The power ball number is ', powerBall_number)

redball = [4, 7, 11, 19]
print(random.choice(redball))
