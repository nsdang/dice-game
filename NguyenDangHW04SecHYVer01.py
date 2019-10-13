# Project:      Lab7 (NguyenDangLab07SecHYVer01.py)
# Name:         Dang Song Nguyen
# Date:         08/11/17
# Description:  This program will create a graphics window program
#               that will display the 5 side of a dice.


# Import the graphics library
from graphics import*


#########################################
##### Define a function drawing dot #####
#########################################

def Dot(CenterPoint,win):
    dot = Circle(CenterPoint,12)
    dot.setFill('Red')
    dot.setOutline('purple3')
    return dot.draw(win)



#################################################################
##### Define 6 functions draw 6 sides (just dots) of a dice #####
#################################################################

def Dot1(i,win):
    Dot(Point(110+i*150,110),win)

def Dot2(i,win):
    for a in [Point(80+i*150,139),Point(140+i*150,80)]:
        Dot(a,win)

def Dot4(i,win):
    for a in [Point(80+i*150,80),Point(140+i*150,140),Point(80+i*150,139),Point(140+i*150,80)]:
        Dot(a,win)

def Dot6(i,win):
    for a in [Point(80+i*150,110),Point(140+i*150,110)]:
        Dot(a,win)
    Dot4(i,win)


##############################################################
### Define a function that generate the random dice number ###
##############################################################
import random
def Random():
    NumberOfDot = random.randint(1, 6)
    return NumberOfDot



########################################################
#### Define a function draw fully 6 sides of a dice ####
########################################################
    
def Dice(i,win):

    # Draw the white dice
    dice = Rectangle(Point(50+i*150,50),Point(169+i*150,169))
    dice.setFill('White')
    dice.draw(win)

    # This generates a random integer between and including 1 and 6
    NumberOfDot = Random()
        

    # Draw the dots
    if NumberOfDot == 1:
        Dot1(i,win)
    elif NumberOfDot == 2:
        Dot2(i,win)
    elif NumberOfDot == 3:
        Dot1(i,win)
        Dot2(i,win)
    elif NumberOfDot == 4:
        Dot4(i,win)
    elif NumberOfDot == 5:
        Dot1(i,win)
        Dot4(i,win)
    else: 
        Dot6(i,win)
    return NumberOfDot



###########################################
############  MAIN FUNCTION  ##############
###########################################

def main():

    # Create a graphics window and set its background
    win = GraphWin('RollDice',835,400)
    win.setBackground('Wheat')

    # Create 5 dices' respective outlined areas
    for i in range(5):
        area = Rectangle(Point(45+i*150,45),Point(174+i*150,174))
        area.setFill('Wheat')
        area.setOutline('Light Steel Blue')
        area.setWidth(5)
        area.draw(win)
        
    # Create and print out the Dice Total
    intDiceTotal = 0
    strResult = 'Dice Total: ' + str(intDiceTotal)
    result = Text(Point(110,200),strResult)
    result.setStyle('bold')
    result.setSize(15)
    result.draw(win)
    
    for i in range(5):
        blnRun1 = True
        while blnRun1 == True:
                
            # Pause the program while waiting for a mouse click
            diceclick = win.getMouse()
            intX = diceclick.getX()
            intY = diceclick.getY()
            if 45+i*150 <= intX <= 174+i*150 and 45 <= intY <= 174 :

                # Draw the whole dice
                NumberOfDot = Dice(i,win)
                intDiceTotal += NumberOfDot

                # Undraw the old result and draw the new one
                result.undraw()
                strResult = 'Dice Total: ' + str(intDiceTotal)
                result = Text(Point(110+i*150,200),strResult)
                result.setStyle('bold')
                result.setSize(15)
                result.draw(win)
                
                blnRun1 = False
            else:
                blnRun1 = True
                
    # Display a greeting if player get 20 score
    if intDiceTotal >= 20:
        strGreet = Text(Point(400,300),'CONGRATULATION!\n You are really lucky')
        strGreet.setSize(15)
        strGreet.setStyle('bold italic')
        strGreet.setTextColor('Red')
        strGreet.draw(win)
    else:
        strGreet = Text(Point(400,300),'Good luck next time!')
        strGreet.setSize(15)
        strGreet.setStyle('bold italic')
        strGreet.setTextColor('Red')
        strGreet.draw(win)

    # Create a 'EXIT' button
    btnExit = Rectangle(Point(695,275),Point(775,325))
    btnExit.setFill('Light Steel Blue')
    btnExit.setWidth('5')
    btnExit.draw(win)
    strExit = Text(Point(735,300),'EXIT')
    strExit.setSize(12)
    strExit.setStyle('bold italic')
    strExit.setTextColor('Red1')
    strExit.draw(win)
    
    # Click on Exit button to quit
    blnRun2 = True
    while blnRun2 == True:     
        Exit = win.getMouse()
        exitX = Exit.getX()
        exitY = Exit.getY()
        if 695 <= exitX <= 775 and 275 <= exitY <= 325 : 
            blnRun2 = False
            win.close()
        else:
            blnRun2 = True         

main()
    
