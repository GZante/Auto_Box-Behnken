import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

# Update the regression coefficients (X values)
coeffs = {
    "Intercept": X,
    "A": X,
    "B": X,
    "C": X,
    "D": X,
    "A_B": X,
    "A_C": X,
    "A_D": X,
    "B_C": X,
    "B_D": X,
    "C_D": X,
}

# Generate grid data for plotting
A_vals = np.linspace(0, 1, 50)
B_vals = np.linspace(0, 1, 50)

# Function to predict response using regression model, assuming two-way interaction
def predict_response(A, B, C, D, coeffs):
    return (coeffs["Intercept"] +
            coeffs["A"] * A + coeffs["B"] * B + coeffs["C"] * C + coeffs["D"] * D +
            coeffs["A_B"] * A * B + coeffs["A_C"] * A * C + coeffs["A_D"] * A * D +
            coeffs["B_C"] * B * C + coeffs["B_D"] * B * D + coeffs["C_D"] * C * D)

# Create meshgrid for A and B
A_grid, B_grid = np.meshgrid(A_vals, B_vals)

#C and D fixed, update values X and Y
C_fixed = np.full_like(A_grid, X)
D_fixed = np.full_like(B_grid, Y)

# Compute response percentages and cap at 100%
Response_grid = np.clip(predict_response(A_grid, B_grid, C_fixed, D_fixed, coeffs), 0, 100)

# Define discrete intervals for coloring
intervals = [0, 20, 40, 60, 80, 100]
colors = ["blue", "green", "yellow", "orange", "red"]
cmap = ListedColormap(colors)
norm = BoundaryNorm(intervals, cmap.N)

# Create the plot
plt.figure(figsize=(8, 6))

# Plot filled contour
contourf = plt.contourf(A_grid, B_grid, Response_grid, levels=intervals, cmap=cmap, norm=norm, extend='both')

# Add contour lines for better visibility
contour_lines = plt.contour(A_grid, B_grid, Response_grid, levels=intervals, colors='black', linewidths=0.8)
plt.clabel(contour_lines, fmt="%.0f%%", fontsize=8)

# Add colorbar
cbar = plt.colorbar(contourf, label='Response (%)')
cbar.set_ticks(intervals)

# Labels and title
plt.xlabel('A')
plt.ylabel('B')
plt.title('A vs B (C=X, D=Y)')

plt.show()
