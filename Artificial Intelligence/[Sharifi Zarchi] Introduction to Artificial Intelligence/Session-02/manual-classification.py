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

# 4. Draw human-guessed linear decision boundaries and evaluate points using ax + by + c logic
# 
# MATHEMATICAL INTUITION FOR LINEAR DECISION BOUNDARIES:
# -------------------------------------------------------------------------
# A linear boundary can be expressed in general form as: ax + by + c = 0 
# (where x is height, y is weight, a and b are coefficients, and c is the intercept offset).
# 
# For any given point (x, y):
#   - If ax + by + c == 0 : The point lies EXACTLY on the decision line.
#   - If ax + by + c > 0  : The point lies on one side (above/right) of the line.
#   - If ax + by + c < 0  : The point lies on the opposite side (below/left) of the line.
#

x_vals = np.linspace(20, 100, 200)

# Boundary 1: y = 0.35x + 12.0  =>  Rearranged to standard form: 0.35x - 1.0y + 12.0 = 0
a1, b1, c1 = 0.35, -1.0, 12.0
y_line1 = 0.35 * x_vals + 12.0

# Boundary 2: y = 0.25x + 52.0  =>  Rearranged to standard form: 0.25x - 1.0y + 52.0 = 0
a2, b2, c2 = 0.25, -1.0, 52.0
y_line2 = 0.25 * x_vals + 52.0

# Plot manual lines
ax.plot(x_vals, y_line1, color='#38bdf8', linestyle='dashed', linewidth=2.2, zorder=4)
ax.plot(x_vals, y_line2, color='#38bdf8', linestyle='dashdot', linewidth=2.2, zorder=4)

# Display the equations directly on the plot near their lines
ax.text(70, 0.35 * 70 + 12.0 + 3, f'$y = 0.35x + 12.0$', color='#38bdf8', fontsize=11, fontweight='bold', bbox=dict(facecolor='#181c24', alpha=0.8, edgecolor='#334155', boxstyle='round,pad=0.3'))
ax.text(50, 0.25 * 50 + 52.0 + 3, f'$y = 0.25x + 52.0$', color='#38bdf8', fontsize=11, fontweight='bold', bbox=dict(facecolor='#181c24', alpha=0.8, edgecolor='#334155', boxstyle='round,pad=0.3'))

# --- VISUALIZING THE CONDITIONS FOR SPECIFIC POINTS ---
# Let's pick a few sample points from our dataset to explicitly evaluate and annotate on the plot:
# Point A (from Normal class): Let's pick an explicit coordinate
sample_x, sample_y = 65.0, 62.0

# Evaluate the expression ax + by + c for Boundary 1
val1 = a1 * sample_x + b1 * sample_y + c1
# Evaluate the expression ax + by + c for Boundary 2
val2 = a2 * sample_x + b2 * sample_y + c2

# Plot the sample point with a special marker to show how it's tested against the equations
ax.scatter([sample_x], [sample_y], color='#ffffff', s=160, marker='*', zorder=5, edgecolors='#000000')

# Add text annotations showing the exact evaluation logic results near the sample point
eval_text = f'Sample Point ({sample_x}, {sample_y})\n' \
            f'B1 (val={val1:.1f}): {"== 0" if val1==0 else ("> 0 (Above)" if val1>0 else "< 0 (Below)")}\n' \
            f'B2 (val={val2:.1f}): {"== 0" if val2==0 else ("> 0 (Above)" if val2>0 else "< 0 (Below)")}'

ax.annotate(eval_text, xy=(sample_x, sample_y), xytext=(sample_x + 3, sample_y - 12),
            arrowprops=dict(facecolor='#38bdf8', shrink=0.05, width=1, headwidth=6),
            fontsize=9, fontweight='bold', color='#f8fafc',
            bbox=dict(facecolor='#181c24', alpha=0.9, edgecolor='#38bdf8', boxstyle='round,pad=0.4'))

# Axis limits
ax.set_xlim(25, 100)
ax.set_ylim(5, 100)

# Axis labels and styling
ax.set_xlabel('Martian Height (cm)', fontsize=13, fontweight='bold', color='#38bdf8')
ax.set_ylabel('Martian Weight (kg)', fontsize=13, fontweight='bold', color='#38bdf8')
ax.set_title(r'Linear Decision Boundaries & Region Evaluation ($ax + by + c \gtrless 0$)', fontsize=15, color='#f8fafc', pad=15)

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
    Line2D([0], [0], marker='*', color='w', label='Sample Point Evaluation', markerfacecolor='#ffffff', markersize=11, markeredgecolor='#000000'),
    Line2D([0], [0], color='#38bdf8', linestyle='dashed', lw=2, label='Boundary 1: y = 0.35x + 12.0'),
    Line2D([0], [0], color='#38bdf8', linestyle='dashdot', lw=2, label='Boundary 2: y = 0.25x + 52.0')
]
ax.legend(handles=legend_elements, loc='upper left', facecolor='#181c24', edgecolor='#334155', framealpha=0.95, fontsize=10, labelcolor='#f8fafc')

plt.tight_layout()
plt.savefig('martian_classification_regions_evaluated.png', dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.show()