import csv
import matplotlib.pyplot as plt

# read CSV function
def readCSV(name):
    with open(name, "r") as f:
        read = csv.reader(f)
        myList = [i for i in read]
        myList.remove(myList[0])
    return myList

# a class to process data
class call:

    def __init__(self, CALLER, CALLED, CALL_TIME, CONNECTION_TIME, CONNECTION_FINISH_TIME, CALL_DURATION_SEC,
                 FINISH_REASON, COST):

        self.CALLER = CALLER
        self.CALLED = CALLED
        self.CALL_TIME = CALL_TIME
        self.CONNECTION_TIME = CONNECTION_TIME
        self.CONNECTION_FINISH_TIME = CONNECTION_FINISH_TIME
        self.CALL_DURATION_SEC = CALL_DURATION_SEC
        self.FINISH_REASON = FINISH_REASON
        self.COST = COST

    def getCALLER(self):
        return self.CALLER

    def getCALLED(self):
        return self.CALLED

    def getCALLTIME(self):
        return self.CALL_TIME

    def getCONNECTION(self):
        return str(self.CONNECTION_TIME)[11:13]

    def getTIMEZONE(self):
        if 6 <= int(str(self.CONNECTION_TIME)[11:13]) < 15:
            return 'Day'
        elif 15 <= int(str(self.CONNECTION_TIME)[11:13]) < 23:
            return 'Evening'
        else:
            return 'Night'

    def getSEC(self):
        return self.CALL_DURATION_SEC

    def getREASON(self):
        return self.FINISH_REASON

    def getCOST(self):
        if self.COST == "":
            return 0
        else:
            return float(self.COST)


# help func
def makecall(a):
    return call(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7])


# use the help
# data=[makecall(i) for i in myList]

# Network error rate % function
def networkERR(alist):
    errorcounter, total = 0, 0
    for i in alist:
        total += 1
        if i.getREASON() == 'NETWORK_ERROR':
            errorcounter += 1
    print("\nThe amount of NETWORK_ERROR calls :{}.".format(errorcounter))
    print("Total calls                       :{}.".format(total))
    print("NETWORK_ERROR rate                :{:.1%}\n".format(errorcounter / total))


# Network error analysis by timezone
def networkERRbyzone(alist):
    print("\nThis is NETWORKERROR analysis by TIMEZONE")
    DayERR, EveningERR, NightERR, total = 0, 0, 0, 0
    for i in alist:
        total += 1
        if i.getREASON() == 'NETWORK_ERROR':
            if i.getTIMEZONE() == "Day":
                DayERR += 1
            elif i.getTIMEZONE() == "Evening":
                EveningERR += 1
            else:
                NightERR += 1

    L1 = "\nNETWORK_ERROR Table :\n"
    L2 = "Time zone  Counts  Rate"
    L3 = "{2:^9}  {0:^6}  {1:^4.1%}".format(DayERR, DayERR / total, "Day")
    L4 = "{2:^9}  {0:^6}  {1:^4.1%}".format(EveningERR, EveningERR / total, "Evening")
    L5 = "{2:^9}  {0:^6}  {1:^4.1%}".format(NightERR, NightERR / total, "Night")
    table = [L1, L2, L3, L4, L5]
    ans = input("Print out on screen or output a file (s/f): ")
    if ans == "f":
        name = input("Input a file name:")
        fname = "{}.txt".format(name)
        ofile = open(fname, "w")
        for i in table:
            ofile.write(i + "\n")
        ofile.close()
    else:
        for i in table:
            print(i)

# Call reason analysis by timezone
def call_by_time(data):
    daycall, eveningcall, nightcall = 0, 0, 0
    for i in data:
        if i.getTIMEZONE() == 'Day':
            daycall += 1
        elif i.getTIMEZONE() == 'Evening':
            eveningcall += 1
        else:
            nightcall += 1
    print('\nThere are {} day time calls'.format(daycall))
    print('There are {} evening time calls'.format(eveningcall))
    print('There are {} night time calls'.format(nightcall))
    print('********************')

    # Pie chart ploted by timezone
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Day', 'Evening', 'Night'
    sizes = [daycall, eveningcall, nightcall]
    colors = ['yellowgreen', 'gold', 'lightskyblue']
    explode = (0.1, 0.1, 0.1)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.show()

