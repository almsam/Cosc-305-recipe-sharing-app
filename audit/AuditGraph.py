import seaborn as sns; import matplotlib.pyplot as plt; import pandas as pd


data = { "Metric": [ 
    "1a. Charter & Timeline Accuracy",
    "1b. Video vs Current Implementation",
    "1c. Milestone Review Accuracy",
    " ", 
    "2a. Change Log Detail",
    "2b. Risk & Change Tracking",
    "2c. Quality Tracking",
    "  ", 
    "3. Responsiveness to Stakeholders"
], "Score": [6, 7, 8, 0, 8, 9, 8, 0, 10] }

Color = ["#ff0000", "#ff8000", "#eecc00", "#000000", "#00bb44", "#2244ff", "#8040ff", "#000000", "#aa5000"]

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6)); sns.barplot(data=df, x="Metric", y="Score", palette=Color)

plt.title("Audit Evaluation Scores", fontsize=16); plt.xlabel("Metric", fontsize=12)
plt.ylabel("Score out of 10", fontsize=12); plt.xticks(rotation=82, ha="right")

plt.ylim(0, 10); plt.tight_layout(); plt.show()
