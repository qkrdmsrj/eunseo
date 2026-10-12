import os
import matplotlib.pyplot as plt

def generate_dashboard():
    os.makedirs("docs", exist_ok=True)
    
    metrics = {
        "Deployment Frequency": 5,
        "Lead Time (min)": 12.5,
        "MTTR (min)": 15.0,
        "Change Failure Rate (%)": 0.0
    }
    
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle("DORA Metrics Dashboard (Saver-AI)", fontsize=16, fontweight='bold')
    
    colors = ['#4CAF50', '#2196F3', '#FF9800', '#F44336']
    metric_names = list(metrics.keys())
    metric_values = list(metrics.values())
    
    for i, ax in enumerate(axes.flat):
        ax.bar([metric_names[i]], [metric_values[i]], color=colors[i], width=0.4)
        ax.set_title(metric_names[i], fontsize=11, fontweight='bold')
        ax.set_ylim(0, max(metric_values[i] * 1.3, 10))
        for p in ax.patches:
            ax.annotate(f"{p.get_height()}", (p.get_x() + p.get_width() / 2., p.get_height() / 2),
                        ha='center', va='center', fontsize=12, color='white', fontweight='bold')
        ax.grid(axis='y', linestyle='--', alpha=0.5)
        
    plt.tight_layout()
    plt.savefig("docs/dora_dashboard.png", dpi=300)
    print("SUCCESS: DORA Dashboard image generated at docs/dora_dashboard.png")

if __name__ == "__main__":
    generate_dashboard()
