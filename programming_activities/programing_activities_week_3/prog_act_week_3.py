# Titanic Visualization Coursework
# Install dependencies if needed:
# pip install pandas matplotlib seaborn plotly plotnine statsmodels

# %% Setup: imports and dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotnine import (
    ggplot, aes, geom_point, stat_smooth,
    facet_wrap, theme_minimal, labs
)

# Change this filename if your CSV has a different name.
# If df is already loaded in your notebook, you can skip this line.
df = pd.read_csv("titanic.csv")

# %% Programming Activity 1: Matplotlib
# Group by passenger class and calculate survivors and average fare.
class_summary = df.groupby("Pclass").agg(
    TotalSurvivors=("Survived", "sum"),
    AverageFare=("Fare", "mean")
)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left subplot: total survivors by class.
axes[0].bar(class_summary.index, class_summary["TotalSurvivors"],
            color="steelblue")
axes[0].set_title("Total Survivors by Passenger Class")
axes[0].set_xlabel("Passenger Class")
axes[0].set_ylabel("Number of Survivors")
axes[0].set_xticks(class_summary.index)

# Right subplot: average fare by class.
axes[1].barh(class_summary.index, class_summary["AverageFare"], color="coral")
axes[1].set_title("Average Fare by Passenger Class")
axes[1].set_xlabel("Average Fare")
axes[1].set_ylabel("Passenger Class")
axes[1].set_yticks(class_summary.index)

plt.tight_layout()
plt.show()

# %% Programming Activity 2: Seaborn
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

ax = sns.violinplot(
    data=df,
    x="Pclass",
    y="Age",
    hue="Survived",
    hue_order=[0, 1],
    split=True
)
ax.set_title("Age Distribution by Passenger Class and Survival")
ax.set_xlabel("Passenger Class")
ax.set_ylabel("Age")

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, ["Did Not Survive", "Survived"], title="Survival Status")

plt.tight_layout()
plt.show()

# %% Programming Activity 3: Plotly
# Include the passenger in the total family size.
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# Treat passenger class and survival as discrete categories.
plotly_df = df.copy()
plotly_df["Pclass"] = plotly_df["Pclass"].astype(str)
plotly_df["Survived"] = plotly_df["Survived"].map(
    {0: "Did Not Survive", 1: "Survived"}
)

fig = px.scatter(
    plotly_df,
    x="Age",
    y="Fare",
    color="Pclass",
    symbol="Survived",
    size="FamilySize",
    hover_name="Name",
    hover_data=["Embarked", "Sex"],
    title="Passenger Age and Fare by Class, Survival, and Family Size",
    labels={
        "Age": "Age",
        "Fare": "Fare",
        "Pclass": "Passenger Class",
        "Survived": "Survival Status",
        "FamilySize": "Family Size",
        "Embarked": "Embarkation Port",
        "Sex": "Sex"
    }
)
fig.show()

# %% Programming Activity 4: Plotnine
plot = (
    ggplot(df, aes(x="Age", y="Fare", color="factor(Survived)"))
    + geom_point(alpha=0.6, na_rm=True)
    + stat_smooth(method="lm", se=False, na_rm=True)
    + facet_wrap("~Embarked")
    + theme_minimal()
    + labs(
        title="Passenger Age and Fare by Embarkation Port",
        x="Age",
        y="Fare",
        color="Survival Status (0 = No, 1 = Yes)"
    )
)
plot.show()
