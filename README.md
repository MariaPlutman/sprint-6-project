# Car Advertisement Analysis Tool
This project involves analyzing a car advertisement dataset to explore various characteristics of vehicles available for sale. It utilizes Streamlit as the interface for user interaction, Plotly Express for data visualization, and Pandas for data manipulation.

## Project Description
This tool allows users to interact with a dataset of car advertisements, exploring different attributes such as model, model year, condition, cylinders, fuel, transmission, vehicle type, price, odometer, days listed, 4-wheel drive availability, and date posted. Users can filter and visualize data using sidebar select boxes and sliders, and view histograms and scatter plots to understand relationships between different vehicle attributes.

## Libraries and Methods Used
- **Pandas**: Used for data manipulation and analysis.
- **Plotly Express**: Utilized for creating interactive visualizations such as histograms and scatter plots.
- **Streamlit**: Employed as the framework to create the user interface and enable user interaction.

## Launching the Project
To launch this project on your local machine, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
```git clone https://github.com/yourusername/sprint-6-project.git```

2. **Install Dependencies**: Navigate to the project directory and install the necessary dependencies by running:
```pip install -r requirements.txt```

3. Run the Application: Execute the Streamlit application using the following command:
```streamlit run your_script_name.py```

4. Replace app.py with the name of your Python script containing the Streamlit code.

5. Interact with the Dashboard: Once the application is running, access it through your web browser at localhost:8501 (by default for Streamlit).

## Notes
Ensure that the CSV file vehicles_us.csv is present in the correct directory or update the file path in the code accordingly.
You may need to modify the data reading and visualization code to fit your specific dataset structure and requirements.