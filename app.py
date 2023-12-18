import plotly.express as px
import pandas as pd
import streamlit as st
import os

# Read data from the CSV file
current_directory = os.getcwd()
relative_path = 'vehicles_upd.csv'
data = pd.read_csv(relative_path)

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

st.header('Car Prices Over Years')
# Define columns to remove outliers from
columns_to_remove_outliers = ['model_year', 'price']

# Calculate IQR for specified columns
Q1 = data[columns_to_remove_outliers].quantile(0.25)
Q3 = data[columns_to_remove_outliers].quantile(0.75)
IQR = Q3 - Q1

# Filter data to remove outliers
data_no_outliers = data[~((data[columns_to_remove_outliers] < (Q1 - 1.5 * IQR)) | (data[columns_to_remove_outliers] > (Q3 + 1.5 * IQR))).any(axis=1)]

# Get unique models for the multiselect dropdown
unique_models = data_no_outliers['model'].unique().tolist()

# Create a multiselect dropdown for model selection
selected_models = st.multiselect("Select models to display", unique_models, default=[])

filtered_data = data_no_outliers[data_no_outliers['model'].isin(selected_models)]

scatter_fig = px.scatter(
    filtered_data, 
    x='model_year', 
    y='price', 
    color='model',
    hover_name='model',  
    hover_data={'model_year': True, 'price': True},  
    labels={'model_year': 'Year', 'price': 'Price'}, 
)

# Customize the appearance of the plot
scatter_fig.update_traces(marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')), selector=dict(mode='markers'))

# Display the scatter plot without outliers using st.plotly_chart
st.plotly_chart(scatter_fig)