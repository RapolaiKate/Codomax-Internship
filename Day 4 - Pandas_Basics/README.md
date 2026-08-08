# Codomax Day 4 – Pandas Basics

## Overview

This project is part of my Codomax Data Science Internship.

For Day 4, I worked with the Pandas library in Python to load, inspect, and explore a dataset. I used a cleaned dataset from my previous Decode Labs data analysis project to practice basic data manipulation and exploration.

## Objectives

- Import the Pandas library.
- Load the dataset into a Pandas DataFrame.
- View the first and last records.
- Inspect the structure of the dataset.
- Check the number of rows and columns.
- Examine column names and data types.
- Generate descriptive statistics.
- Identify and remove completely empty columns.

## Tools Used

- Python
- Pandas
- Jupyter Notebook
- Microsoft Excel

## Dataset

The dataset used for this task is a cleaned e-commerce dataset containing information such as:

- Order ID
- Customer ID
- Product
- Quantity
- Unit Price
- Payment Method
- Order Status
- Total Price
- Shipping Address
- Referral Source

## Main Pandas Operations

Some of the Pandas operations used include:

```python
import pandas as pd

df = pd.read_excel("Cleaned_Dataset.xlsx")

df.head()
df.tail()
df.info()
df.shape
df.columns
df.dtypes
df.describe()
