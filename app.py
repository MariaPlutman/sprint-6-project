import plotly.express as px
import pandas as pd
import streamlit as st
import yfinance as yf

# Read data from the CSV file
data = pd.read_csv('/Users/user/Documents/GitHub/sprint-6-project/vehicles_us.csv')

st.title('Car advertisement dataset')

st.sidebar.header('User Input Features')
st.dataframe(data)
# Create a sidebar select box with unique model years
columns_to_select = {
    'Vehicles Model': 'model',
    'Model Year' : 'model_year',
    'Condition': 'condition',
    'Cylinders': 'cylinders',
    'Fuel': 'fuel',
    'Transmission': 'transmission',
    'Vehicle Type': 'type',
    'Is 4wd': 'is_4wd',
    'Date Posted' : 'date_posted'
}

# Iterate through the dictionary keys and create select boxes in the sidebar
for label, column in columns_to_select.items():
    options = data[column].unique()
    selected_value = st.sidebar.selectbox(label, list(reversed(sorted(options))))

columns_to_slide = {
    'Price' : 'price',
    'Odometer' : 'odometer',
    'Days Listed' : 'days_listed'
}

# Iterate through the dictionary keys and create sliders in the sidebar
for label, column in columns_to_slide.items():
    # Check if the values in the column are numeric before extracting minimum and maximum
    if pd.api.types.is_numeric_dtype(data[column]):
        min_value = int(data[column].min())
        max_value = int(data[column].max())
        selected_value = st.sidebar.slider(label, min_value=min_value, max_value=max_value)
    else:
        st.sidebar.write(f"The '{column}' column contains non-numeric data.")


st.header('Histogram of Model VS Price')
# Create the histogram with Plotly Express
fig = px.histogram(data, x='model', y='price', color='condition', 
                   title='', 
                   labels={'model': 'Model', 'price': 'Price', 'condition': 'Condition'},
                   hover_data=data.columns)  # Display all columns in hover information

fig.update_xaxes(categoryorder='total descending')  # Sort x-axis by total price
fig.update_layout(xaxis_title='Model', yaxis_title='Price')

# Update layout and display the chart
fig.update_traces(marker=dict(line=dict(width=0.5, color='DarkSlateGrey')))  # Define marker properties
fig.update_layout(barmode='overlay')  # Overlay bars for better visibility

st.plotly_chart(fig)

# Create the scatter plot with Plotly Express
fig = px.scatter(data, x='model_year', y='type', color='model',
                 title='Comparison of Models by Type and Model Year',
                 labels={'model_year': 'Model Year', 'type': 'Type', 'model': 'Model'},
                 hover_data=data.columns)

fig.update_traces(marker=dict(size=12, opacity=0.8, line=dict(width=2, color='DarkSlateGrey')))

fig.update_layout(xaxis_title='Model Year', yaxis_title='Type')

# Display the chart using st.plotly_chart()
st.plotly_chart(fig)