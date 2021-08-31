import random
import math

def Probability(rating1,rating2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10,1.0*(rating1-rating2)/400))

def EloRating(Ra, Rb, K, d,Ta,Tb):

    Pb = Probability(Ra, Rb)

    Pa = Probability(Rb, Ra)

    if (d == 1):
        Ra = Ra + K * (1 - Pa)
        Rb = Rb + K * (0 - Pb)


    else:
        Ra = Ra + K * (0 - Pa)
        Rb = Rb + K * (1 - Pb)

    print("Updated Ratings:-")
    print(Ta, " =", round(Ra, 6), " ", Tb, " =", round(Rb, 6))
    return [round(Ra, 6), round(Rb, 6)]

fAlbumsUsed = open("albums","r")
albumsUsed = fAlbumsUsed.read().split(",")
fAlbumsUsed.close()
trackList = []
eloList = []
for x in albumsUsed:
    fItemSet = open("AlbumSet/" + x, "r")
    itemSet = fItemSet.read().split(",")
    i = 0
    for x in itemSet:
        if i % 2 == 0:
            if(x != ''):
                trackList.append(x)
        else:
            if(x != ''):
                eloList.append(float(x))
        i += 1
    fItemSet.close()
print(trackList)
print(eloList)
print(len(trackList))
print(len(eloList))

inputText = ""

K = 30
indexOfA = 0
indexOfB = 0
winnerStay = 0
previousWinner = 0

print("Should the winner stay? (yes or no)")
if input() == "yes":
    winnerStay = 1
else:
    winnerStay = 0

while(inputText != "End"):
    print("------NEW PAIRING-----")
    if winnerStay == 0:
        indexOfA = random.randint(0, len(trackList) - 1)
        indexOfB = random.randint(0, len(trackList) - 1)
        while (indexOfB == indexOfA):
            indexOfB = random.randint(0, len(trackList) - 1)
    elif winnerStay == 1 & previousWinner == 1:
        indexOfB = random.randint(0, len(trackList) - 1)
        while(indexOfB == indexOfA):
            indexOfB = random.randint(0, len(trackList) - 1)
    else:
        indexOfA = random.randint(0, len(trackList) - 1)
        while(indexOfB == indexOfA):
            indexOfA = random.randint(0, len(trackList) - 1)


    trackA = trackList[indexOfA]
    trackB = trackList[indexOfB]
    eloA = eloList[indexOfA]
    eloB = eloList[indexOfB]
    print(trackA," __VS__ ",trackB)
    inputText = input()
    if(inputText == "End"):
        break
    elif inputText == "a":
        changes = EloRating(float(eloA),float(eloB),K,1,trackA,trackB)
        previousWinner = 1
    else:
        changes = EloRating(float(eloA),float(eloB),K,0,trackA,trackB)
        previousWinner = 0
    eloList[indexOfA] = changes[0]
    eloList[indexOfB] = changes[1]

print("-----------------------------------------------------------")
yz = zip(eloList, trackList)
yx = sorted(yz)
yx.reverse()
for x in range(len(yx)):
    print(yx[x])

for x in albumsUsed:
    f = open("AlbumSet/"+x,"w")
    f.close()

for x in yx:
    trackAlbum=x[1].split(" - ")[1]
    fTrack= open("AlbumSet/"+trackAlbum,"a")
    fTrack.write(x[1]+","+str(x[0])+",")
    fTrack.close()