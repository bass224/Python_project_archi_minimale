from pipeline_bass.ingestion.ingestion import load_data, save_df
from pathlib import Path
from pipeline_bass.utils.paths import DATA_DIR, RAW_DATA, INTERIM_DATA, PROCESSED_DATA


def main():
    df = load_data(Path(RAW_DATA / "sales.csv"))
    save_df(df, INTERIM_DATA, "sales_interim.csv")
   

if __name__ =="__main__":
    main()
    
