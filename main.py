import datetime
import requests
import random
import time
import multiprocessing
from LinksToCrawl import *
from cLottoDraw import cLottoDrawOld
from multiprocessing import Process, Manager
from bs4 import BeautifulSoup

def MakeSoup(CPU, URL):
    heads = [
        {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"},
        {"User-Agent": "Lynx/2.8.4rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.6c"},
        {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"},
        {"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36"},
        {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36"},
        {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"},
        {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"},
        {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"}
    ]

    try:
        Bot = True
        i = 0
        while Bot:
            IntHeader = random.randint(0, int(len(heads)))
            if IntHeader == 8:
                IntHeader = IntHeader - 1
            headers = heads[IntHeader]

            sleep = 0
            if (i >= 0) and (i < 5):
                sleep = round(random.uniform(2.1, 5.0), 2)
            if (i >= 5) and (i < 10) and (sleep == 0):
                sleep = round(random.uniform(4.1, 7.0), 2)
            if (i >= 10) and (i < 50) and (sleep == 0):
                sleep = round(random.uniform(8.1, 11.0), 2)
            if (i >= 50) and (sleep == 0):
                sleep = round(random.uniform(12.1, 14.0), 2)
            time.sleep(sleep)
            i += 1
            Bot = False

            page = requests.get(URL, headers=headers)
            pagePlainText = page.content
            pageSoup = BeautifulSoup(pagePlainText, "html.parser")

            '''
            SoupTitle = str(pageSoup.title.text)
            SoupTitle = SoupTitle.replace("\n", "")
            SoupTitle = SoupTitle.lstrip()
            SoupTitle = SoupTitle.rstrip()
            if (SoupTitle == "Bot Check") or (SoupTitle == "Tut uns Leid!"):
                print("(" + str(CPU) + ")" + " " + "Blocked: " + str(i) + " Try" + " (Sleep " + str(sleep) + ")")
                Bot = True
            '''

        return pageSoup

    except:
        print("")

    return pageSoup

allOldLottoDraws = []
allMidLottoDraws = []
allModLottoDraws = []

def getOldDraws(CPU):
    for i, OldLottoDrawLink in enumerate(OldLottoDrawLinks):
        try:
            OldLottoDrawLinkSoup = MakeSoup(1, OldLottoDrawLink)
            Draws = OldLottoDrawLinkSoup.find("div", {"id":"lottobox"})
            Draws = Draws.findAll("p")
            Year = OldLottoDrawLink[-7:]

            for j, Draw in enumerate(Draws):
                if "Ziehung vom" in str(Draw.text):
                    thisDate = Draw.text
                    thisDraws = Draw.findNext().text
                    thisBonusNumber = Draw.findNext().findNext().text
                    if ("Ziehung vom" in thisBonusNumber) or ("\n" in thisBonusNumber):
                        thisBonusNumber = "nA"

                    newLottoDrawOld = cLottoDrawOld.cLottoDrawOld(Draw)
                    newLottoDrawOld.findDate(thisDate)
                    newLottoDrawOld.findWinningNumbers(thisDraws)
                    newLottoDrawOld.findPullDraw(thisDraws)
                    newLottoDrawOld.findBonusNumber(thisBonusNumber)

                    allOldLottoDraws.append(newLottoDrawOld)

        except:
            print()

    #allLottoDrawsOld = sorted(allOldLottoDraws, key=lambda cLottoDraw: int(cLottoDraw.getYear()))
    #allLottoDrawsOld = sorted(allOldLottoDraws, key=lambda cLottoDraw: int(cLottoDraw.getMonth()), reverse=True)

def getMidDraws(CPU):
    for i, MidLottoDrawLink in enumerate(MidLottoDrawLinks):
        try:
            print()

        except:
            print()

def getModDraws(CPU):
    for i, ModLottoDrawLink in enumerate(ModernLottoDrawLinks):
        try:
            print()

        except:
            print()

if __name__ == "__main__":
    startTime = time.time()
    print("\n### Started ###\n")

    numberOfCPUs = multiprocessing.cpu_count()

    getOldDraws(1)
    getMidDraws(1)
    getModDraws(1)

    '''
    manager = Manager()
    ManagedLottoDrawYearURLs = manager.list(allLottoDrawYearURLs)
    Intervall = math.floor(lenghtLottoDrawYearURLs / numberOfCPUs)

    Processes = []

    #getDraws(1, allLottoDrawYearURLs, 0, 7)

    for v in range(numberOfCPUs):
        start = Intervall * v
        end = (Intervall * (v + 1))

        if v < numberOfCPUs - 1:
            p = Process(target=getDraws,
                        args=(v + 1, ManagedLottoDrawYearURLs, start, end))
        else:
            p = Process(target=getDraws,
                        args=(v + 1, ManagedLottoDrawYearURLs, start, lenghtLottoDrawYearURLs))
        p.start()
        Processes.append(p)

    for p in Processes:
        p.join()
    '''

    print("\n### Finished ###\n")
    elapsedTime = time.time() - startTime
    print(elapsedTime)










