playerID = input("Enter player ID: ")

try:
    games = int(input("Enter number of games (5 to 10): "))
except ValueError:
    print("Text not allowed, please enter a number: ")
    quit()

while games < 5 or games > 10:
    games = int(input("Enter a number from 5 to 10: "))

totalTime = 0
highestScore = 0


for game in range(games):
    try:
        score = int(input("Enter score: "))
        time = int(input("Enter time in minutes (5 to 60): "))
    except ValueError:
        print("Text not allowed, please enter a number: ")
        quit()

    if time < 5 or time > 60:
        print("Time is invalid: ")
        quit()

    totalTime = totalTime + time

    if score > highestScore:
        highestScore = score

averageTime = round(totalTime / games)

print("Player ID:", playerID)
print("Highest score:", highestScore)
print("Average time:", averageTime, "minutes")