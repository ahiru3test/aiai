# Tetromino (a Tetris clone)
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

# KRT 17/06/2012 rewrite event detection to deal with mouse use

#import random, time, pygame, sys
import random, time, sys
#from pygame.locals import *
import tkinter as tk

FPS = 25
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOXSIZE = 20
BOARDWIDTH = 10
BOARDHEIGHT = 20
BLANK = '.'

MOVESIDEWAYSFREQ = 0.15
MOVEDOWNFREQ = 0.1

XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5

#               R    G    B
#WHITE       = (255, 255, 255)
#GRAY        = (185, 185, 185)
#BLACK       = (  0,   0,   0)
#RED         = (155,   0,   0)
#LIGHTRED    = (175,  20,  20)
#GREEN       = (  0, 155,   0)
#LIGHTGREEN  = ( 20, 175,  20)
#BLUE        = (  0,   0, 155)
#LIGHTBLUE   = ( 20,  20, 175)
#YELLOW      = (155, 155,   0)
#LIGHTYELLOW = (175, 175,  20)

WHITE       = ("#FFFFFF",)
GRAY        = ("#B9B9B9",)
BLACK       = ("#000000",)
RED         = ("#9B0000",)
LIGHTRED    = ("#AF1414",)
GREEN       = ("#009B00",)
LIGHTGREEN  = ("#14AF14",)
BLUE        = ("#00009B",)
LIGHTBLUE   = ("#1414AF",)
YELLOW      = ("#9B9B00",)
LIGHTYELLOW = ("#AFAF14",)

BORDERCOLOR = BLUE
BGCOLOR = BLACK
TEXTCOLOR = GRAY
TEXTSHADOWCOLOR = GRAY
COLORS      = (     BLUE,      GREEN,      RED,      YELLOW)
LIGHTCOLORS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)
assert len(COLORS) == len(LIGHTCOLORS) # each color must have light color

TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5

fallFreq = 0.25 # TBD
S_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]

Z_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]

I_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]

O_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

J_SHAPE_TEMPLATE = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]

L_SHAPE_TEMPLATE = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]

T_SHAPE_TEMPLATE = [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}

