
from pathlib import Path
import os 

ROOT_PROJECT = Path(__file__).parents[3]
#print(ROOT_PROJECT)

#Proposer  à l'utilisateur de d'envoyer le root_project via une variable d'environnement 


CUSTOM_DATA_DIR = os.getenv("my_root_variable")

if CUSTOM_DATA_DIR:
    DATA_DIR = Path(CUSTOM_DATA_DIR) / "data"
else:
   DATA_DIR = ROOT_PROJECT / "data"


RAW_DATA = DATA_DIR / "raw"
INTERIM_DATA = DATA_DIR / "interim"
PROCESSED_DATA = DATA_DIR / "processed"

#création des dossiers s'ils n'existent pas déjà : 

for file in [RAW_DATA, INTERIM_DATA, PROCESSED_DATA]:
    file.mkdir(parents=True, exist_ok= True ) 
