
import pandas as pd
import numpy as np

DELIVERY_RISK_WEIGHT = 0.45
QUALITY_RISK_WEIGHT = 0.45
GEOPOLITICAL_RISK_WEIGHT = 0.10

if not np.isclose(DELIVERY_RISK_WEIGHT + QUALITY_RISK_WEIGHT + GEOPOLITICAL_RISK_WEIGHT, 1.0):
    raise ValueError("Risk weights must sum to 1.0")

if __name__ == "__main__":
    # Load the final dataset from the previous phase
    try:
        df = pd.read_csv('final_supplier_data.csv')
    except FileNotFoundError:
        print("Error: 'final_supplier_data.csv' not found. Please run the previous phase's script.")
        exit()

    df['on_time_delivery_rate'].fillna(df['on_time_delivery_rate'].median(), inplace=True)
    df['quality_score'].fillna(df['quality_score'].median(), inplace=True)

    df['delivery_risk_score'] = 1 - df['on_time_delivery_rate']

    df['quality_risk_score'] = 1 - (df['quality_score'] / 100)
    
    df['total_risk_score'] = (
        df['delivery_risk_score'] * DELIVERY_RISK_WEIGHT +
        df['quality_risk_score'] * QUALITY_RISK_WEIGHT +
        df['geopolitical_risk_score'] * GEOPOLITICAL_RISK_WEIGHT
    )
    
    # bins for Low, Medium, and High risk.
    bins = [0, 0.2, 0.4, 1.0]
    labels = ['Low Risk', 'Medium Risk', 'High Risk']
    df['risk_category'] = pd.cut(df['total_risk_score'], bins=bins, labels=labels, right=False)
    
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


final_df_for_dashboard.tail(10)
