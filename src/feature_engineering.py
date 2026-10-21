import pandas as pd
import holidays
import numpy as np

class FeatureEngineer:
    def __init__(self, country="US", mode="train"):
        self.country = country
        self.mode = mode
        self.us_holidays = holidays.CountryHoliday(country)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        
        # 1. Basic Temporal Features
        df['hour'] = df.index.hour
        df['dayofweek'] = df.index.dayofweek
        df['month'] = df.index.month
        df['year'] = df.index.year
        
        # 2. Holiday & Weekend flags
        df['is_holiday'] = df.index.isin(self.us_holidays).astype(int)
        df['is_weekend'] = df['dayofweek'].isin([5, 6]).astype(int)
        df['is_working_day'] = ((df['is_holiday'] == 0) & (df['is_weekend'] == 0)).astype(int)

        # 3. Dubai Weather Simulation
        base_temp = 25 + 15 * np.sin(2 * np.pi * (df['month'] - 3) / 12)
        diurnal_temp = 7 * np.sin(2 * np.pi * (df['hour'] - 6) / 24)
        
        df['temperature_celsius'] = base_temp + diurnal_temp
        df['temperature_celsius'] = df['temperature_celsius'].clip(15, 48)
        
        df['humidity_pct'] = 80 - (df['temperature_celsius'] * 1.2) + np.random.normal(0, 3, len(df))
        df['humidity_pct'] = df['humidity_pct'].clip(15, 95)

        return df
