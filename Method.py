import random
import GUI as g
import csv
import re
from functools import reduce
from tkinter import filedialog
from  tkinter import messagebox as ms
import Method as m
import tkinter as tk
ListData = []  # Reading List Of Data #X #Y
ListPOI = []  # List which contains POI #X #Y
Radius=''
radiusTxt='' #Files which contain name of FIle
STATE=[]
AmountWSN=0
ListofNeighbour=[] #List which contains neighbour
def donothing():
    abc=0

def OpenSensorWSN():
    #LOAD POI
    global Radius # assigment variable global
    with open("POI36.csv") as file:  # CHANGE TO PO 4412
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

    #Iteration
    t=0
    #NEIGHBOR
    ListSensorneigh=[]
    #RandomState
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
            ys = ""
            counter = counter + 1
        print(ListSensorneigh)

        def SaveFileSenss():
            with open("sensor-neighbours .txt", 'w') as file:
                for row in ListSensorneigh:
                    s = "".join(map(str, row))
                    file.write(s + '\n')

        SaveFileSenss()
    #Call Neighbour
    OpenMYSensorNeighbour()


