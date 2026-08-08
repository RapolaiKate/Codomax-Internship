# Day 7 – Data Analysis

## Overview

This project is part of my Codomax Data Science Internship.

For Day 7, I used Python and Pandas to perform basic analysis on the dataset. I calculated the total, average, minimum, maximum, and count of the `TotalPrice` column.

## Objectives

- Load the dataset using Pandas.
- Calculate the total value.
- Calculate the average value.
- Find the minimum value.
- Find the maximum value.
- Count the number of records.

## Tools Used

- Python
- Pandas
- Jupyter Notebook

## Dataset

The dataset used for this task is the cleaned e-commerce dataset from my previous Decode Labs project.

The dataset was loaded from:

`Cleaned_Dataset_Day10.csv`

## Analysis Performed

The following Pandas functions were used:

```python
df["TotalPrice"].sum()
df["TotalPrice"].mean()
df["TotalPrice"].min()
df["TotalPrice"].max()
df["TotalPrice"].count()

## The five calculations were also combined using:

df["TotalPrice"].agg(["sum", "mean", "min", "max", "count"])

## Results

The analysis provided basic statistical information about the TotalPrice values in the dataset, including the total, average, minimum, maximum, and number of records.

## Conclusion

Day 7 provided practical experience in performing basic data analysis using Pandas. The results will be useful for the visualization tasks in Day 8.
