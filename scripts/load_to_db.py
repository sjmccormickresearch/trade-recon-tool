import sqlite3
import pandas as pd
import os

# Define paths
base_dir = os.path.dirname(os.path.dirname(__file__))  # one level up to root
data_dir = os.path.join(base_dir, 'data')
db_path = os.path.join(base_dir, 'trades.db')

# Load CSVs into pandas
internal_df = pd.read_csv(os.path.join(data_dir, 'internal_trades.csv'))
broker_df = pd.read_csv(os.path.join(data_dir, 'broker_trades.csv'))

# Connect to SQLite database (creates 'trades.db' if it doesn't exist)
conn = sqlite3.connect(db_path)

# Load data into database
internal_df.to_sql('internal_trades', conn, if_exists='replace', index=False)
broker_df.to_sql('broker_trades', conn, if_exists='replace', index=False)

# Done
print("✅ CSVs loaded into SQLite database successfully.")
