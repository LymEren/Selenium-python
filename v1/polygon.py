# Eyyub Eren - Polygon

myPoly = []
takeSide = True
sideCounter = 0
while takeSide:
    mySide = input(f"Enter {sideCounter+1}. side length(cm) or press e to finish: ")
    if str(mySide).isnumeric() and sideCounter <= 5:
        myPoly.append(mySide)
        sideCounter += 1
        if sideCounter == 5:
            takeSide = False
    elif mySide == 'e':
        takeSide = False
    else:
        print("Wrong Input!")

match sideCounter:
    case 1:
        radius = int(myPoly[0])
        print("\nFull circle:\n")
        for valOne in range(2 * radius + 1):
            for valTwo in range(2 * radius + 1):

                xPoint = valOne - radius
                yPoint = valTwo - radius
                square = (xPoint ** 2) + (yPoint ** 2)
                if square <= (radius ** 2) + 1:
                    # I used the end parameter as i don't want a new line
                    print("*", end="  ")
                else:
                    print(" ", end="  ")
            print()

        print("\nRing:\n")
        for valOne in range(2 * radius + 1):
            for valTwo in range(2 * radius + 1):

                xPoint = valOne - radius
                yPoint = valTwo - radius
                square = (xPoint ** 2) + (yPoint ** 2)

                if square - 3 <= (radius ** 2) <= square + 3:
                    print("*", end="  ")
                else:
                    print(" ", end="  ")
            print()
    case 2:
        print("There is no 2-sided polygon!")
    case 3:
        for value in range(int(myPoly[0]) + 1):
            print(" " * (int(myPoly[0]) - value) + "*" * (2 * value - 1))
    case 4:
        if int(myPoly[0]) == int(myPoly[1]):
            print("\nIts Square!\n")
        elif int(myPoly[0]) != int(myPoly[1]) and int(myPoly[1]) == int(myPoly[3]):
            print("\nIts Rectangle!\n")
        for valOne in range(int(myPoly[1])):
            print("*  " * int(myPoly[0]))
    case 5:
        for value in range(int(myPoly[0]) + 1):
            print(" " * (int(myPoly[0]) - value) + "*" * (2 * value - 1))
        for value in range(int(myPoly[1])-1,2,-1):
            print(" " * (int(myPoly[1]) - value ) + "*" * (2 * value -1))

