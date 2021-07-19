"""
Name: Daniel Mukwende
CS602: Section N1
Data: Boston Crime
Description:
This program measures the crime rate in Boston. It shows the locations
where there is a high crime rate, the most common crimes, and the period
of the year when the crimes are higher

"""


import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px


#bar plot
def bar():
    x = []
    y = []

    district = {}
    districtcode = []
    with open('BostonPoliceDistricts.csv') as csv1file:
        data = csv.reader(csv1file)
        count = 0
        for row in data:
            count += 1
            if count != 1:
                district[row[0]]=row[1]
                districtcode.append(row[0])

    with open('bostoncrime2021_7000_sample.csv') as csv2file:
        plots = csv.reader(csv2file, delimiter=',')
        df=list(plots)
        #print(df)
        for dist in districtcode:
            count =0
            for row in df:
                if row[4] == dist:
                    count += 1
            x.append(district[dist])
            y.append(count)

        plt.bar(x, y, color='r', width = 0.72, label='Crimes')
        plt.xlabel('Districts', labelpad=30)
        plt.xticks(rotation=45)
        plt.ylabel('Incidents')
        plt.title('Number of Incidents by District')
        plt.legend()
        plt.show()


def months():
    df = pd.read_csv('bostoncrime2021_7000_sample.csv')
    numbers = df['MONTH'].value_counts()
    monthscount = df['MONTH'].value_counts().keys()
    plt.title('Most Common Months')
    plt.ylabel('Month Repetition')
    plt.xlabel('Months')
    plt.xticks(rotation = 0)
    plt.bar(monthscount, numbers)
    plt.show()


def offenses():
    df = pd.read_csv('bostoncrime2021_7000_sample.csv')
    value = df['OFFENSE_DESCRIPTION'].value_counts()
    print(value)


def days():
    df = pd.read_csv('bostoncrime2021_7000_sample.csv')
    numbers = df['DAY_OF_WEEK'].value_counts()
    dayscount = df['DAY_OF_WEEK'].value_counts().keys()
    plt.title('Most Common Days')
    plt.ylabel('Day Repetition')
    plt.xlabel('Days')
    plt.xticks(rotation = 45)
    plt.bar(dayscount, numbers)
    plt.show()


def map_():
    data = pd.read_csv('bostoncrime2021_7000_sample.csv')
    police = pd.read_csv('BostonPoliceDistricts.csv')
    df = data.merge(police, left_on='DISTRICT', right_on='District', how='left')
    fig = px.scatter_mapbox(df, lat="Lat", lon="Long", hover_name="District Name",hover_data=[ "INCIDENT_NUMBER"],
                            color_discrete_sequence=["fuchsia"], zoom=3, height=300)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()


#choose option


def show_plot(option):
    if option == 'bar':
        bar()
    elif option == 'map':
        map_()
    elif option == 'days':
        days()
    elif option == 'months':
        months()
    elif option == 'offenses':
        offenses()
    else:
        print('Choose from bar or map plots')


option = input('Enter the type of plot you want to see:')
show_plot(option)
