import pandas as pd 
import statistics
import plotly.express as px
import csv
import plotly.graph_objects as go


df = pd.read_csv("savings_data.csv")

fig = px.scatter(df, y="quant_saved", color="wealthy")
fig.show()
with open("savings_data.csv", newline="")as f:
    reader = csv.reader(f)
    savings_data = list(reader)
    savings_data.pop(0)
#Finding total number of people and number of people who were reminded    

total_entries = len(savings_data)
total_people_given_reminder = 0
for data in savings_data:
    if int(data[3]) == 1:
        total_people_given_reminder += 1
fig = go.Figure(go.Bar(x=["Reminded", "Not Reminded"], y=[total_people_given_reminder, (total_entries - total_people_given_reminder)]))
fig.show()