import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D

# Set up dark background style for matplotlib
plt.style.use('dark_background')

# 1. Define base data templates and add controlled random scatter
np.random.seed(42)

# Class 0: Underweight (Medium to high height, low to medium weight)
n_samples_0 = 16
height_0 = np.random.uniform(55, 95, n_samples_0)
weight_0 = np.random.uniform(15, 40, n_samples_0)
data_underweight = np.column_stack((height_0, weight_0))

# Class 1: Normal (Low to high height, medium weight)
n_samples_1 = 18
height_1 = np.random.uniform(30, 90, n_samples_1)
weight_1 = np.random.uniform(45, 60, n_samples_1)
data_normal = np.column_stack((height_1, weight_1))

# Class 2: Overweight (Low to medium height, medium to high weight)
n_samples_2 = 16
height_2 = np.random.uniform(35, 65, n_samples_2)
weight_2 = np.random.uniform(65, 95, n_samples_2)
data_overweight = np.column_stack((height_2, weight_2))

# Store them cleanly in a dictionary using explicitly defined arrays
data_dict = {
    'Underweight': data_underweight,
    'Normal': data_normal,
    'Overweight': data_overweight
}

X_0, y_0 = data_dict['Underweight'], np.zeros(len(data_dict['Underweight']), dtype=int)
X_1, y_1 = data_dict['Normal'], np.ones(len(data_dict['Normal']), dtype=int)
X_2, y_2 = data_dict['Overweight'], np.full(len(data_dict['Overweight']), 2, dtype=int)

X = np.vstack((X_0, X_1, X_2))
y = np.concatenate((y_0, y_1, y_2))

# 3. Set up the plot layout with a solid black/dark gray figure background
fig, ax = plt.subplots(figsize=(11, 7), facecolor='#0f1115')
ax.set_facecolor('#13161c') # Dark gray graph plotting area

# Points color map: Red, Yellow, Green
point_colormap = ListedColormap(['#ef4444', '#eab308', '#22c55e'])

# Scatter plot for the points using Red, Yellow, and Green
scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap=point_colormap,
                     edgecolors='#000000', s=95, linewidth=1.5, zorder=3)

# 4. Draw human-guessed linear decision boundaries using y = ax + b
x_vals = np.linspace(20, 100, 200)

# Boundary 1 (Underweight vs Normal)
a1, b1 = 0.35, 12.0
y_line1 = a1 * x_vals + b1

# Boundary 2 (Normal vs Overweight)
a2, b2 = 0.25, 52.0
y_line2 = a2 * x_vals + b2

# Plot manual lines
ax.plot(x_vals, y_line1, color='#38bdf8', linestyle='dashed', linewidth=2.2, zorder=4)
ax.plot(x_vals, y_line2, color='#38bdf8', linestyle='dashdot', linewidth=2.2, zorder=4)

# Display the equations directly on the plot near their lines
ax.text(70, a1 * 70 + b1 + 3, f'$y = {a1}x + {b1}$', color='#38bdf8', fontsize=11, fontweight='bold', bbox=dict(facecolor='#181c24', alpha=0.8, edgecolor='#334155', boxstyle='round,pad=0.3'))
ax.text(50, a2 * 50 + b2 + 3, f'$y = {a2}x + {b2}$', color='#38bdf8', fontsize=11, fontweight='bold', bbox=dict(facecolor='#181c24', alpha=0.8, edgecolor='#334155', boxstyle='round,pad=0.3'))

# Axis limits
ax.set_xlim(25, 100)
ax.set_ylim(5, 100)

# Axis labels and styling
ax.set_xlabel('Martian Height (cm)', fontsize=13, fontweight='bold', color='#38bdf8')
ax.set_ylabel('Martian Weight (kg)', fontsize=13, fontweight='bold', color='#38bdf8')
ax.set_title('Manual Linear Decision Boundaries with Equations ($y = ax + b$)', fontsize=15, color='#f8fafc', pad=15)

# Grid styling
ax.grid(True, linestyle='-', alpha=0.2, color='#64748b')
ax.tick_params(colors='#94a3b8')
for spine in ax.spines.values():
    spine.set_color('#334155')

# Custom Legend
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Underweight', markerfacecolor='#ef4444', markersize=9, markeredgecolor='#000000'),
    Line2D([0], [0], marker='o', color='w', label='Normal', markerfacecolor='#eab308', markersize=9, markeredgecolor='#000000'),
    Line2D([0], [0], marker='o', color='w', label='Overweight', markerfacecolor='#22c55e', markersize=9, markeredgecolor='#000000'),
    Line2D([0], [0], color='#38bdf8', linestyle='dashed', lw=2, label='Boundary 1: y = 0.35x + 12.0'),
    Line2D([0], [0], color='#38bdf8', linestyle='dashed', lw=2, label='Boundary 2: y = 0.25x + 52.0')
]
ax.legend(handles=legend_elements, loc='upper left', facecolor='#181c24', edgecolor='#334155', framealpha=0.95, fontsize=10, labelcolor='#f8fafc')

plt.tight_layout()
plt.savefig('martian_classification_equations.png', dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.show()