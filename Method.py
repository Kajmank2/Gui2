import GUI as g
import Iteration as it
import csv
from random import *
import re
from functools import reduce
from tkinter import filedialog
from  tkinter import messagebox as ms
import tkinter as tk
#VALUE TO SAVE
q=0
f_alavie=0
minBatt=0
avBatt=0
maxBatt=0

ListData = []  # Reading List Of Data #X #Y
ListPOI = []  # List which contains POI #X #Y
Radius=''
radiusTxt='' #Files which contain name of FIle
STATE=[] # STATES
RULES=[] #RULES
K=[]
BATTERY_STATE=[] # List with lifetime battery
ALIVE_DEAD=[] #ALIVE OF SENSOR
AmountWSN=0
ListofNeighbour=[] #List which contains neighbour
def donothing():
    abc=0

def OpenSensorWSN():
    #LOAD POI
    global AmountWSN
    global Radius # assigment variable global
    with open("POI441.csv") as file:  # CHANGE TO PO 4412
        reader = csv.reader(file)
        for row in reader:
            ListPOI.append(row)

        #text_file = filedialog.askopenfilename(initialdir="C:/", title="Open TextFile",
        #                                       filetypes=(("Text Files", "*.txt"),))
        #text_file = open(text_file, 'r')
        text_file=open('WSN-12d-r35.txt','r')
        radiusTxt=text_file.name
        radius=''
        #RADIUS VALUE FROM FILE
        for word in radiusTxt:
            if word.isdigit():
                radius+=str(word)
        Radius=radius[-2:]
        # DELETE FIRST PARAMETER
        #ADD XY TO LIST
        itera=-1
        for x in text_file:
            ListData.append(x)
            itera+=1
        AmountWSN=itera
        ListData.pop(0)
        print(AmountWSN)
        #Print DATA

