from playsound import playsound

X = True
Y = 1000

while X:
    print(Y)
    Y = Y - 1
    if Y == 0:
        X = False
        print("boom")
        playsound("Explosion.mp3")