import Method as m
import tkinter as tk
Pi=3.14
ListPOI=[] #List which contains POI #X #Y
#LABELS VALUE
labelkDvalue = ""
labelkCvalue = ""
labelkDCvalue = ""
labelBattery=""
labelIterationNumb=""
labelMuttiruns=""
labelSetSeed=""
#1-10 KC-KD-KDC
valuesRadiokCstate=""
valuesRadiokDstate=""
valuesRadiokDCstate=""
#BAttery STATE
labelBattery=""
def InitGui():
    #GLOVAL VALUE TO METHODS
    global labelkCvalue
    global labelkDvalue
    global labelkDCvalue
    global valuesRadiokCstate
    global valuesRadiokDstate
    global valuesRadiokDCstate
    global labelBattery
    global labelIterationNumb
    global labelSetSeed
    main_window=tk.Tk()
    labelkDvalue = tk.StringVar()
    labelkCvalue = tk.StringVar()
    labelkDCvalue = tk.StringVar()
    labelBattery = tk.StringVar()
    labelIterationNumb = tk.StringVar()
    labelMuttiruns = tk.StringVar()
    labelSetSeed = tk.StringVar()
    labelkDvalue.set("0.33")
    labelkCvalue.set("0.33")
    labelkDCvalue.set("0.34")
    labelBattery.set("10")
    labelIterationNumb.set("8")
    labelMuttiruns.set("1")
    #labelSetSeed.set(123)
    def choiceD(text):
        valuesRadiokDstate.set(text)
    def choiceC(text):
        valuesRadiokCstate.set(text)
    def choiceDC(text):
        valuesRadiokDCstate.set(text)
    valuesRadiokD = {"0D": "0", "1D": "1", " 2D": "2", "3D": "3", "4D": '4', "5D": '5', "6D": '6', '7D': '7', '8D': '8',
                     '9D': '9', '10D': '10'}
    valuesRadiokDstate = tk.StringVar(main_window, '2')
    valuesRadiokC = {"0C": "0", "1C": "1", " 2C": "2", "3C": "3", "4C": '4', "5C": '5', "6C": '6', '7C': '7', '8C': '8',
                     '9C': '9', '10C': '10'}
    valuesRadiokCstate = tk.StringVar(main_window, '2')
    valuesRadiokDC = {"0DC": "0", "1DC": "1", " 2DC": "2", "3DC": "3", "4DC": '4', "5DC": '5', "6DC": '6', '7DC': '7', '8DC': '8',
                     '9DC': '9', '10DC': '10'}
    valuesRadiokDCstate = tk.StringVar(main_window, '2')
    tk.Label(main_window,text="kD").grid(row=0,column=0)
    iterKd=1
    for (text, value) in valuesRadiokD.items():
        tk.Radiobutton(main_window, text=text, variable=valuesRadiokDstate,
                       value=value, command=choiceD(value)).grid(row=iterKd,column=0,sticky="NSEW")
        iterKd+=1
    iterKd=1
    tk.Label(main_window, text="kC").grid(row=0, column=1)
    for (text, value) in valuesRadiokC.items():
        tk.Radiobutton(main_window, text=text, variable=valuesRadiokCstate,
                       value=value, command=choiceC(value)).grid(row=iterKd,column=1,sticky="NSEW")
        iterKd+=1
    iterKd=1
    tk.Label(main_window, text="kDC").grid(row=0, column=2)
    for (text, value) in valuesRadiokDC.items():
        tk.Radiobutton(main_window, text=text, variable=valuesRadiokDCstate,
                       value=value, command=choiceDC(value)).grid(row=iterKd,column=2,sticky="NSEW")
        iterKd+=1
        #Display value of method
    def dispalyValRules():
        print(valuesRadiokCstate.get())
        print(valuesRadiokDstate.get())
        print(valuesRadiokDCstate.get())

    tk.Label(main_window, text="Probability").grid(row=12)
    tk.Label(text="prob kD").grid(row=13,column=0)
    tk.Entry(main_window, textvariable=labelkDvalue, width=10, borderwidth=5).grid(row=14,column=0)
    tk.Label(text="prob kC").grid(row=13, column=1)
    tk.Entry(main_window, textvariable=labelkCvalue, width=10, borderwidth=5).grid(row=14, column=1)
    tk.Label(text="prob kDC").grid(row=13, column=2)
    tk.Entry(main_window, textvariable=labelkDCvalue, width=10, borderwidth=5).grid(row=14, column=2)
    tk.Label(text="Battery unit").grid(row=15,column=0)
    tk.Entry(main_window, textvariable=labelBattery, width=10, borderwidth=5).grid(row=15, column=1)
    tk.Label(text="iter numb").grid(row=16, column=0)
    tk.Entry(main_window, textvariable=labelIterationNumb, width=10, borderwidth=5).grid(row=16, column=1)
    #tk.Label(text="Multiruns").grid(row=17, column=0)
   # tk.Entry(main_window, textvariable=labelMuttiruns, width=10, borderwidth=5).grid(row=17, column=1)
    tk.Label(text="set seed").grid(row=18, column=0)
    tk.Entry(main_window, textvariable=labelSetSeed, width=10, borderwidth=5).grid(row=18, column=1)
    tk.Button(main_window,text="Start by iter",command=m.Start).grid(row=20,column=1)
    tk.Button(main_window, text="Start ", command=m.Startstandard).grid(row=19, column=1)
    #==========================================================#
    #GUI DATA - > #READ POI #READ DATA X,Y
    tk.Button(main_window, text="READ WSN", command=m.OpenSensorWSN).grid(row=19, column=4)

















    main_window.mainloop()
