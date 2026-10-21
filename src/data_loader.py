from pathlib import Path
import pandas as pd

class EnergyDataLoader: 
    def __init__(self, data_path: Path):
        self.data_path = data_path 

    def load_raw_data(self) -> pd.DataFrame:
        """
        Load raw PJM energy consumption data from a CSV file.
        """
        df = pd.read_csv(self.data_path) 
        
        return df
    
    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame: 
        """
        Basic preprocessing:
        - Rename columns 
        - Parse datetime 
        - Set datetime index 
        - Sort index
        """
        df = df.rename(columns={
            "Datetime": "timestamp", 
            df.columns[1]: "load"
        })

        df["timestamp"] = pd.to_datetime(df["timestamp"]) 
        df = df.set_index("timestamp") 
        df = df.sort_index() 

        return df
    
    def load_and_preprocess(self) -> pd.DataFrame:
        """
        Load and preprocess the PJM energy consumption data.
        """
        raw_df = self.load_raw_data() 
        processed_df = self.preprocess(raw_df) 
        
        return processed_df