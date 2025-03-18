# Auto_Box-Behnken

## Overview

The Auto_Box-Behnken repository provides tools to automate the analysis and visualization of Box-Behnken design of experiments. The aim is to extract statistics and plot results easily within the framework of a Box-Behnken design. The repository includes scripts for both 4^3 and 3^3 designs, allowing users to perform regression analysis, ANOVA, and generate plots to visualize the response as a function of the input parameters.

## Features

Automated Statistics Extraction: Extract regression statistics including ANOVA for linear, square, and two-way interaction models.
Regression Equation: Provide the regression equation for the models.
Visualization: Generate plots to visualize the response as a function of input parameters.
Flexible Input: Reads data from an Excel file with specified columns.


## 1. Box-Behnken statistics 4_3.py

This script is designed for a 4^3 Box-Behnken design. It performs the following tasks:

- Reads data from an Excel file with columns A, B, C, D, and Response.
- Extracts regression statistics including ANOVA for linear, square, and two-way interaction models.
- Provides the regression equation for each model.
 
## 2. Box-Behnken statistics 3_3.py

This script is designed for a 3^3 Box-Behnken design. It performs the same tasks as Box-Behnken statistics 4_3.py but for a 3^3 design:

- Reads data from an Excel file with columns A, B, C, and Response.
- Extracts regression statistics including ANOVA for linear, square, and two-way interaction models.
- Provides the regression equation for each model.
 
## 3. Example plot 4_3.py

This script provides an example of how to generate a plot for a 4^3 Box-Behnken design. It visualizes the response as a function of parameters A and B, with C and D fixed. 

The plot includes:

- A filled contour plot to show the response percentage.
- Contour lines for better visibility.
- A colorbar to indicate the response percentage.



## Prerequisites

Python 3.12.6
Required Libraries: pandas, numpy, statsmodels, matplotlib
