import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Data for the flowchart
weeks = [
    "Week 1", "Weeks 2–3", "Weeks 4–5", "Weeks 6–7", "Week 8",
    "Week 9", "Week 10", "Week 11", "Week 12"
]
milestones = [
    "Project Kickoff & Requirements Gathering",
    "UI/UX Design Phase",
    "Core Infrastructure Setup",
    "API Integration & Data Handling",
    "Offline Capability Integration",
    "Core Features Development",
    "QA & Internal Testing",
    "Beta Release & Feedback",
    "Final Release & Submission"
]

# Create a flowchart using matplotlib
fig, ax = plt.subplots(figsize=(12, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, len(weeks) + 1)
ax.axis('off')

# Draw each milestone as a rounded box and connect with arrows
for i, (week, milestone) in enumerate(zip(weeks, milestones)):
    y = len(weeks) - i
    box = mpatches.FancyBboxPatch(
        (2, y - 0.5), 6, 1,
        boxstyle="round,pad=0.1", edgecolor='black', facecolor='#cce5ff'
    )
    ax.add_patch(box)
    ax.text(5, y, f"{week}: {milestone}", ha='center', va='center', fontsize=9, weight='bold')
    
    # Add arrows between boxes
    if i < len(weeks) - 1:
        ax.annotate('', xy=(5, y - 0.5), xytext=(5, y - 1.5),
                    arrowprops=dict(arrowstyle='->', lw=2, color='gray'))

plt.title("iOS App Development Project Plan - Flowchart", fontsize=14, weight='bold')
plt.tight_layout()
plt.show()
