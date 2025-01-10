# Career-Trends-Explorer-and-Personalized-Job-Matcher

This project analyzes and predicts trends related to remote work and job openings, with a focus on the future workforce. Using historical job data and various forecasting models like ARIMA and Prophet, we provide insights into the growth of remote jobs and other workforce patterns.

## Overview

With the growing shift towards remote work, this project aims to:

1. Forecast future trends in remote jobs.
2. Identify key factors influencing job openings and salary trends.
3. Offer recommendations for companies, job seekers, and policymakers.

## Features

- **Data Analysis**: Cleans and processes job data to extract key metrics such as job type, salary, and remote job status.
- **Forecasting**: Implements ARIMA and Prophet models to predict future job trends based on historical data.
- **Visualization**: Generates visualizations of historical and predicted trends, helping stakeholders to understand how remote work is evolving.

## Installation

To run this project locally, follow these steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/your-repository-name.git
    ```

2. Navigate to the project directory:
    ```bash
    cd your-repository-name
    ```

3. Create and activate a Python virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Data

The dataset used in this project includes job postings with details like:

- Job title
- Salary range
- Country
- Job type (e.g., remote, full-time, part-time)
- Year and month of posting

The data is processed to create aggregated metrics such as:

- Percentage of remote jobs
- Average salary and hourly rates
- Job trends over time

## Models Used

1. **ARIMA (AutoRegressive Integrated Moving Average)**: A time series forecasting model used to predict future job trends based on historical data.
2. **Prophet**: A forecasting model developed by Facebook, which is robust to missing data and outliers and is ideal for time series with daily or seasonal patterns.

## How to Run

1. Ensure all dependencies are installed (`pip install -r requirements.txt`).
2. Run the main script to analyze and forecast trends:
    ```bash
    python main.py
    ```
3. View the output visualizations and forecast results.

## Visualizations

The project generates various plots, including:

- A plot showing the historical and forecasted trends of remote jobs.
- A chart forecasting future job openings based on the selected forecasting model.

## Insights and Recommendations

Based on the model forecasts, key insights and recommendations are provided to help stakeholders adapt to future workforce changes:

- **For Companies**: Invest in remote work infrastructure and training programs.
- **For Job Seekers**: Focus on roles in high-demand categories like technology and healthcare.
- **For Policymakers**: Support upskilling initiatives to prepare the workforce for future demands.
## Output 
![Output](https://github.com/minalmmm/Career-Trends-Explorer-and-Personalized-Job-Matcher/blob/main/images/img1.png)
![Output](https://github.com/minalmmm/Career-Trends-Explorer-and-Personalized-Job-Matcher/blob/main/images/img2.png)
