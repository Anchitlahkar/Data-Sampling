import pandas as pd
import statistics as st
import random
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")

claps = df["claps"].tolist()
reading_time = df["reading_time"].tolist()


population_meanOfClaps = st.mean(claps)
population_meanOfReadingTime = st.mean(reading_time)


ClapsMean = []
ReadingTimeMean = []


for i in range(0, 100):

    spDataOfClaps = []
    spDataOfReadingTime = []

    for i in range(0, 30):
        randomIndexofClaps = random.randint(0, len(claps)-1)
        Claps_Value = claps[randomIndexofClaps]

        randomIndexofReadingTime = random.randint(0, len(reading_time)-1)
        ReadingTime_Value = reading_time[randomIndexofReadingTime]

        spDataOfClaps.append(Claps_Value)
        spDataOfReadingTime.append(ReadingTime_Value)

    Mean_spData_Claps = st.mean(spDataOfClaps)
    Mean_spData_ReadingTime = st.mean(spDataOfReadingTime)

    ClapsMean.append(Mean_spData_Claps)
    ReadingTimeMean.append(Mean_spData_ReadingTime)


SampleClapMean = st.mean(ClapsMean)
SampleReadingTime = st.mean(ReadingTimeMean)


print("Population Claps Mean: ", population_meanOfClaps)
print("Population Reading Time Mean: ", population_meanOfReadingTime)
print("Sample Claps Mean: ", SampleClapMean)
print("Sample Reading Time Mean: ", SampleReadingTime)


print("\n\nWant to see two different graph Y/N")
userInput = input("'Y' for two graph, 'N' for one Graph: \t")

ans = userInput.lower()

if 'n' in ans:
    graph = ff.create_distplot([ClapsMean, ReadingTimeMean], [
        "Clap Mean",  "Reading Time Mean"], show_hist=False)

    graph.show()

elif 'y' in ans:
    graph1 = ff.create_distplot([ClapsMean], ["Clap Mean"], show_hist=False)

    graph2 = ff.create_distplot(
        [ReadingTimeMean], ["Reading Time Mean"], show_hist=False)

    graph1.show()
    graph2.show()

else:
    print('Please Enter Y/N')
    input("Exit")
