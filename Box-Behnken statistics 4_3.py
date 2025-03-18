import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Load data from Excel file
file_path = 'path_to_your_excel_file.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(file_path)

# Ensure the DataFrame has the correct columns, with four parameters at 3 levels (4^3 design) and a response
required_columns = ['A', 'B', 'C', 'D', 'Response']
if not all(column in df.columns for column in required_columns):
    raise ValueError(f"Excel file must contain the following columns: {required_columns}")

# Add squared terms
df['A_sq'] = df['A'] ** 2
df['B_sq'] = df['B'] ** 2
df['C_sq'] = df['C'] ** 2
df['D_sq'] = df['D'] ** 2  

# Add interaction terms
df['A_B'] = df['A'] * df['B']
df['A_C'] = df['A'] * df['C']
df['B_C'] = df['B'] * df['C']
df['A_D'] = df['A'] * df['D']  
df['B_D'] = df['B'] * df['D']  
df['C_D'] = df['C'] * df['D']  

# Define models
formula_linear = 'Response ~ A + B + C + D'
formula_square = 'Response ~ A + B + C + D + A_sq + B_sq + C_sq + D_sq'
formula_interaction = 'Response ~ A + B + C + D + A_B + A_C + B_C + A_D + B_D + C_D'

# Fit models
model_linear = ols(formula_linear, data=df).fit()
model_square = ols(formula_square, data=df).fit()
model_interaction = ols(formula_interaction, data=df).fit()

# ANOVA tables
anova_linear = sm.stats.anova_lm(model_linear, typ=2)
anova_square = sm.stats.anova_lm(model_square, typ=2)
anova_interaction = sm.stats.anova_lm(model_interaction, typ=2)

# Print results
print("Linear Model Summary:")
print(model_linear.summary())
print("\nANOVA for Linear Model:")
print(anova_linear)
print(f"R-squared: {model_linear.rsquared:.3f}\n")
print(f"Equation: Response = {model_linear.params[0]:.3f} + {model_linear.params[1]:.3f}*A + {model_linear.params[2]:.3f}*B + {model_linear.params[3]:.3f}*C + {model_linear.params[4]:.3f}*D\n")

print("Square Model Summary:")
print(model_square.summary())
print("\nANOVA for Square Model:")
print(anova_square)
print(f"R-squared: {model_square.rsquared:.3f}\n")
print(f"Equation: Response = {model_square.params[0]:.3f} + {model_square.params[1]:.3f}*A + {model_square.params[2]:.3f}*B + {model_square.params[3]:.3f}*C + {model_square.params[4]:.3f}*A^2 + {model_square.params[5]:.3f}*B^2 + {model_square.params[6]:.3f}*C^2 + {model_square.params[7]:.3f}*D^2\n")

print("Two-Way Interaction Model Summary:")
print(model_interaction.summary())
print("\nANOVA for Two-Way Interaction Model:")
print(anova_interaction)
print(f"R-squared: {model_interaction.rsquared:.3f}\n")
print(f"Equation: Response = {model_interaction.params[0]:.3f} + {model_interaction.params[1]:.3f}*A + {model_interaction.params[2]:.3f}*B + {model_interaction.params[3]:.3f}*C + {model_interaction.params[4]:.3f}*D + {model_interaction.params[5]:.3f}*A*B + {model_interaction.params[6]:.3f}*A*C + {model_interaction.params[7]:.3f}*B*C + {model_interaction.params[8]:.3f}*A*D + {model_interaction.params[9]:.3f}*B*D + {model_interaction.params[10]:.3f}*C*D\n")