# Call time and cost analysis in different days
def call_by_day(data):
    MONtotalCALLTIME = 0
    TUEtotalCALLTIME = 0
    WEDtotalCALLTIME = 0
    THUtotalCALLTIME = 0
    FRItotalCALLTIME = 0
    SATtotalCALLTIME = 0
    SUNtotalCALLTIME = 0

    MONtotalCOST = 0
    TUEtotalCOST = 0
    WEDtotalCOST = 0
    THUtotalCOST = 0
    FRItotalCOST = 0
    SATtotalCOST = 0
    SUNtotalCOST = 0

    for i in data:

        if i.getCALLTIME()[0:2] == '02':
            MONtotalCALLTIME += float(i.getSEC())
            MONtotalCOST += float(i.getCOST())
        elif i.getCALLTIME()[0:2] == '03':
            TUEtotalCALLTIME += float(i.getSEC())
            TUEtotalCOST += float(i.getCOST())
        elif i.getCALLTIME()[0:2] == '04':
            WEDtotalCALLTIME += float(i.getSEC())
            WEDtotalCOST += float(i.getCOST())
        elif i.getCALLTIME()[0:2] == '05':
            THUtotalCALLTIME += float(i.getSEC())
            THUtotalCOST += float(i.getCOST())
        elif i.getCALLTIME()[0:2] == '06':
            FRItotalCALLTIME += float(i.getSEC())
            FRItotalCOST += float(i.getCOST())
        elif i.getCALLTIME()[0:2] == '07':
            SATtotalCALLTIME += float(i.getSEC())
            SATtotalCOST += float(i.getCOST())
        elif i.getCALLTIME()[0:2] == '01' or '08':
            SUNtotalCALLTIME += float(i.getSEC())
            SUNtotalCOST += float(i.getCOST())

    print('MON total time :{0}; total cost :{1:9.2f}; cost per sec :{2}'.format(MONtotalCALLTIME, MONtotalCOST,
                                                               MONtotalCOST / MONtotalCALLTIME))
    print('TUE total time :{0}; total cost :{1:9.2f}; cost per sec :{2}'.format(TUEtotalCALLTIME, TUEtotalCOST,
                                                               TUEtotalCOST / TUEtotalCALLTIME))
    print('WED total time :{0}; total cost :{1:9.2f}; cost per sec :{2}'.format(WEDtotalCALLTIME, WEDtotalCOST,
                                                               WEDtotalCOST / WEDtotalCALLTIME))
    print('THU total time :{0}; total cost :{1:9.2f}; cost per sec :{2}'.format(THUtotalCALLTIME, THUtotalCOST,
                                                               THUtotalCOST / THUtotalCALLTIME))
    print('FRI total time :{0}; total cost :{1:9.2f}; cost per sec :{2}'.format(FRItotalCALLTIME, FRItotalCOST,
                                                               FRItotalCOST / FRItotalCALLTIME))
    print('SAT total time :{0}; total cost :{1:9.2f}; cost per sec :{2}'.format(SATtotalCALLTIME, SATtotalCOST,
                                                               SATtotalCOST / SATtotalCALLTIME))
    print('SUN total time :{0}; total cost :{1:9.2f}; cost per sec :{2}'.format(SUNtotalCALLTIME, SUNtotalCOST,
                                                               SUNtotalCOST / SUNtotalCALLTIME))
    # Pie chart ploted by days
    labels = 'Mon', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'
    sizes = [MONtotalCALLTIME, TUEtotalCALLTIME, WEDtotalCALLTIME, THUtotalCALLTIME, FRItotalCALLTIME, SATtotalCALLTIME,
             SUNtotalCALLTIME]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red', 'blue', 'green']
    explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.show()