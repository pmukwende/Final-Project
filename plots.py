#bar plot
def bar():
    import csv
    import matplotlib.pyplot as plt
    import plotly.express as px

    x=[]
    y=[]

    district = {}
    districtcode = []
    with open('BostonPoliceDistricts.csv') as csv1file:
        data = csv.reader(csv1file)
        count = 0
        for row in data:
            count+=1
            if count != 1:
                district[row[0]]=row[1]
                districtcode.append(row[0])

    with open('bostoncrime2021_7000_sample.csv') as csv2file:
        plots = csv.reader(csv2file, delimiter = ',')
        df=list(plots)
        #print(df)
        for dist in districtcode:
            count =0
            for row in df:
                if row[4] == dist:
                    count+=1
            x.append(district[dist])
            y.append(count)

        plt.bar(x, y, color = 'r', width = 0.72, label = 'Crimes')
        plt.xlabel('Districts', labelpad=30)
        plt.xticks(rotation = 90)
        plt.ylabel('Incidents')
        plt.title('Number of Incidents by District')
        plt.legend()
        plt.show()



#map plot
def map_():
    import pandas as pd
    import plotly.express as px
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
    #elif option == 'new_chart':
     #   new_chart()
    else:
        print('Choose from bar or map plots')


option = input('Enter the type of plot you want to see:')
show_plot(option)
