# Day 5 – Data Cleaning

## Overview

This project is part of my Codomax Data Science Internship.

For Day 5, I worked on cleaning and inspecting the dataset using Python and Pandas. The task focused on checking missing values, identifying duplicate records, and reviewing and correcting data types.

## Objectives

- Import the Pandas library.
- Load the dataset using Pandas.
- Inspect the first few records.
- Check for missing values.
- Check for duplicate records.
- Examine the data types of each column.
- Convert the Date column to the correct datetime format.
- Inspect the final dataset information.

## Tools Used

- Python
- Pandas
- Jupyter Notebook

## Dataset

The dataset used for this task is the cleaned e-commerce dataset from my previous Decode Labs project.

The dataset was loaded from a CSV file:

`Cleaned_Dataset_Day10.csv`

## Data Cleaning Steps

### 1. Import Pandas
import pandas as pd

### 2. Load the Dataset
df = pd.read_csv("Cleaned_Dataset_Day10.csv")

### 3. Preview the Dataset
df.head()

### 4. Check Missing Values
df.isnull().sum()

### 5. Check Duplicate Records
df.duplicated().sum()

### 6. Check Data Types
df.dtypes

### 7. Convert the Date Column
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

### 8. Inspect Dataset Information
df.info()

## Results

The dataset was successfully loaded and inspected. Missing values and duplicate records were checked, the data types were reviewed, and the Date column was converted to the appropriate datetime format.

## Conclusion

Day 5 provided practical experience with data cleaning and validation using Pandas. The dataset is now better prepared for the data filtering and analysis tasks that follow.
