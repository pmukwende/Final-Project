import csv
import matplotlib.pyplot as plt
import pandas as pd

def processdatafiles():
    filename = 'bostoncrime2021_7000_sample.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        incidentlist=list(reader)
    f.close()

    filename = 'BostonPoliceDistricts.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        districtList = list(reader)
    f.close()
    return incidentlist, districtList

def barchart (incidentlist, districtlist):
    x=[]
    y=[]

    district = {}
    districtcode = []

    count = 0
    for row in districtlist:
        count+=1
        if count != 1:
            district[row[0]]=row[1]
            districtcode.append(row[0])


    for dist in districtcode:
        count =0
        for row in incidentlist:
            if row[4] == dist:
                count+=1
        x.append(district[dist])
        y.append(count)

    plt.bar(x, y, color = 'r', width = 0.72, label = 'Crimes')
    plt.xlabel('Districts', labelpad=30)
    plt.ylabel('Incidents')
    plt.title('Number of Incidents by District')
    plt.legend()
    plt.show()

def main():

    MENU = """ 
    2 - See sample Data
    Q - Quit
    """


    done = False
    while not done:
        valid = False
        while not valid:
            print(MENU)
            choice = input("Enter your choice: ")
            if choice not in "2Q":
                print("Try again")
            else:
                valid = True
        if choice == "2":
            barchart (incidentlist, districtlist)
        else:
            #print(choice)
            done = True


main()






