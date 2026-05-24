import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D

# ── Load world.csv ──────────────────────────────────────────────────────────
df = pd.read_csv("/mnt/user-data/uploads/world.csv")

# Replicate C logic: avg_income_with = income_with_billionaire / population_with_billionaire
df["avg_income_with"] = df["income_with_billionaire"] / df["population_with_billionaire"]
data = np.sort(df["avg_income_with"].dropna().values)
n = len(data)

# ── Quartiles (match C's simple index method) ────────────────────────────────
Q1 = np.percentile(data, 25)
Q2 = np.percentile(data, 50)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1

# 3×IQR fences (as used in the C code)
lower_fence = Q1 - 3 * IQR
upper_fence = Q3 + 3 * IQR

# ── Adjacent values (LAV / UAV) ───────────────────────────────────────────────
# LAV = smallest value still >= lower_fence
# UAV = largest value  still <= upper_fence
lav = data[data >= lower_fence].min()
uav = data[data <= upper_fence].max()

# ── Outliers ──────────────────────────────────────────────────────────────────
upper_outliers = df[df["avg_income_with"] > upper_fence]
lower_outliers = df[df["avg_income_with"] < lower_fence]

print(f"n={n}  Q1={Q1:.2f}  Q2={Q2:.2f}  Q3={Q3:.2f}  IQR={IQR:.2f}")
print(f"Lower fence (Q1-3×IQR)={lower_fence:.2f}   LAV={lav:.2f}")
print(f"Upper fence (Q3+3×IQR)={upper_fence:.2f}   UAV={uav:.2f}")
print(f"Upper outliers ({len(upper_outliers)}):\n", upper_outliers[["country","avg_income_with"]].to_string())
print(f"Lower outliers ({len(lower_outliers)}):\n", lower_outliers[["country","avg_income_with"]].to_string())


# ════════════════════════════════════════════════════════════════════════════
# SHARED DRAWING HELPER
# ════════════════════════════════════════════════════════════════════════════
COLORS = {
    "box":     "#3B82F6",   # bright blue fill
    "median":  "#60A5FA",   # lighter blue median
    "whisker": "#93C5FD",   # pale blue whisker
    "lav_uav": "#38BDF8",   # sky blue LAV/UAV caps
    "upper_o": "#F472B6",   # pink – upper outliers (pops on dark bg)
    "lower_o": "#A78BFA",   # violet – lower outliers
    "label":   "#E0F2FE",   # near-white for labels on black
    "bg":      "#000000",   # pure black background
    "grid":    "#1E3A5F",   # very dark blue grid
}