class MyWindow(tk.Frame):
    def __init__(self, master=None, size=(640,400)):
        super().__init__(master, width=size[0], height=size[1])
        self.pack()
        self.create_widgets(size)

    def create_widgets(self, size):
        # setup variables for the start of the game
        self.board = self.getBlankBoard()
        self.lastMoveDownTime = time.time()
        self.lastMoveSidewaysTime = time.time()
        self.lastFallTime = time.time()
        self.movingDown = False # note: there is no movingUp variable
        self.movingLeft = False
        self.movingRight = False
        self.score = 0
        self.level, self.fallFreq = self.calculateLevelAndFallFreq(self.score)

        self.fallingPiece = self.getNewPiece()
        self.nextPiece = self.getNewPiece()
        self.kb_event = ""
        self.interval = 3000

        # Bind keyboard event
        self.bind("<Key>", self.key)
        self.focus_set()

        # Create canvas
        self.canvas  = tk.Canvas(self, width = size[0], height = size[1], bg=WHITE)
        self.canvas.place(x=0, y=0)

        #Call runGame
        self.runGame()

    def runGame(self):
        #Run every 0.25 seconds
        if self.fallingPiece == None:
            # No falling piece in play, so start a new piece at the top
            self.fallingPiece = self.nextPiece
            self.nextPiece = self.getNewPiece()
            self.lastFallTime = time.time() # reset lastFallTime

            if not self.isValidPosition(self.board, self.fallingPiece):
                self.showTextScreen("Game Over")
                return # can't fit a new piece on the board, so game over

        #checkForQuit()
        # handle moving the piece because of user input
        # moving the piece sideways
        kb = self.kb_event
        self.kb_event = ""
        if kb == "Left" and self.isValidPosition(self.board, self.fallingPiece, adjX=-1):
            self.fallingPiece['x'] -= 1
            self.movingLeft = True
            self.movingRight = False
            self.lastMoveSidewaysTime = time.time()
        elif kb == "Right" and self.isValidPosition(self.board, self.fallingPiece, adjX=1):
            self.fallingPiece['x'] += 1
            self.movingRight = True
            self.movingLeft = False
            self.lastMoveSidewaysTime = time.time()

        # rotating the piece (if there is room to rotate)
        elif kb == "CW":
                self.fallingPiece['rotation'] = (self.fallingPiece['rotation'] + 1) % len(PIECES[self.fallingPiece['shape']])
                if not self.isValidPosition(self.board, self.fallingPiece):
                    self.fallingPiece['rotation'] = (self.fallingPiece['rotation'] - 1) % len(PIECES[self.fallingPiece['shape']])
        elif kb == "CCW": # rotate the other direction
            self.fallingPiece['rotation'] = (self.fallingPiece['rotation'] - 1) % len(PIECES[self.fallingPiece['shape']])
            if not self.isValidPosition(self.board, self.fallingPiece):
                self.fallingPiece['rotation'] = (self.fallingPiece['rotation'] + 1) % len(PIECES[self.fallingPiece['shape']])

        # making the piece fall faster with the down key
        elif kb == "Down":
            self.movingDown = True
            if self.isValidPosition(self.board, self.fallingPiece, adjY=1):
                self.fallingPiece['y'] += 1
            self.lastMoveDownTime = time.time()

        # move the current piece all the way down
        elif kb == "Space":
                self.movingDown = False
                self.movingLeft = False
                self.movingRight = False
                for i in range(1, BOARDHEIGHT):
                    if not self.isValidPosition(self.board, self.fallingPiece, adjY=i):
                        break
                self.fallingPiece['y'] += i - 1

        """
        if (self.movingLeft or self.movingRight) and time.time() - self.lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
            if self.movingLeft and self.isValidPosition(self.board, self.fallingPiece, adjX=-1):
                self.fallingPiece['x'] -= 1
            elif self.movingRight and self.isValidPosition(self.board, self.fallingPiece, adjX=1):
                self.fallingPiece['x'] += 1
            self.lastMoveSidewaysTime = time.time()
        """
        if self.movingDown and time.time() - self.lastMoveDownTime > MOVEDOWNFREQ and self.isValidPosition(self.board, self.fallingPiece, adjY=1):
            self.fallingPiece['y'] += 1
            self.lastMoveDownTime = time.time()

        # let the piece fall if it is time to fall
        if time.time() - self.lastFallTime > fallFreq:
            # see if the piece has landed
            if not self.isValidPosition(self.board, self.fallingPiece, adjY=1):
                # falling piece has landed, set it on the board
                self.addToBoard(self.board, self.fallingPiece)
                self.score += self.removeCompleteLines(self.board)
                self.level, self.fallFreq = self.calculateLevelAndFallFreq(self.score)
                self.fallingPiece = None
            else:
                # piece did not land, just move the piece down
                self.fallingPiece['y'] += 1
                self.lastFallTime = time.time()

        # drawing everything on the screen
        #DISPLAYSURF.fill(BGCOLOR)
        # Clear all canvas
        self.canvas.delete('all')
        self.drawBoard(self.board)
        self.drawStatus(self.score, self.level)
        self.drawNextPiece(self.nextPiece)
        if self.fallingPiece != None:
            self.drawPiece(self.fallingPiece)

        #pygame.display.update()
        #FPSCLOCK.tick(FPS)
        #25 FPS
        self.after(self.interval, self.runGame)
        if self.interval > 10000//FPS:
            self.interval = 10000//FPS
            self.showTextScreen("Tketromino")

    def key(self, event):
        # handle moving the piece because of user input
        # moving the piece sideways
        if event.char == "j" or event.keysym == "Left":
            self.kb_event = "Left"
        elif event.char == "k" or event.keysym == "Right":
            self.kb_event = "Right"

        # rotating the piece (if there is room to rotate)
        elif (event.char == "w" or event.keysym == "Up"):
            self.kb_event = "CW"
        elif (event.char == "q"): # rotate the other direction
            self.kb_event = "CCW"

        # making the piece fall faster with the down key
        elif (event.char == "s" or event.keysym == "Down"):
            self.kb_event = "Down"

        # move the current piece all the way down
        elif event.char == " ":
            self.kb_event = "Space"

    """
    def makeTextObjs(text, font, color):
        surf = font.render(text, True, color)
        return surf, surf.get_rect()
    """
    """
    def terminate():
        pygame.quit()
        sys.exit()
    """
    """
    # KRT 17/06/2012 rewrite event detection to deal with mouse use
    def checkForKeyPress():
        for event in pygame.event.get():
            if event.type == QUIT:      #event is quit
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:   #event is escape key
                    terminate()
                else:
                    return event.key   #key found return with it
        # no quit or key events in queue so return None
        return None
    """


    ##def checkForKeyPress():
    ##    # Go through event queue looking for a KEYUP event.
    ##    # Grab KEYDOWN events to remove them from the event queue.
    ##    checkForQuit()
    ##
    ##    for event in pygame.event.get([KEYDOWN, KEYUP]):
    ##        if event.type == KEYDOWN:
    ##            continue
    ##        return event.key
    ##    return None


    def showTextScreen(self, text):
        # This function displays large text in the
        # center of the screen until a key is pressed.
        # Draw the text drop shadow
        #titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTSHADOWCOLOR)
        #titleRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
        #DISPLAYSURF.blit(titleSurf, titleRect)
        self.canvas.create_text(int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2), text=text, font=('FixedSys',48),fill = TEXTCOLOR)
        # Draw the text
        #titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTCOLOR)
        #titleRect.center = (int(WINDOWWIDTH / 2) - 3, int(WINDOWHEIGHT / 2) - 3)
        #DISPLAYSURF.blit(titleSurf, titleRect)
        self.canvas.create_text(int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2), text=text, font=('FixedSys',48),fill = TEXTCOLOR)

        # Draw the additional "Press a key to play." text.
        #pressKeySurf, pressKeyRect = makeTextObjs('Press a key to play.', BASICFONT, TEXTCOLOR)
        #pressKeyRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 100)
        #DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

        #while checkForKeyPress() == None:
            #pygame.display.update()
            #FPSCLOCK.tick()

    """
    def checkForQuit(self):
        for event in pygame.event.get(QUIT): # get all the QUIT events
            terminate() # terminate if any QUIT events are present
        for event in pygame.event.get(KEYUP): # get all the KEYUP events
            if event.key == K_ESCAPE:
                terminate() # terminate if the KEYUP event was for the Esc key
            pygame.event.post(event) # put the other KEYUP event objects back
    """

    def calculateLevelAndFallFreq(self, score):
        # Based on the score, return the level the player is on and
        # how many seconds pass until a falling piece falls one space.
        level = int(score / 10) + 1
        fallFreq = 0.27 - (level * 0.02)
        return level, fallFreq

    def getNewPiece(self):
        # return a random new piece in a random rotation and color
        shape = random.choice(list(PIECES.keys()))
        newPiece = {'shape': shape,
                    'rotation': random.randint(0, len(PIECES[shape]) - 1),
                    'x': int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2),
                    'y': -2, # start it above the board (i.e. less than 0)
                    'color': random.randint(0, len(COLORS)-1)}
        return newPiece


    def addToBoard(self, board, piece):
        # fill in the board based on piece's location, shape, and rotation
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                    self.board[x + piece['x']][y + piece['y']] = piece['color']


    def getBlankBoard(self):
        # create and return a new blank board data structure
        self.board = []
        for i in range(BOARDWIDTH):
            self.board.append([BLANK] * BOARDHEIGHT)
        return self.board


    def isOnBoard(self, x, y):
        return x >= 0 and x < BOARDWIDTH and y < BOARDHEIGHT


    def isValidPosition(self, board, piece, adjX=0, adjY=0):
        # Return True if the piece is within the board and not colliding
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                isAboveBoard = y + piece['y'] + adjY < 0
                if isAboveBoard or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                    continue
                if not self.isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
                    return False
                if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
                    return False
        return True

    def isCompleteLine(self, board, y):
        # Return True if the line filled with boxes with no gaps.
        for x in range(BOARDWIDTH):
            if board[x][y] == BLANK:
                return False
        return True


    def removeCompleteLines(self, board):
        # Remove any completed lines on the board, move everything above them down, and return the number of complete lines.
        numLinesRemoved = 0
        y = BOARDHEIGHT - 1 # start y at the bottom of the board
        while y >= 0:
            if self.isCompleteLine(board, y):
                # Remove the line and pull boxes down by one line.
                for pullDownY in range(y, 0, -1):
                    for x in range(BOARDWIDTH):
                        board[x][pullDownY] = board[x][pullDownY-1]
                # Set very top line to blank.
                for x in range(BOARDWIDTH):
                    board[x][0] = BLANK
                numLinesRemoved += 1
                # Note on the next iteration of the loop, y is the same.
                # This is so that if the line that was pulled down is also
                # complete, it will be removed.
            else:
                y -= 1 # move on to check next row up
        return numLinesRemoved


    def convertToPixelCoords(self, boxx, boxy):
        # Convert the given xy coordinates of the board to xy
        # coordinates of the location on the screen.
        return (XMARGIN + (boxx * BOXSIZE)), (TOPMARGIN + (boxy * BOXSIZE))


    def drawBox(self, boxx, boxy, color, pixelx=None, pixely=None):
        # draw a single box (each tetromino piece has four boxes)
        # at xy coordinates on the board. Or, if pixelx & pixely
        # are specified, draw to the pixel coordinates stored in
        # pixelx & pixely (this is used for the "Next" piece).
        if color == BLANK:
            return
        if pixelx == None and pixely == None:
            pixelx, pixely = self.convertToPixelCoords(boxx, boxy)
        #pygame.draw.rect(DISPLAYSURF, COLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1))
        #pygame.draw.rect(DISPLAYSURF, LIGHTCOLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 4, BOXSIZE - 4))
        self.canvas.create_rectangle(pixelx + 1, pixely + 1, pixelx + 1 + BOXSIZE - 1, pixely + 1 + BOXSIZE - 1, fill = COLORS[color])
        self.canvas.create_rectangle(pixelx + 1, pixely + 1, pixelx + 1 + BOXSIZE - 4, pixely + 1 + BOXSIZE - 4, fill = LIGHTCOLORS[color])

    def drawBoard(self, board):
        # draw the border around the board
        #pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (XMARGIN - 3, TOPMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 5)
        self.canvas.create_rectangle( XMARGIN - 3, TOPMARGIN - 7, XMARGIN + (BOARDWIDTH * BOXSIZE) + 8, TOPMARGIN + (BOARDHEIGHT * BOXSIZE) + 8, fill = BORDERCOLOR)

        # fill the background of the board
        #pygame.draw.rect(DISPLAYSURF, BGCOLOR, (XMARGIN, TOPMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))
        self.canvas.create_rectangle(XMARGIN, TOPMARGIN, XMARGIN + BOXSIZE * BOARDWIDTH, TOPMARGIN + BOXSIZE * BOARDHEIGHT, fill = BGCOLOR)
        # draw the individual boxes on the board
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                self.drawBox(x, y, board[x][y])


    def drawStatus(self, score, level):
        # draw the score text
        #scoreSurf = BASICFONT.render('Score: %s' % score, True, TEXTCOLOR)
        #scoreRect = scoreSurf.get_rect()
        #scoreRect.topleft = (WINDOWWIDTH - 150, 20)
        #DISPLAYSURF.blit(scoreSurf, scoreRect)
        self.canvas.create_text(WINDOWWIDTH - 150, 20, text = 'Score: ' + str(score), font=('FixedSys',20, 'bold'),fill=TEXTCOLOR)

        # draw the level text
        #levelSurf = BASICFONT.render('Level: %s' % level, True, TEXTCOLOR)
        #levelRect = levelSurf.get_rect()
        #levelRect.topleft = (WINDOWWIDTH - 150, 50)
        #DISPLAYSURF.blit(levelSurf, levelRect)
        self.canvas.create_text(WINDOWWIDTH - 150, 50, text = 'Level: ' + str(level), font=('FixedSys',20, 'bold'),fill=TEXTCOLOR)



    def drawPiece(self, piece, pixelx=None, pixely=None):
        shapeToDraw = PIECES[piece['shape']][piece['rotation']]
        if pixelx == None and pixely == None:
            # if pixelx & pixely hasn't been specified, use the location stored in the piece data structure
            pixelx, pixely = self.convertToPixelCoords(piece['x'], piece['y'])

        # draw each of the boxes that make up the piece
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if shapeToDraw[y][x] != BLANK:
                    self.drawBox(None, None, piece['color'], pixelx + (x * BOXSIZE), pixely + (y * BOXSIZE))


    def drawNextPiece(self, piece):
        # draw the "next" text
        #nextSurf = BASICFONT.render('Next:', True, TEXTCOLOR)
        #nextRect = nextSurf.get_rect()
        #nextRect.topleft = (WINDOWWIDTH - 120, 80)
        #DISPLAYSURF.blit(nextSurf, nextRect)
        # draw the "next" piece
        self.canvas.create_text(WINDOWWIDTH - 120, 80, text = 'Next: ', font=('FixedSys', 20, 'bold'),fill=TEXTCOLOR)
        self.drawPiece(piece, pixelx=WINDOWWIDTH-120, pixely=100)


def main():
    root=tk.Tk()
    root.title("Tketromino")
    w = MyWindow(master=root, size=(WINDOWWIDTH,WINDOWHEIGHT))

    # Call Main loop
    try:
        import pygame
        pygame.init()
        if random.randint(0, 1) == 0:
            pygame.mixer.music.load('tetrisb.mid')
        else:
            pygame.mixer.music.load('tetrisc.mid')
        pygame.mixer.music.play(-1, 0.0)
        w.mainloop()
        pygame.mixer.music.stop()
    except:
        w.mainloop()

if __name__=="__main__":
    main()