def Start():
    print(ListPOI)
    global  STATE
    global  RULES
    #Iteration
    t=0
    #NEIGHBOR FILE TXT
    ListSensorneigh=[]
    ListSensorneighQ =[]
    ListSensorneighQresult =[]
    #NEigh every singe Sensor
    Neighb=[]
    def OpenMYSensorNeighbour():  # find WSN grapph

        # LIST NEIGTBOUR
        ListSensorneigh.append("#parameters of run: ")
        ListSensorneigh.append("#Number of Sensors " + str(AmountWSN))
        ListSensorneigh.append("#Sensor Range: " + Radius)
        ListSensorneigh.append("#POI: 36")
        ListSensorneigh.append("#Sensor for file: " + radiusTxt)
        ListSensorneigh.append("#id num_of_neighb neigb-ID")
        id = 1

        def circle(x1, y1, x2, y2, r1, r2):
            distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
            radSumSq = (r1 + r2) * (r1 + r2)
            if (distSq == radSumSq):
                return 1
            elif (distSq > radSumSq):
                return -1
            else:
                return 0

        ys = ""
        counter = 1
        for x in ListData:
            id = 1
            helper=0
            for y in ListData:
                ListofNeighbour.append(str(id) + str(
                    circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                           int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                           int(Radius), int(Radius))))
                xs = str(id) + str(
                    circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                           int(re.search(r'\d+', y[0:2]).group()), int(re.search(r'\d+', y[5:7]).group()),
                           int(Radius), int(Radius)))
                beng = '-'
                if (beng in xs or str(counter) == xs[0:1] or str(counter) == xs[0:2] ):
                    donothing()
                else:
                    if (len(xs) < 3):
                        ys += xs[0] + " "
                        helper = helper + 1
                    else:
                        ys += xs[0:2] + " "
                        helper = helper + 1
                id = id + 1
            ListSensorneigh.append(str(counter) + "    " + str(helper) + "     " + ys)
            Neighb.append(ys)
            ys = ""
            counter = counter + 1
        print(Neighb)

        def SaveFileSenss():
            with open("sensor-neighbours .txt", 'w') as file:
                for row in ListSensorneigh:
                    s = "".join(map(str, row))
                    file.write(s + '\n')

        SaveFileSenss()
    #Call Neighbour
    OpenMYSensorNeighbour()
    #STATE LIST | RANDOM STATE FORM 0,1
    for x in range(int(AmountWSN)):
        STATE.append(randint(0,1))
    print("FIRST STATE ")
    print(STATE)
    #RULES LIST => Values [1-3]
    for x in range(int(AmountWSN)):
        helper=random()
        if(float(g.labelkDvalue.get())>helper):
            print("KD")
            RULES.append(1)
        elif(float(g.labelkDvalue.get())+(float(g.labelkCvalue.get()))>helper):
            print("KC")
            RULES.append(2)
        else:
            print('KDC')
            RULES.append(3)
    #print(RULES)
    # K -APPROACH [1..N]
    for x in range(int(AmountWSN)):
        if(RULES[x]==1):
            K.append(g.valuesRadiokDstate.get())
        elif (RULES[x] == 2):
            K.append(g.valuesRadiokCstate.get())
        else:
            K.append(g.valuesRadiokDCstate.get())
    #print(K)
    # Battery State [1..N]
    for x in range(int(AmountWSN)):
        BATTERY_STATE.append(int(g.labelBattery.get()))
    #print(BATTERY_STATE)
    #Read neighb of onn LIST
    #BEFORE START ASSIGN SOME VARIABLE
    #LIST SENSOR NEIGH result-2.txt
    ListSensorneighQ.append("#")
    ListSensorneighQ.append("# parameters of experiment")
    ListSensorneighQ.append("#")
    ListSensorneighQ.append("iter s1  s2 ........ sn")
    #List Sensor neigh result 1.txt
    ListSensorneighQresult.append("#")
    ListSensorneighQresult.append("# parameters of experminet")
    ListSensorneighQresult.append('#')
    ListSensorneighQresult.append("# iter  q  freq kD freq kC freq kDC freq_s_ON freq_s_DEAD")

    def MainIter():
        converted_ListData = []
        NewState = []
        StateListNeigh = []
        SensorHelper = []  # HELPER LIST
        POIVALUE = 441
        IdPOICOV=[]
        SensorHelperPoiID=[]
        ALLPOICOV=[]
        global STATE
        for i in range(int(g.labelIterationNumb.get())):
            iter = 0
            def ReadState():
                for x in Neighb:
                    c = 0
                    d = 0
                    i = 1
                    for y in STATE:
                        if (x.find(str(i) + ' ') == -1):
                            i += 1
                            continue
                        else:
                            if (y == 1):
                                c += 1
                            else:
                                d += 1
                            i += 1
                    StateListNeigh.append(str(c) + " " + str(d))
            ReadState()
            print("STATE LIST NEIGH")
            print(StateListNeigh)
            NewState.clear()
        #=====================================================================
            def CalcALLq(): # WRITE COVERAGE METHOD
                def circle(x1, y1, x2, y2, r1, r2):
                    distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
                    radSumSq = (r1 + r2) * (r1 + r2)
                    if (distSq == radSumSq):
                        return 1
                    elif (distSq > radSumSq):
                        return -1
                    else:
                        return 0
                #STATE #SENSORSTATES
                #ListData#->XY
                #ListPOI#->POI
                variableAm=0

                for x in ListData:
                    converted_ListData.append(x.strip())
                    variableAm += 1
                print("COnverted List Data")
                print(converted_ListData)
                #ADD STATE TO THE LIST
                #LIST TO TXT FILE
                ListSensorneighQ.append(str(i) + "  " + str(STATE))
                #ListSensorneighQ.append("#q    s    1 2 3 4 5   q1   q2   q3   q4   q5")
                #FLATEN LIST
                flaten_list=reduce(lambda z, y :z + y,ListPOI)
                ids=6
                #COUNT COVERAE EVERY SENSOR
                for x in converted_ListData:
                    helper = 0
                    for y in flaten_list:
                        if (y[0] == '0' or y[0:2] == '5;' or y[0:2] == '8;'):  # SOLUCJA ZAPISAC CSV JAKO CIĄG STRINGÓW NIE OSOBNĄ LISTE
                            SensorHelper.append(str(
                                circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                                       int(y[0]), int(y[2:]), int(Radius), int(Radius))))
                            ys = str(
                                circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                                       int(y[0]), int(y[2:]), int(Radius), int(Radius)))
                            if (ys[0] == '0'):
                                donothing()
                            else:
                                helper += 1  # VALUE WHEN SENSOR STATE IS 1
                        elif (y[0:3] == '100'):
                            SensorHelper.append(
                                str(circle(int(re.search(r'\d+', x[0:2]).group()),
                                           int(re.search(r'\d+', x[5:7]).group()), int(y[0:3]), int(y[4:]),
                                           int(Radius), int(Radius))))
                            ys = str(
                                circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                                       int(y[0:3]), int(y[4:]), int(Radius), int(Radius)))
                            if (ys[0] == '0'):
                                donothing()
                            else:
                                helper += 1
                        else:
                            SensorHelper.append(
                                str(circle(int(re.search(r'\d+', x[0:2]).group()),
                                           int(re.search(r'\d+', x[5:7]).group()), int(y[0:2]), int(y[3:]),
                                           int(Radius), int(Radius))))
                            ys = str(
                                circle(int(re.search(r'\d+', x[0:2]).group()), int(re.search(r'\d+', x[5:7]).group()),
                                       int(y[0:2]), int(y[3:]),int(Radius), int(Radius)))
                            if (ys[0] == '0'):
                                donothing()
                            else:
                                helper += 1

                    coverage = POIVALUE - helper  # ZMINA Z 411
                    IdPOICOV.append(str(coverage))  # ID + AMOUNT OF
                    pom = 0
                    for x in SensorHelper:
                        ALLPOICOV.append(x)
                        SensorHelperPoiID.append(x + " - " + str(pom))
                        pom = pom + 1
                    # ALLPOICOV.extend(SensorHelper)
                    ids += 1
                    SensorHelper.clear()
                chunkser = [ALLPOICOV[x:x + POIVALUE] for x in range(0, len(ALLPOICOV), POIVALUE)]  #
                chunkserPoi = [SensorHelperPoiID[x:x + POIVALUE] for x in range(0, len(SensorHelperPoiID), POIVALUE)]
                idstates = 0
                arubaCloud = []
                counterchuk = 0
                abc = ""
                for x in STATE:
                    if (x == 0):
                        donothing()
                    else:
                        trucrypt = chunkser[counterchuk]
                        for y in chunkser:
                            printerek = 0
                            amount = 0
                            for z in y:
                                if (trucrypt[printerek] == z):
                                    if (z == '0'):  # and trucrypt != y
                                        amount = amount + 1
                                        arubaCloud.append(str(printerek))  # USUNIECIE PRINTERKA
                                else:
                                    donothing()
                                printerek = printerek + 1
                            abc += str(idstates) + "-" + str(amount) + "\n"  # AMOUNT + STATES ON
                    counterchuk = counterchuk + 1
                    idstates = idstates + 1
                finalStates = dict.fromkeys(arubaCloud)  # DELETE DUPLICATE
                # COVERAGE Q
                coverageQ = len(finalStates) / POIVALUE
                # CALC SENSOR ID TO TXT
                #helper Values
                sensOn=STATE.count(1)
                sensOff=STATE.count(0)
                amountSens=len(STATE)
                kd=str(g.labelkDvalue.get())
                kc = str(g.labelkCvalue.get())
                kdc=str(g.labelkDCvalue.get())
                ListSensorneighQresult.append("    " + str(int(i))+ "  "+
                    str(round(coverageQ, 2)) + "  " + kd+ "  "+kc + "  "+ kdc+ "  "+
                                               str(round(sensOn/amountSens,2)) + "  " +str(round(sensOff/amountSens,2)))

                def SaveFileSenss():
                    with open("result2.txt"
                              "", 'w') as file:
                        for row in ListSensorneighQ:
                            s = "".join(map(str, row))
                            file.write(s + '\n')
                def SaveFileSensss():
                    with open("result1.txt"
                              "", 'w') as file:
                        for row in ListSensorneighQresult:
                            s = "".join(map(str, row))
                            file.write(s + '\n')

                SaveFileSenss()
                SaveFileSensss()
        #FIrst ITeration
            iterr = 0
            for x in RULES:
                if(x==1):# StateListNeigh[iter][2]<K[iter]
                    if(int(StateListNeigh[iter][2])<= int(K[iter]) and BATTERY_STATE[iterr]>0):
                        NewState.append(1)
                        iter+=1
                    else:
                        NewState.append(0)
                        iter += 1
                elif(x==2):
                    if ( int(StateListNeigh[iter][0])<= int(K[iter])and BATTERY_STATE[iterr]>0):
                        NewState.append(1)
                        iter += 1
                    else:
                        NewState.append(0)
                        iter += 1
                else:
                    if (int(StateListNeigh[iter][2])>= int(K[iter])and BATTERY_STATE[iterr]>0):
                        NewState.append(1)
                        iter += 1
                    else:
                        NewState.append(0)
                        iter += 1
                #Battery STATE
                if (1 == int(STATE[iterr])):
                    BATTERY_STATE[iterr] -= 1
                iterr+=1

            #=====================================================================================
            #QOVERAGE
            print("STATE")
            print(STATE)
            #======================================================================ALL COV Q ##################################
            CalcALLq()
            #BATTERY ALIVE
            #print("BATTERY STATE")
            #print(BATTERY_STATE)
            #ZAMIANA STATE PROBLEM
            if (NewState == STATE):
                break
            STATE=NewState
            #CalcALLq()
            #CLEAR
            StateListNeigh.clear()
    MainIter()
    #print("LISTA POI")
    #print(ListPOI)
    #print("LISTA DATA")
    #print(ListData)










