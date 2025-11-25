
import pandas as pd
from pipeline_bass.utils.logger import get_logger
from pathlib import Path
from pipeline_bass.utils.paths import DATA_DIR, RAW_DATA, INTERIM_DATA, PROCESSED_DATA


logger = get_logger("data_pipeline", env = "dev", run_id=None, component= "ingestion", json_format=True)


def load_data (file_path: Path) -> pd.DataFrame :
    """ On va charger le jeu de données """

    logger.info("Lecture du dataframe")
    
    #si le chemin n'existe pas on veut remonter l'info 
    if not file_path.exists():
        logger.error(f"Le chemin specifie n'existe pas : {file_path}")
        raise FileNotFoundError(file_path)
    
    df = pd.read_csv(file_path)
    logger.info(f"Dataframe charge : {len(df)} lignes")
    
    return df 
    


def save_df(df: pd.DataFrame, output_path, filename: str) -> Path:
    
    logger.info("Sauvegarde du fichier csv ")
    output_path = INTERIM_DATA / filename
    
    df.to_csv(output_path)
    
    logger.info(f"Le dataframe a bien ete sauvegarde ici {output_path}")
    
    return output_path

