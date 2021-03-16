import pygame
import time
import sys


class SpeedTester:
    def __init__(self):
        """
        initializes all the needed elements e.g pictures/time/pygame window
        and all needed  attributes
        """
        pygame.init()
        self.__width, self.__height = 680, 480
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption("Typing Speed Test")
        self.__icon = pygame.image.load("icon.png")
        pygame.display.set_icon(self.__icon)
        self.__font = pygame.font.Font("Bogart-Bold-trial.ttf", 50)
        self.__welcome_img = pygame.image.load("welcome_img.png")
        self.__mouse = pygame.mouse.get_pos()
        self.__stats = []  # can be anything or just spread it out to multiple variables if needed
        self.__time = 0  # will be changed in the initializeTypingTest
        self.__realTimeStat = False
        self.__screenToBeRendered = "M"
        self.__typed = ""
        self.__mainButton = [160, 160 + 346, 160, 160 + 76]  # x1,x2,y1,y2 of the start button in the main screen
        self.__resetButton = [0, 0, 0, 0]  # x1,x2,y1,y2 of the reset button in the last screen

    def __statistics(self):
        """
        calculates the statistics
        :return:
        """
        pass

    def __statisticsRenderer(self):
        """
        renders the calculated statistics
        :return:
        """
        pass

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

    def __mouePressHandler(self):
        self.__mouse = pygame.mouse.get_pos()
        # print(self.__mouse)  # uncomment this to see the position of the mouse when it is clicked
        if self.__screenToBeRendered == "M":
            if self.__mainButton[0] < self.__mouse[0] < self.__mainButton[1]:
                if self.__mainButton[2] < self.__mouse[1] < self.__mainButton[3]:
                    self.__initializeTypingTest()
                    self.__screenToBeRendered = "T"
        elif self.__screenToBeRendered == "D":
            if self.__resetButton[0] < self.__mouse[0] < self.__resetButton[1]:
                if self.__resetButton[2] < self.__mouse[1] < self.__resetButton[3]:
                    self.__initializeTypingTest()
                    self.__screenToBeRendered = "T"

    def __keyPressesHandler(self, event):
        press = pygame.key.name(event.key)
        if press != "space":
            if press != "return":
                if press != "backspace":
                    self.__typed += press
                else:
                    self.__typed = self.__typed[:-1]
            else:
                self.__typed += "\n"
        else:
            self.__typed += " "

    def __typingChecker(self):
        """
        checks if the user has inputted the right characters
        :return:
        """
        pass

    def __initializeTypingTest(self):
        """
        resets the statistics and the typing challenge
        :return:
        """
        pass

    def __testDoneScreen(self):
        """
        renders the end screen with it is needed elements
        :return:
        """
        pass

    def __typingScreen(self):
        """
        renders the typing screen with it is needed elements
        :return:
        """
        pass

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
            self.__screen.fill((245, 245, 245))
            self.__statistics()
            self.__renderScreen()
            pygame.display.flip()


test = SpeedTester()
test.main()
