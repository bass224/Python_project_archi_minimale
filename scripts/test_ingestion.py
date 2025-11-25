from pipeline_bass.ingestion.ingestion import load_data, save_df, load_json
from pathlib import Path
from pipeline_bass.utils.paths import DATA_DIR, RAW_DATA, INTERIM_DATA, PROCESSED_DATA
import json

def main():
    
    df = load_data(Path(RAW_DATA / "sales.csv"))
    users = load_json(Path("data/raw/users.json"))
    
    save_df(df, INTERIM_DATA, "sales_interim.csv")
    save_df(users,INTERIM_DATA, "users_interim.csv")

if __name__ =="__main__":
    main()
    

