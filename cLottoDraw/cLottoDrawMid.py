import re
from cLottoDraw import cLottoDraw

class cLottoDrawMid(cLottoDraw.cLottoDraw):
    def findDate(self, thisDateString):
        thisDateString = thisDateString[-10:]
        for i, Split in enumerate(thisDateString.split(".")):
            if i == 0:
                Day = Split
                self.setDay(Day)
            if i == 1:
                Month = Split
                self.setMonth(Month)
            if i == 2:
                Year = Split
                self.setYear(Year)

    def findWeekDay(self, thisDateString):
        thisDateString = thisDateString[:-12]
        thisDateString = thisDateString[12:]
        thisDateString = str(thisDateString)
        thisDateString = thisDateString.lstrip()
        thisDateString = thisDateString.rstrip()
        self.setWeekDay(thisDateString)

    def findWinningNumbers(self, thisWinDrawString):
        WinningNumbers = []
        WinningNumbersString = ""

        thisWinDrawString = str(thisWinDrawString)
        thisWinDrawString = " ".join(thisWinDrawString.split())

        for i, Split in enumerate(thisWinDrawString.split(" ")):
            length = len(Split)
            if length == 1:
                Split = "0" + Split
            WinningNumbers.append(Split)
            WinningNumbersString = WinningNumbersString + Split

        WinningNumbersString = WinningNumbersString.replace(" ", "")

        self.setWinNumber1(WinningNumbers[0])
        self.setWinNumber2(WinningNumbers[1])
        self.setWinNumber3(WinningNumbers[2])
        self.setWinNumber4(WinningNumbers[3])
        self.setWinNumber5(WinningNumbers[4])
        self.setWinNumber6(WinningNumbers[5])
        self.setWinDraw(WinningNumbersString)

    def findPullDraw(self, thisPullDrawString):
        thisPullDrawString = str(thisPullDrawString)
        thisPullDrawString = thisPullDrawString[20:]
        if "live" in thisPullDrawString:
            thisPullDrawString = thisPullDrawString[:-30]
        thisPullDrawString = thisPullDrawString.strip()

        PulledDraw = ""
        for i, Split in enumerate(thisPullDrawString.split("-")):
            Split = Split.strip()
            length = len(Split)
            if length == 1:
                Split = "0" + Split
            PulledDraw = PulledDraw + Split

        PulledDraw = PulledDraw.replace(" ","")
        self.setPullDraw(PulledDraw)

    def findBonusNumber(self, thisBonusNumberString):
        thisBonusNumberString = thisBonusNumberString[3:]
        length = len(thisBonusNumberString)
        if length == 1:
            thisBonusNumberString = "0" + thisBonusNumberString

        self.setBonusNumber(thisBonusNumberString)

    def findSuperNumber(self, thisSuperNumberString):
        thisSuperNumberString = thisSuperNumberString[3:]
        length = len(thisSuperNumberString)
        if length == 1:
            thisSuperNumberString = "0" + thisSuperNumberString

        if " - " in thisSuperNumberString:
            thisSuperNumberString = "nA"

        self.setSuperNumber(thisSuperNumberString)