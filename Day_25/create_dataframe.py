# create dataframe from scratch
import pandas

data_dict = {
    "students": ["Nikhil", "Angela", "Sharmila"],
    "scores": [89, 98, 89]
}

data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv("new_data.csv")
