#!/usr/bin/env python
# coding: utf-8

# #### Phase 3: Risk Scoring and Integration

# ###### Objective: Combine all the individual risk factors (on_time_delivery_rate, quality_score, and geopolitical_risk_score) into a single, 
# master total_risk_score for each supplier. This is the core of the project's logic and business impact.

# In[1]:


import pandas as pd
import numpy as np

# --- Configuration for Risk Scoring ---
DELIVERY_RISK_WEIGHT = 0.45
QUALITY_RISK_WEIGHT = 0.45
GEOPOLITICAL_RISK_WEIGHT = 0.10

# Ensure weights sum to 1.0
if not np.isclose(DELIVERY_RISK_WEIGHT + QUALITY_RISK_WEIGHT + GEOPOLITICAL_RISK_WEIGHT, 1.0):
    raise ValueError("Risk weights must sum to 1.0")

# --- Main Script Execution ---

if __name__ == "__main__":
    # Load the final dataset from the previous phase
    try:
        df = pd.read_csv('final_supplier_data.csv')
    except FileNotFoundError:
        print("Error: 'final_supplier_data.csv' not found. Please run the previous phase's script.")
        exit()

    # --- Data Cleaning and Preparation (A quick review before scoring) ---
    # Handle the missing values we introduced in Phase 1
    # We will impute missing quality scores and delivery rates with the median.
    # This is a simple but effective strategy for a portfolio project.
    df['on_time_delivery_rate'].fillna(df['on_time_delivery_rate'].median(), inplace=True)
    df['quality_score'].fillna(df['quality_score'].median(), inplace=True)

    # --- Calculate Individual Risk Scores ---
    
    # 1. Convert on_time_delivery_rate to a risk score (0-1 scale)
    # A higher rate means lower risk, so we inverse it.
    df['delivery_risk_score'] = 1 - df['on_time_delivery_rate']

    # 2. Convert quality_score to a risk score (0-1 scale)
    # A higher score means lower risk, so we inverse and normalize it.
    df['quality_risk_score'] = 1 - (df['quality_score'] / 100)
    
    # The geopolitical_risk_score is already on a 0-1 scale, so no change is needed.
    
    # --- Calculate the Total Risk Score using the weighted algorithm ---
    df['total_risk_score'] = (
        df['delivery_risk_score'] * DELIVERY_RISK_WEIGHT +
        df['quality_risk_score'] * QUALITY_RISK_WEIGHT +
        df['geopolitical_risk_score'] * GEOPOLITICAL_RISK_WEIGHT
    )
    
    # --- Categorize suppliers based on their total risk score ---
    # We'll create bins for Low, Medium, and High risk.
    bins = [0, 0.2, 0.4, 1.0]
    labels = ['Low Risk', 'Medium Risk', 'High Risk']
    df['risk_category'] = pd.cut(df['total_risk_score'], bins=bins, labels=labels, right=False)
    
    # --- Final Dataset Preparation ---
    # We can drop the intermediate risk scores to make the final dataset cleaner for the dashboard.
    final_df_for_dashboard = df.drop(columns=['delivery_risk_score', 'quality_risk_score'])

    # Save the final dataset to a new CSV file
    final_df_for_dashboard.to_csv('dashboard_data.csv', index=False)
    
    print("Supplier risk scores calculated and categorized successfully!")
    print(f"Final dashboard data saved as 'dashboard_data.csv'.")
    print("\nHere's a preview of the final data ready for visualization:")
    print(final_df_for_dashboard.head())
    print("\nRisk category distribution:")
    print(final_df_for_dashboard['risk_category'].value_counts())
    
    print("\nWe are now ready for the final and most impactful phase: Dashboard Creation!")


# In[4]:


final_df_for_dashboard.tail(10)


# In[ ]:




