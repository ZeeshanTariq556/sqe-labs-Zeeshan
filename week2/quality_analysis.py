import matplotlib.pyplot as plt
import numpy as np

# 1. Define Characteristics and Ratings
labels = [
    'Functional Suitability', 'Performance Efficiency', 'Compatibility', 
    'Usability', 'Reliability', 'Security', 'Maintainability', 'Portability'
]

# Ratings extracted from your Quality Assessment Report
APP1_RATINGS = [5, 4, 5, 4, 4, 5, 4, 5]  # Gmail
APP2_RATINGS = [5, 4, 4, 4, 4, 5, 4, 5]  # Outlook

# Weights defined in your report
weights = np.array([0.15, 0.12, 0.10, 0.15, 0.15, 0.15, 0.08, 0.10])

# 2. Calculate Weighted Totals (to verify)
app1_score = np.sum(np.array(APP1_RATINGS) * weights)
app2_score = np.sum(np.array(APP2_RATINGS) * weights)

print(f"Gmail Weighted Total: {app1_score:.2f}")
print(f"Outlook Weighted Total: {app2_score:.2f}")

# 3. Create Radar Chart
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Close the radar loop
APP1_RATINGS += APP1_RATINGS[:1]
APP2_RATINGS += APP2_RATINGS[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot App 1 (Gmail)
ax.fill(angles, APP1_RATINGS, color='blue', alpha=0.25)
ax.plot(angles, APP1_RATINGS, color='blue', linewidth=2, label=f'Gmail (Score: {app1_score:.2f})')

# Plot App 2 (Outlook)
ax.fill(angles, APP2_RATINGS, color='red', alpha=0.25)
ax.plot(angles, APP2_RATINGS, color='red', linewidth=2, label=f'Outlook (Score: {app2_score:.2f})')

# Labels and Styling
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), labels)
ax.set_ylim(0, 5)

plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.title("ISO/IEC 25010 Quality Profile: Gmail vs Outlook", size=15, y=1.1)

# Save as PNG as required by Step 4
plt.savefig('quality_radar_Gmail_Outlook.png', bbox_inches='tight')
print("Radar chart saved as quality_radar_Gmail_Outlook.png")
