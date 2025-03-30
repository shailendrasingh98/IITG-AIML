import pandas as pd
import numpy as np
import scipy.stats as stats

# Creating sample data
np.random.seed(42)
data = {
    'Team': np.repeat(['India', 'Australia', 'England'], 10),
    'Score': np.concatenate([
        np.random.normal(280, 15, 10),  # India's scores
        np.random.normal(290, 15, 10),  # Australia's scores
        np.random.normal(275, 15, 10)   # England's scores
    ])
}

df = pd.DataFrame(data)

# Perform One-Way ANOVA
f_stat, p_value = stats.f_oneway(df[df['Team'] == 'India']['Score'],
                                 df[df['Team'] == 'Australia']['Score'],
                                 df[df['Team'] == 'England']['Score'])

print(f"F-Statistic: {f_stat:.2f}, P-Value: {p_value:.4f}")