def draw_custom_boxplot(ax, show_lower_outliers=True,
                        y_log=False, title=""):
    """Draw a fully custom boxplot that matches the project spec."""

    # ── decide y-axis scale ──────────────────────────────────────────────
    if y_log:
        ax.set_yscale("log")
    ax.set_xlim(0, 2)

    # ── main box (Q1 → Q3) ───────────────────────────────────────────────
    box_x   = [0.6, 1.4, 1.4, 0.6, 0.6]
    box_y   = [Q1,  Q1,  Q3,  Q3,  Q1 ]
    ax.fill(box_x, box_y, color=COLORS["box"], alpha=0.25, zorder=2)
    ax.plot(box_x, box_y, color=COLORS["box"], lw=2,   zorder=3)

    # ── median line ──────────────────────────────────────────────────────
    ax.plot([0.6, 1.4], [Q2, Q2],
            color=COLORS["median"], lw=2.5, zorder=4, label=f"Q2 / Median = {Q2:,.0f}")

    # ── whiskers (box → LAV / UAV) ───────────────────────────────────────
    ax.plot([1.0, 1.0], [Q1, lav],
            color=COLORS["whisker"], lw=1.8, linestyle="--", zorder=2)
    ax.plot([1.0, 1.0], [Q3, uav],
            color=COLORS["whisker"], lw=1.8, linestyle="--", zorder=2)

    # ── LAV / UAV caps ───────────────────────────────────────────────────
    for y_cap, lab in [(lav, f"LAV = {lav:,.0f}"), (uav, f"UAV = {uav:,.0f}")]:
        ax.plot([0.75, 1.25], [y_cap, y_cap],
                color=COLORS["lav_uav"], lw=2.8, zorder=3)

    # ── upper outliers ───────────────────────────────────────────────────
    for _, row in upper_outliers.iterrows():
        ax.scatter(1.0, row["avg_income_with"],
                   color=COLORS["upper_o"], s=80, zorder=5,
                   marker="^", edgecolors="#FBCFE8", linewidths=0.8)

    # ── lower outliers (only if requested) ───────────────────────────────
    if show_lower_outliers and len(lower_outliers) > 0:
        for _, row in lower_outliers.iterrows():
            ax.scatter(1.0, row["avg_income_with"],
                       color=COLORS["lower_o"], s=80, zorder=5,
                       marker="v", edgecolors="#DDD6FE", linewidths=0.8)

    # ── annotation labels for Q1, Q2, Q3, LAV, UAV ───────────────────────
    annots = [
        (Q1,  f"Q1 = {Q1:,.0f}",   "right"),
        (Q2,  f"Q2 = {Q2:,.0f}",   "right"),
        (Q3,  f"Q3 = {Q3:,.0f}",   "right"),
        (lav, f"LAV = {lav:,.0f}", "left"),
        (uav, f"UAV = {uav:,.0f}", "left"),
    ]
    for y_val, label, side in annots:
        x_pos = 0.58 if side == "right" else 1.42
        ha    = "right" if side == "right" else "left"
        ax.annotate(label,
                    xy=(x_pos, y_val),
                    fontsize=8.5, color=COLORS["label"],
                    ha=ha, va="center",
                    fontweight="semibold")

    # ── legend ───────────────────────────────────────────────────────────
    legend_elements = [
        mpatches.Patch(facecolor=COLORS["box"],    alpha=0.35, edgecolor=COLORS["box"],
                       label="IQR Box (Q1–Q3)"),
        Line2D([0],[0], color=COLORS["median"],  lw=2.5,  label=f"Median (Q2) = {Q2:,.0f}"),
        Line2D([0],[0], color=COLORS["lav_uav"], lw=2.5,  label=f"LAV={lav:,.0f}  |  UAV={uav:,.0f}"),
        Line2D([0],[0], color=COLORS["whisker"], lw=1.8, linestyle="--",
               label="Whisker (LAV↔Q1, Q3↔UAV)"),
        Line2D([0],[0], marker="^", color=COLORS["upper_o"],
               markersize=9, linestyle="None", label="Upper Extreme Outliers"),
    ]
    if show_lower_outliers:
        legend_elements.append(
            Line2D([0],[0], marker="v", color=COLORS["lower_o"],
                   markersize=9, linestyle="None", label="Lower Extreme Outliers")
        )
    ax.legend(handles=legend_elements, loc="upper left",
              fontsize=8, framealpha=0.15,
              facecolor="#0F172A", edgecolor="#3B82F6",
              labelcolor=COLORS["label"])

    # ── axes cosmetics ────────────────────────────────────────────────────
    ax.set_title(title, fontsize=12, fontweight="bold",
                 color=COLORS["label"], pad=12)
    ax.set_xticks([])
    ax.set_ylabel("Avg Per Capita Income WITH Billionaires (USD)", fontsize=9,
                  color=COLORS["label"])
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, _: f"${x:,.0f}")
    )
    ax.tick_params(axis="y", colors=COLORS["label"])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#1E3A5F")
    ax.spines["bottom"].set_color("#1E3A5F")
    ax.grid(axis="y", linestyle=":", alpha=0.3, zorder=0, color=COLORS["lav_uav"])
    ax.set_facecolor(COLORS["bg"])


# ════════════════════════════════════════════════════════════════════════════
# FIGURE 1 – Upper extreme outliers only, log scale for visibility
# ════════════════════════════════════════════════════════════════════════════
fig1, ax1 = plt.subplots(figsize=(9, 9))
fig1.patch.set_facecolor("#000000")

draw_custom_boxplot(
    ax1,
    show_lower_outliers=False,
    y_log=True,
    title="Analysis 2 – BoxPlot 1\nAvg Income WITH Billionaires | Upper Extreme Outliers Only (3×IQR fence)"
)

fig1.tight_layout(pad=2.0)
fig1.savefig("/mnt/user-data/outputs/boxplot1_upper_outliers_only.png",
             dpi=150, bbox_inches="tight")
print("Saved: boxplot1_upper_outliers_only.png")


# ════════════════════════════════════════════════════════════════════════════
# FIGURE 2 – Both upper AND lower extreme outliers, log scale
# ════════════════════════════════════════════════════════════════════════════
fig2, ax2 = plt.subplots(figsize=(9, 9))
fig2.patch.set_facecolor("#000000")

draw_custom_boxplot(
    ax2,
    show_lower_outliers=True,
    y_log=True,
    title="Analysis 2 – BoxPlot 2\nAvg Income WITH Billionaires | Upper AND Lower Extreme Outliers (3×IQR fence)"
)

fig2.tight_layout(pad=2.0)
fig2.savefig("/mnt/user-data/outputs/boxplot2_both_outliers.png",
             dpi=150, bbox_inches="tight")
print("Saved: boxplot2_both_outliers.png")

plt.show()
