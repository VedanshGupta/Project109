import random
import pandas as pd
import csv
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("StudentsPerformance.csv")
reading_score = df["reading score"].to_list()
writing_score = df["writing score"].to_list()

mean_r = statistics.mean(reading_score)
mean_w = statistics.mean(writing_score)

median_r = statistics.median(reading_score)
median_w = statistics.median(writing_score)

mode_r = statistics.mode(reading_score)
mode_w = statistics.mode(writing_score)

std_deviation_r = statistics.stdev(reading_score)
std_deviation_w = statistics.stdev(writing_score)

#Finding standard deiation start and end value

first_start_r, first_end_r = mean_r-std_deviation_r, mean_r+std_deviation_r
first_start_w, first_end_w = mean_w-std_deviation_w, mean_w+std_deviation_w

second_start_r, second_end_r = mean_r-(2*std_deviation_r), mean_r+(2*std_deviation_r)
second_start_w, second_end_w = mean_w-(2*std_deviation_w), mean_w+(2*std_deviation_w)

third_start_r, third_end_r = mean_r-(3*std_deviation_r), mean_r+(3*std_deviation_r)
third_start_w, third_end_w = mean_w-(3*std_deviation_w), mean_w+(3*std_deviation_w)

#plotting the chart, and line for mean, one and second standard deviation

fig = ff.create_distplot([reading_score], ["Result"], show_hist = False)
fig = ff.create_distplot([writing_score], ["Result"], show_hist = False)

fig.add_trace(go.Scatter(x = [mean_r, mean_r], y = [0, 0.17], mode = "lines", name = "MEAN OF READING SCORE"))
fig.add_trace(go.Scatter(x = [mean_w, mean_w], y = [0, 0.17], mode = "lines", name = "MEAN OF WITNIG SCORE"))

fig.add_trace(go.Scatter(x = [first_start_r, first_start_r], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 OF READING SCORE START"))
fig.add_trace(go.Scatter(x = [first_start_w, first_start_w], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 OF WRITING SCORE START"))
fig.add_trace(go.Scatter(x = [first_end_r, first_end_r], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 OF READING SCORE END"))
fig.add_trace(go.Scatter(x = [first_end_w, first_end_w], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 OF WRITING SCORE END"))

fig.add_trace(go.Scatter(x = [second_start_r, second_start_r], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 OF READING SCORE START"))
fig.add_trace(go.Scatter(x = [second_start_w, second_start_w], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 OF WRITING SCORE START"))
fig.add_trace(go.Scatter(x = [second_end_r, second_end_r], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 OF READING SCORE END"))
fig.add_trace(go.Scatter(x = [second_end_w, second_end_w], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 OF WRITING SCORE END"))

#printing finding
list_first_std_dev_r = [result for result in reading_score if result > first_start_r and result < first_end_r]
list_first_std_dev_w = [result for result in writing_score if result > first_start_w and result < first_end_w]

list_second_std_dev_r = [result for result in reading_score if result > second_start_r and result < second_end_r]
list_second_std_dev_w = [result for result in writing_score if result > second_start_w and result < second_end_w]

list_third_std_dev_r = [result for result in reading_score if result > third_start_r and result < third_end_r]
list_third_std_dev_w = [result for result in writing_score if result > third_start_w and result < third_end_w]

print(mean_r)
print(mean_w)

print(mode_r)
print(mode_w)

print(median_r)
print(median_w)

print(std_deviation_r)
print(std_deviation_w)

print("Standard deviation of this data is {}".format(std_deviation_r))
print("Standard deviation of this data is {}".format(std_deviation_w))

print("{}% of data lies within 1 standard deviation".format(len(list_first_std_dev_r)*100.0/len(reading_score)))
print("{}% of data lies within 1 standard deviation".format(len(list_first_std_dev_w)*100.0/len(writing_score)))

print("{}% of data lies within 2 standard deviation".format(len(list_second_std_dev_r)*100.0/len(reading_score)))
print("{}% of data lies within 2 standard deviation".format(len(list_second_std_dev_w)*100.0/len(writing_score)))

print("{}% of data lies within 3 standard deviation".format(len(list_third_std_dev_r)*100.0/len(reading_score)))
print("{}% of data lies within 3 standard deviation".format(len(list_third_std_dev_w)*100.0/len(writing_score)))

fig.show()