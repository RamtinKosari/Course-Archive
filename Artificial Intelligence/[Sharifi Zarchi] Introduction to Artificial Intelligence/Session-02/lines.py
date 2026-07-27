import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
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

# Extract and combine into X and y arrays for the SVM
X_0, y_0 = data_dict['Underweight'], np.zeros(len(data_dict['Underweight']), dtype=int)
X_1, y_1 = data_dict['Normal'], np.ones(len(data_dict['Normal']), dtype=int)
X_2, y_2 = data_dict['Overweight'], np.full(len(data_dict['Overweight']), 2, dtype=int)

X = np.vstack((X_0, X_1, X_2))
y = np.concatenate((y_0, y_1, y_2))

# 2. Train the Classifier (Switched to linear kernel for straight decision boundaries)
clf = svm.SVC(kernel='linear', C=2.0)
clf.fit(X, y)

# 3. Set up the plot layout with a solid black/dark gray figure background
fig, ax = plt.subplots(figsize=(11, 7), facecolor='#0f1115')
ax.set_facecolor('#13161c') # Dark gray graph plotting area

# Create a mesh grid for the decision surface
x_min, x_max = X[:, 0].min() - 5, X[:, 0].max() + 5
y_min, y_max = X[:, 1].min() - 5, X[:, 1].max() + 5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.5),
                     np.arange(y_min, y_max, 0.5))

Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Define blue/cyan/dark-gray background color maps
bg_colormap = ListedColormap(['#182232', '#141820', '#11222b'])
# Points color map: Red, Yellow, Green
point_colormap = ListedColormap(['#ef4444', '#eab308', '#22c55e'])

# 4. Render Visualizations
# Filled decision boundaries in the background
ax.contourf(xx, yy, Z, cmap=bg_colormap, alpha=0.7)

# Scatter plot for the points using Red, Yellow, and Green
scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap=point_colormap,
                     edgecolors='#000000', s=95, linewidth=1.5, zorder=3)

# Straight linear decision boundaries (Cyan/Blue themed)
ax.contour(xx, yy, Z, colors='#38bdf8', linestyles='dashed', linewidths=1.8, levels=[0.5, 1.5], alpha=0.9, zorder=2)

# Axis labels and styling
ax.set_xlabel('Martian Height (cm)', fontsize=13, fontweight='bold', color='#38bdf8')
ax.set_ylabel('Martian Weight (kg)', fontsize=13, fontweight='bold', color='#38bdf8')
ax.set_title('Martian Classification: Height vs. Weight (Linear Kernel)', fontsize=15, color='#f8fafc', pad=15)

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
    Line2D([0], [0], color='#38bdf8', linestyle='dashed', lw=2, label='Linear Decision Boundary')
]
ax.legend(handles=legend_elements, loc='upper left', facecolor='#181c24', edgecolor='#334155', framealpha=0.95, fontsize=11, labelcolor='#f8fafc')

plt.tight_layout()

# Save the figure as a high-resolution PNG file
plt.savefig('martian_classification_linear.png', dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')

plt.show()