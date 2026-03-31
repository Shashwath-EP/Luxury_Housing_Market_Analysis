# Luxury Housing Market Analysis – Bangalore

## Project Overview

This project analyzes luxury housing trends in Bangalore using **Python, SQL, and Power BI**.
The goal is to build a complete **data analytics pipeline** that processes raw housing data, stores it in a database, and visualizes insights using an interactive dashboard.

The analysis focuses on developer performance, buyer segmentation, housing configuration demand, pricing trends, and geographical distribution of projects.

---

## Tools & Technologies

* **Python** – Data cleaning and preprocessing
* **MySQL** – Database storage and querying
* **Power BI** – Data visualization and dashboard creation
* **Git & GitHub** – Version control and project hosting

---

## Project Workflow

The project follows a typical data analytics pipeline:

1. **Data Cleaning (Python)**

   * Load the raw dataset
   * Handle missing values
   * Normalize column formats
   * Prepare the dataset for database insertion

2. **Database Integration (SQL)**

   * Create database schema
   * Load cleaned data into MySQL
   * Run validation and aggregation queries

3. **Data Visualization (Power BI)**

   * Connect Power BI to the SQL database
   * Create interactive dashboards
   * Build KPIs, charts, and filters for analysis

---

## Key Dashboard Features

The Power BI dashboard includes:

* **Total Projects KPI**
* **Average Ticket Price**
* **Average Amenity Score**
* **Projects by Developer**
* **Housing Configuration Demand**
* **Buyer Type Distribution**
* **Projects by Micro Market**
* **Luxury Housing Price Trend**
* **Project Growth by Quarter**
* **Interactive filters (developer, location, configuration, buyer type)**

---

## Key Insights

* Major developers dominate the luxury housing market in Bangalore.
* Demand is highest for **3BHK and 4BHK configurations**.
* Certain micro-markets have higher project concentration.
* Luxury housing prices show trends across purchase quarters.
* Buyer segments include CXO, HNI, NRI, and startup founders.

---

## Project Structure

```
Luxury_Housing_Market_Analysis
│
├── data
│   └── housing_data.csv
│
├── scripts
│   ├── data_cleaning.py
│   └── load_to_sql.py
│
├── sql
│   ├── create_table.sql
│   └── analysis_queries.sql
│
├── notebooks
│   └── luxury_housing_eda.ipynb
│
├── Luxury_Housing_Market_Analysis.pbix
└── README.md
```

---

## How to Run the Project

1. Clone the repository
2. Run Python scripts for data cleaning and database loading
3. Execute SQL scripts to create the database tables
4. Open the `.pbix` file in Power BI to explore the dashboard

---

## Conclusion

This project demonstrates how to build an **end-to-end data analytics workflow** using Python, SQL, and Power BI to generate meaningful insights from a real estate dataset.

The dashboard provides a clear overview of luxury housing market trends and enables interactive exploration of the data.
