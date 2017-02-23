class cLottoDraw():
    def __init__(self, LottoDrawSoup):
        self.__LottoDrawSoup = LottoDrawSoup
        self.__Day = "0"
        self.__Month = "0"
        self.__Year = "0"
        self.__WeekDay = ""
        self.__WinNumber1 = "0"
        self.__WinNumber2 = "0"
        self.__WinNumber3 = "0"
        self.__WinNumber4 = "0"
        self.__WinNumber5 = "0"
        self.__WinNumber6 = "0"
        self.__WinDraw = "0"
        self.__PullDraw = "0"
        self.__BonusNumber = "nA"
        self.__SuperNumber = "nA"

    def getLottoDrawSoup(self):
        return self.__LottoDrawSoup

    def getDay(self):
        return self.__Day

    def getMonth(self):
        return self.__Month

    def getYear(self):
        return self.__Year

    def getWeekDay(self):
        return self.__WeekDay

    def getWinNumber1(self):
        return self.__WinNumber1

    def getWinNumber2(self):
        return self.__WinNumber2

    def getWinNumber3(self):
        return self.__WinNumber3

    def getWinNumber4(self):
        return self.__WinNumber4

    def getWinNumber5(self):
        return self.__WinNumber5

    def getWinNumber6(self):
        return self.__WinNumber6

    def getWinDraw(self):
        return self.__WinDraw

    def getPullDraw(self):
        return self.__PullDraw

    def getBonusNumber(self):
        return self.__BonusNumber

    def getSuperNumber(self):
        return self.__SuperNumber

    def setDay(self, Day):
        self.__Day = Day

    def setMonth(self, Month):
        self.__Month = Month

    def setYear(self, Year):
        self.__Year = Year

    def setWeekDay(self, WeekDay):
        self.__WeekDay = WeekDay

    def setWinNumber1(self, WinNumber1):
        self.__WinNumber1 = WinNumber1

    def setWinNumber2(self, WinNumber2):
        self.__WinNumber2 = WinNumber2

    def setWinNumber3(self, WinNumber3):
        self.__WinNumber3 = WinNumber3

    def setWinNumber4(self, WinNumber4):
        self.__WinNumber4 = WinNumber4

    def setWinNumber5(self, WinNumber5):
        self.__WinNumber5 = WinNumber5

    def setWinNumber6(self, WinNumber6):
        self.__WinNumber6 = WinNumber6

    def setWinDraw(self, WinDraw):
        self.__WinDraw = WinDraw

    def setPullDraw(self, PullDraw):
        self.__PullDraw = PullDraw

    def setBonusNumber(self, BonusNumber):
        self.__BonusNumber = BonusNumber

    def setSuperNumber(self, SuperNumber):
        self.__SuperNumber = SuperNumber

    def writeToCSVFile(self, CPU):
        FileWrite = open(str(CPU) + " - CSVLottoDraws" + ".txt", "a")
        FileWrite.write(str(self.getYear()) + ', ' +
                        str(self.getMonth()) + ', ' +
                        str(self.getDay()) + ', ' +
                        str(self.getWinNumber1()) +  ', ' +
                        str(self.getWinNumber2()) + ', ' +
                        str(self.getWinNumber3()) + ', ' +
                        str(self.getWinNumber4()) + ', ' +
                        str(self.getWinNumber5()) + ', ' +
                        str(self.getWinNumber6()) + ', ' +
                        str(self.getBonusNumber()) + ', ' +
                        str(self.getSuperNumber()) + ', ' +
                        str(self.getWinDraw()) + ', ' +
                        str(self.getPullDraw()) + ', ' +
                        str(self.getWeekDay()) + '\n')
        FileWrite.close()

    def writeToTABFile(self, CPU):
        FileWrite = open(str(CPU) + " - TABLottoDraws" + ".txt", "a")
        FileWrite.write(str(self.getYear()) + '\t' +
                        str(self.getMonth()) + '\t' +
                        str(self.getDay()) + '\t' +
                        str(self.getWinNumber1()) + '\t' +
                        str(self.getWinNumber2()) + '\t' +
                        str(self.getWinNumber3()) + '\t' +
                        str(self.getWinNumber4()) + '\t' +
                        str(self.getWinNumber5()) + '\t' +
                        str(self.getWinNumber6()) + '\t' +
                        str(self.getBonusNumber()) + '\t' +
                        str(self.getSuperNumber()) + '\t' +
                        str(self.getWinDraw()) + '\t' +
                        str(self.getPullDraw()) + '\t' +
                        str(self.getWeekDay()) + '\n')
        FileWrite.close()
