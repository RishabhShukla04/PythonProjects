import pandas

census_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240905.csv")
grey_data = len(census_data[census_data["Primary Fur Color"] == "Gray"])
cinnammon_data = len(census_data[census_data["Primary Fur Color"] == "Cinnamon"])
black_data = len(census_data[census_data["Primary Fur Color"] == "Black"])

data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_data, cinnammon_data, black_data]
}
final_data = pandas.DataFrame(data)
final_data.to_csv("Squirrel_Colour_Count.csv")