import pygame
import time
import sys
import random


class SpeedTester:
    def __init__(self):
        """
        initializes all the needed elements e.g pictures/time/pygame window
        and all needed  attributes
        """
        pygame.init()
        self.__width, self.__height = 700, 480
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption("Typing Speed Test")
        self.__icon = pygame.image.load("icon.svg")
        pygame.display.set_icon(self.__icon)
        self.__font = pygame.font.Font("MADE Sunflower PERSONAL USE.otf", 58)
        self.__welcome_img = pygame.image.load("Welcome_img.png")
        self.__sentences = open("sentences.txt", "r").readlines()
        self.__text = ''.join(random.choice(self.__sentences))
        self.__pts = 0
        self.__stats = [0,0]  # can be anything or just spread it out to multiple variables if needed
        self.__time = 0  # will be changed in the initializeTypingTest
        self.__time2 = 0
        self.__realTimeStat = False
        self.__screenToBeRendered = "M"
        self.__typed = ""
        self.__shift = False
        self.__caps = -1
        self.__backspace = False
        self.__backspaceTime = 200
        self.__mainButton = [160, 160 + 346, 160, 160 + 76]  # x1,x2,y1,y2 of the start button in the main screen
        self.__resetButton = [300, 420, 350, 470]  # x1,x2,y1,y2 of the reset button in the last screen

    def __eventHandler(self):
        """
        handles the events that happen on screen e.g. mouse pos/clicks and user input
        :return:
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.__mouePressHandler()
            if event.type == pygame.KEYDOWN:
                self.__keyPressesHandler(event)
            if event.type == pygame.KEYUP:
                self.__backspace = False
                self.__backspaceTime = 70
                self.__shift = False

    def __mouePressHandler(self):
        self.__mouse = pygame.mouse.get_pos()
        # print(self.__mouse)  # uncomment this to see the position of the mouse when it is clicked
        if self.__screenToBeRendered == "M":
            if self.__mainButton[0] < self.__mouse[0] < self.__mainButton[1]:
                if self.__mainButton[2] < self.__mouse[1] < self.__mainButton[3]:
                    self.__initializeTypingTest()
                    self.__time = time.time()
                    self.__screenToBeRendered = "T"
        elif self.__screenToBeRendered == "D":
            if self.__resetButton[0] < self.__mouse[0] < self.__resetButton[1]:
                if self.__resetButton[2] < self.__mouse[1] < self.__resetButton[3]:
                    self.__initializeTypingTest()
                    self.__time = time.time()
                    self.__screenToBeRendered = "T"

    def __backspaceHandler(self):
        if self.__backspace:
            if self.__backspaceTime == 0:
                self.__backspaceTime = 70
                self.__typed = self.__typed[:-1]
            self.__backspaceTime -= 1


    def __keyPressesHandler(self, event):
        pressed = pygame.key.get_pressed()
        press = pygame.key.name(event.key)
        if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
            self.__shift = True
        if press == "caps lock":
            self.__caps *= -1
        if self.__shift:
            press = press.upper()
        if self.__caps > 0:
            press = press.swapcase()
        if press != "space" and press != "SPACE":
            if press != "return" and press != "RETURN":
                if press != "backspace" and press != "BACKSPACE":
                    if press != "LEFT SHIFT" and press != "RIGHT SHIFT" and len(press) == 1 and press != "CAPS LOCK":
                        self.__typed += press
                        self.__shift = False
                        self.__backspace = False
                elif not self.__backspace:
                    self.__backspaceTime = 70
                    self.__backspace = True
                    self.__typed = self.__typed[:-1]
            else:
                self.__time2 = time.time()
                self.__typingChecker()
        else:
            self.__typed += " "

    def __typingChecker(self):
        """
        checks if the user has inputted the right characters
        :return:
        """
        for i in range(len(self.__text)):
            try:
                if self.__text[i] == self.__typed[i]:
                    self.__pts += 1
            except IndexError:  # User hasnot completed the sentence
                break
        self.__statistics()

    def __statistics(self):
        """
        calculates the statistics
        :return:
        """
        correctness = (self.__pts / len(self.__text)) * 100
        speed = abs(self.__time2 - self.__time)
        self.__stats[0] , self.__stats[1] = correctness, speed
        self.__screenToBeRendered = 'D'

    def __statisticsRenderer(self):
        """
        renders the calculated statistics
        :return:
        """
        pass

    def __initializeTypingTest(self):
        """
        resets the statistics and the typing challenge
        :return:
        """
        self.__typed = ""
        self.__text = ''.join(random.choice(self.__sentences))
        self.__pts = 0

    def __typingScreen(self):
        """
        renders the typing screen with it is needed elements
        :return:
        """
        title = self.__font.render("Type the sentence below:", True, (64, 78, 128))
        self.__screen.blit(title, (5, 10))
        font = pygame.font.Font("MADE Sunflower PERSONAL USE.otf", 23)
        self.__screen.blit(font.render(self.__text, True, (0, 0, 0)), (10, 100))
        img = font.render(self.__typed, True, (0, 0, 0))
        rect = pygame.Rect((10, 200), (self.__width - 20, img.get_height() + 10))
        pygame.draw.rect(self.__screen, (255, 191, 0), rect, 1)
        self.__screen.blit(img, (10, 205))

    def __testDoneScreen(self):
        """
        renders the end screen with it is needed elements
        :return:
        """
        self.__screen.blit(self.__font.render("Results", True, (64, 78, 128)), (self.__width // 3, 10))
        img = pygame.image.load("results.svg")
        img = pygame.transform.scale(img, (150, 150))
        self.__screen.blit(img, ((2 * self.__width) // 3, 0))
        font = pygame.font.Font("MADE Sunflower PERSONAL USE.otf", 40)
        self.__screen.blit(font.render("Accuracy: " + f"{self.__stats[0]:.2f}%", True, (64, 78, 128)), (20, 150))
        self.__screen.blit(font.render("Speed: " + f"{self.__stats[1]:.2f}secs.", True, (64, 78, 128)), (20, 220))
        self.__screen.blit(pygame.transform.scale(pygame.image.load("reset.svg"), (120, 120)), (300, 350))
        self.__screen.blit(self.__font.render("Reset?", True, (64, 78, 128)), (250, 280))

    def __mainScreen(self):
        """
        renders the main screen so the user does not just start typing right away
        and there is a welcome screen
        :return:
        """
        self.__screen.blit(self.__welcome_img, (230, 270))
        title = self.__font.render("Welcome to Typing", True, (64, 78, 128))
        title2 = self.__font.render("Speed Test!", True, (64, 78, 128))
        text = self.__font.render("Click to Start", True, (255, 191, 0), (235, 235, 235))
        # print(text.get_size())
        self.__screen.blit(title, (70, 10))
        self.__screen.blit(title2, (180, 70))
        self.__screen.blit(text, (160, 160))

    def __renderScreen(self):
        """
        factory to choose which screen to render
        :return:
        """
        if self.__screenToBeRendered == "M":
            self.__mainScreen()
        elif self.__screenToBeRendered == "T":
            self.__typingScreen()
        elif self.__screenToBeRendered == "D":
            self.__testDoneScreen()

    def main(self):
        """
        main program loop
        :return:
        """
        while True:
            self.__eventHandler()
            self.__backspaceHandler()
            self.__screen.fill((245, 245, 245))
            self.__renderScreen()
            pygame.display.flip()


test = SpeedTester()
test.main()
