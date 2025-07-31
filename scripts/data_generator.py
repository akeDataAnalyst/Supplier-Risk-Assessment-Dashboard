
import pandas as pd
import numpy as np
from datetime import date, timedelta

NUM_SUPPLIERS = 50
NUM_MONTHS = 12
START_DATE = date(2024, 1, 1)

# List of hypothetical countries our suppliers are in
SUPPLIER_COUNTRIES = ['China', 'Mexico', 'USA', 'Germany', 'India', 'Brazil', 'Vietnam', 'Turkey', 'South Korea', 'Taiwan']

np.random.seed(42) # for reproducibility

supplier_ids = [f'SUP-{i:03d}' for i in range(1, NUM_SUPPLIERS + 1)]
supplier_countries = np.random.choice(SUPPLIER_COUNTRIES, size=NUM_SUPPLIERS)

suppliers_df = pd.DataFrame({
    'supplier_id': supplier_ids,
    'supplier_country': supplier_countries
})

all_data = []
current_date = START_DATE
for i in range(NUM_MONTHS):
    # Simulate on-time delivery rates with some variation
    on_time_delivery = np.random.uniform(low=0.75, high=0.99, size=NUM_SUPPLIERS)
    
    # Simulate quality scores, with a few low-performing suppliers
    quality_score = np.random.uniform(low=85, high=100, size=NUM_SUPPLIERS)
    
    # Introduce some "poor performers"
    if i == 5: # In the 6th month, a few suppliers perform poorly
        poor_performers_indices = np.random.choice(NUM_SUPPLIERS, size=5, replace=False)
        on_time_delivery[poor_performers_indices] = np.random.uniform(low=0.5, high=0.7, size=5)
        quality_score[poor_performers_indices] = np.random.uniform(low=70, high=85, size=5)

    month_data = pd.DataFrame({
        'supplier_id': supplier_ids,
        'date': current_date,
        'on_time_delivery_rate': on_time_delivery,
        'quality_score': quality_score
    })
    
    all_data.append(month_data)
    current_date += timedelta(days=30) # move to next month

performance_df = pd.concat(all_data, ignore_index=True)

performance_df.loc[performance_df.sample(frac=0.05).index, 'quality_score'] = np.nan
performance_df.loc[performance_df.sample(frac=0.03).index, 'on_time_delivery_rate'] = np.nan

final_df = pd.merge(performance_df, suppliers_df, on='supplier_id')

final_df['geopolitical_risk_score'] = 0.0

# Save the dataset to a CSV file
final_df.to_csv('supplier_data.csv', index=False)

print("Synthetic dataset created successfully!")
print(final_df.head())
print(f"Total rows: {len(final_df)}")

