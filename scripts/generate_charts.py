import matplotlib.pyplot as plt
import numpy as np

bg_color = '#0F172A'
purple = '#9333ea'
blue = '#3b82f6'
text_color = '#F8FAFC'

def generate_cover_art():
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 4), facecolor=bg_color)
    ax.set_facecolor(bg_color)
    x = np.linspace(0, 10, 1000)
    y1 = np.sin(x) * np.exp(-0.2 * x)
    y2 = np.cos(x) * np.exp(-0.2 * x)
    y3 = np.sin(x*4) * 0.1
    y4 = np.cos(x*2) * np.exp(-0.4 * x)
    
    ax.plot(x, y1, color=blue, lw=3, alpha=0.9)
    ax.plot(x, y2, color=purple, lw=3, alpha=0.9)
    ax.plot(x, y3, color=text_color, lw=1, alpha=0.3, zorder=0)
    ax.fill_between(x, y1, y2, color=blue, alpha=0.1)
    
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('docs/cover_graphic.png', dpi=300, facecolor=bg_color, bbox_inches='tight', transparent=True)
    plt.close()

def generate_performance_chart():
    plt.style.use('default')
    fig, ax = plt.subplots(figsize=(9, 6)) # Made larger
    
    labels = ['MemoryGraft', 'eTAMP']
    base_success = [77.0, 59.1]  # Updated with N=1000 empirical data
    memshield_success = [0.1, 0.1]
    
    x = np.arange(len(labels))
    width = 0.35
    
    rects1 = ax.bar(x - width/2, base_success, width, label='Unprotected LTM', color='#EF4444')
    rects2 = ax.bar(x + width/2, memshield_success, width, label='MemShield Defended', color=blue)
    
    ax.set_ylabel('Attack Success Rate (%)', fontweight='bold', fontsize=14)
    ax.set_title('Poisoning Efficacy: Base vs. MemShield (N=1000 Trials)', fontweight='bold', pad=15, fontsize=16)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontweight='bold', fontsize=13)
    ax.set_ylim(0, 100)
    
    ax.grid(axis='y', linestyle='--', alpha=0.6)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    ax.legend(frameon=True, shadow=True, fancybox=True, fontsize=12)
    for rect in rects1 + rects2:
        height = rect.get_height()
        ax.annotate(f'{height}%',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 5), textcoords="offset points",
                    ha='center', va='bottom', fontweight='bold', fontsize=13)
                    
    plt.tight_layout()
    plt.savefig('docs/performance_chart.png', dpi=300, bbox_inches='tight')
    plt.close()

def generate_trust_decay_chart():
    plt.style.use('default')
    fig, ax = plt.subplots(figsize=(9, 6)) # Made larger
    
    t = np.linspace(0, 30, 200) # days
    lam = 0.1
    direct = 1.0 * np.exp(-0.005 * t)
    tool = 0.5 * np.exp(-lam * t)
    scrape = 0.2 * np.exp(-lam * t * 2) 
    
    ax.plot(t, direct, label='DIRECT_USER (Anchor)', color='#10B981', lw=4)
    ax.plot(t, tool, label='TOOL_OUTPUT', color=blue, lw=4)
    ax.plot(t, scrape, label='WEB_SCRAPE', color='#F59E0B', lw=4)
    
    ax.set_xlabel('Time Evaluated (Days Since Ingestion)', fontweight='bold', fontsize=14)
    ax.set_ylabel('Target Trust Density', fontweight='bold', fontsize=14)
    ax.set_title('Trust-Weighted Retrieval Decay Simulation over 30 Epochs', fontweight='bold', pad=15, fontsize=16)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend(frameon=True, fancybox=True, shadow=True, fontsize=12)
    
    plt.tight_layout()
    plt.savefig('docs/trust_decay.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_cover_art()
    generate_performance_chart()
    generate_trust_decay_chart()
