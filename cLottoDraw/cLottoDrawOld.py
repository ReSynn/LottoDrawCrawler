import datetime
from cLottoDraw import cLottoDraw

class cLottoDrawOld(cLottoDraw.cLottoDraw):
    def findDate(self, DateSoup):
        Date = DateSoup[-10:]
        for i, Split in enumerate(Date.split(".")):
            if i == 0:
                Day = Split
                self.setDay(Day)
            if i == 1:
                Month = Split
                self.setMonth(Month)
            if i == 2:
                Year = Split
                self.setYear(Year)

        EnglishDate = Year + " " + Month + " " + Day
        self.findWeekDay(EnglishDate)

    def findWeekDay(self, EnglishDate):
        WeekDay = datetime.datetime.strptime(EnglishDate, "%Y %m %d").strftime("%A")

        if WeekDay == "Monday":
            WeekDay = "Montag"

        if WeekDay == "Tuesday":
            WeekDay = "Dienstag"

        if WeekDay == "Wednesday":
            WeekDay = "Mittwoch"

        if WeekDay == "Thursday":
            WeekDay = "Donnerstag"

        if WeekDay == "Friday":
            WeekDay = "Freitag"

        if WeekDay == "Saturday":
            WeekDay = "Samstag"

        if WeekDay == "Sunday":
            WeekDay = "Sonntag"

        self.setWeekDay(WeekDay)

    def findWinningNumbers(self, thisDrawsString):
        WinNumbers = thisDrawsString[14:41]
        WinNumbers = WinNumbers.replace(" ","")
        WinningNumbers = []
        WiningNumbersString = ""
        for i, Split in enumerate(WinNumbers.split("-")):
            WinningNumbers.append(Split)
            WiningNumbersString = WiningNumbersString + Split

        self.setWinNumber1(WinningNumbers[0])
        self.setWinNumber2(WinningNumbers[1])
        self.setWinNumber3(WinningNumbers[2])
        self.setWinNumber4(WinningNumbers[3])
        self.setWinNumber5(WinningNumbers[4])
        self.setWinNumber6(WinningNumbers[5])
        self.setWinDraw(WiningNumbersString)

    def findPullDraw(self, thisDrawsString):
        PullNumbers = thisDrawsString[-31:]
        PullNumbers = PullNumbers.replace(" ","")
        for k, char in enumerate(PullNumbers):
            if char is "(":
                PullNumbers = PullNumbers[k:]
                break

        PullNumbers = PullNumbers.replace("(", "")
        PullNumbers = PullNumbers.replace(")", "")
        PulledDraw = ""
        for i, Split in enumerate(PullNumbers.split("-")):
            length = len(Split)
            if length == 1:
                Split = "0" + Split

            PulledDraw = PulledDraw + Split

        self.setPullDraw(PulledDraw)

    def findBonusNumber(self, thisBonusNumberString):
        BonusNumber = thisBonusNumberString[-2:]
        BonusNumber = BonusNumber.replace(" ", "")
        length = len(BonusNumber)
        if length == 1:
            BonusNumber = "0" + BonusNumber

        self.setBonusNumber(BonusNumber)


'''
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
self.__BonusNumber = "0"
self.__SuperNumber = "0"
'''