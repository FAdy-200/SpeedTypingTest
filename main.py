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
        self.__font = pygame.font.Font("freesansbold.ttf", 20)
        self.__mouse = pygame.mouse.get_pos()
        self.__stats = []  # can be anything or just spread it out to multiple variables if needed
        self.__time = 0  # will be changed in the initializeTypingTest
        self.__realTimeStat = False

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
        pass

    def __renderScreen(self):
        """
        factory to choose which screen to render
        :return:
        """

    def main(self):
        """
        main program loop
        :return:
        """
        while True:
            self.__eventHandler()
            self.__screen.fill((245, 245, 245))
            self.__renderScreen()
            self.__statistics()
            pygame.display.flip()


test = SpeedTester()
test.main()
