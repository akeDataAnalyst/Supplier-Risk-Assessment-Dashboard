#!/usr/bin/env python
# coding: utf-8

# #### Objective: Complete the geopolitical_risk_score column in our dataset with a mix of real and synthetic values.

# In[1]:


import pandas as pd
import numpy as np

# --- Configuration ---
# Use the geopolitical scores we got from our last run
geopolitical_scores = {
    'China': 0.5000,
    'Mexico': 0.4924,
    'USA': 0.4975,
    'Germany': 0.5000,
    'India': 0.4454,
    'Brazil': 0.5000,
    'Vietnam': 0.5000,
    'Turkey': 0.5000,
    'South Korea': 0.5020,
    'Taiwan': 0.5000
}

# --- Manually adjust scores to create a compelling narrative for the dashboard ---
# The goal is to have a range of scores to visualize on a heatmap.
# High risk countries (e.g., due to geopolitical tensions or economic instability)
geopolitical_scores['China'] = 0.85 # High risk due to trade disputes/geopolitical tensions
geopolitical_scores['Turkey'] = 0.75 # High risk due to economic volatility
geopolitical_scores['Brazil'] = 0.65 # Medium-high risk due to economic factors

# Medium-to-low risk countries
geopolitical_scores['Mexico'] = 0.55 # Medium risk (already had a score, we can keep it slightly elevated)
geopolitical_scores['India'] = 0.45 # Low-medium risk (good score, let's keep it)
geopolitical_scores['USA'] = 0.35 # Low risk
geopolitical_scores['Germany'] = 0.25 # Very low risk
geopolitical_scores['South Korea'] = 0.50 # Neutral risk
geopolitical_scores['Taiwan'] = 0.70 # Medium-high risk due to geopolitical factors
geopolitical_scores['Vietnam'] = 0.40 # Low risk

# --- Load the synthetic supplier data (from the first script run) ---
try:
    supplier_df = pd.read_csv('supplier_data.csv')
except FileNotFoundError:
    print("Error: 'supplier_data.csv' not found. Please run the data generation script from Phase 1 first.")
    exit()

# Map the final geopolitical scores to the main DataFrame
supplier_df['geopolitical_risk_score'] = supplier_df['supplier_country'].map(geopolitical_scores)

# Save the updated DataFrame
final_dataset_name = 'final_supplier_data.csv'
supplier_df.to_csv(final_dataset_name, index=False)
    
print("\nFinal dataset created successfully!")
print(f"Dataset saved as '{final_dataset_name}'.")
print("\nHere's a preview of the final dataset with all risk factors:")
print(supplier_df.head())
print("\nNow we are ready for the next phase: risk scoring and dashboard creation!")


# In[ ]:





# In[ ]:




