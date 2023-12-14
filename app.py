import plotly.express as px

# Create a histogram
fig = px.histogram(vehicles_us.model_year, x="model_year",
                  title="Model year")
fig.show()