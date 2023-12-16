import plotly.express as px
import pandas as pd
import streamlit as st
import os

# Read data from the CSV file
current_directory = os.getcwd()
relative_path = 'vehicles_upd.csv'
data = pd.read_csv(relative_path )

st.title('Car advertisement dataset')

# Sidebar for sorting options
sort_column = st.selectbox('Select column to sort by', data.columns)
sort_order = st.radio('Select sorting order', ['Ascending', 'Descending'])

# Convert sorting order to boolean for ascending or descending
ascending = True if sort_order == 'Ascending' else False

# Checkbox for filtering specific models
selected_models = st.multiselect('Select models to filter', data['model'].unique())

# Checkbox for filtering by price range
filter_price = st.checkbox('Filter by Price Range')
if filter_price:
    min_price = st.number_input('Minimum Price', min_value=data['price'].min(), max_value=data['price'].max())
    max_price = st.number_input('Maximum Price', min_value=data['price'].min(), max_value=data['price'].max())
    data = data[(data['price'] >= min_price) & (data['price'] <= max_price)]

# Filter DataFrame based on selected models
if selected_models:
    filtered_df = data[data['model'].isin(selected_models)]
else:
    filtered_df = data.copy()  # If no models selected, show the entire DataFrame


# Sort the filtered DataFrame based on user-selected column and order
sorted_df = filtered_df.sort_values(by=sort_column, ascending=ascending)

# Display the sorted DataFrame
st.write(sorted_df)


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

# Create a scatter plot using Plotly Express with color and hover interactions
scatter_fig = px.scatter(
    data, 
    x='model_year', 
    y='price', 
    color='model', 
    title='Car Prices Over Years',
    hover_name='model',  # Show model name on hover
    hover_data={'model_year': True, 'price': True},  # Show year and price on hover
    labels={'year': 'year', 'price': 'price'},  # Customize axis labels
)

# Customize the appearance of the plot
scatter_fig.update_traces(marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')), selector=dict(mode='markers'))

# Display the scatter plot using st.plotly_chart
st.plotly_chart(scatter_fig)