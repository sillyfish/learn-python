import plotly.express as px
from die import Die

# Create a D6.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = [die_1.roll() * die_2.roll() for roll_num in range(50_000)]

# Analyze the results.
max_result = die_1.num_sides * die_2.num_sides
poss_results = range(1, max_result + 1)
frequencies = [results.count(value) for value in poss_results]

# Visualize the results.
title = "Results of Rolling Two D6 50,000 Times."
label = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, labels=label, title=title)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()
