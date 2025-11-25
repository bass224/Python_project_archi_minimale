
#on va faire un script qui va lancer tout le pipeline de data engineering : ingestion, transformation,

import uuid
import pandas as pd

from pipeline_bass.utils.logger import get_logger
from pipeline_bass.utils.paths import RAW_DATA, INTERIM_DATA, PROCESSED_DATA

from pipeline_bass.ingestion.ingestion import load_data, load_json, save_df
from pipeline_bass.transformation.transformation import (
    clean_users,
    clean_sales,
    enrich_sales_with_users,
    save_processed
)


def main():

    # ------------------------------------------------------
    # 1. créer un run_id unique (très utile en production)
    # ------------------------------------------------------
    run_id = str(uuid.uuid4()) #Chaque exécution du pipeline a un ID unique.
    #C’est exactement ce que font Airflow, GCP Dataflow ou Databricks pour tracer un run.

    logger = get_logger(
        name="pipeline_bass.run",
        component="pipeline",
        run_id=run_id,
        json_format=True
    )

    logger.info("Pipeline started")

    try:
        # --------------------------------------------------
        # 2. INGESTION
        # --------------------------------------------------
        logger.info("Step 1: Ingestion")

        users = load_json(RAW_DATA / "users.json")
        sales = load_data(RAW_DATA / "sales.csv")

        save_df(users,INTERIM_DATA, "users_interim")
        save_df(sales, INTERIM_DATA, "sales_interim")

        # --------------------------------------------------
        # 3. TRANSFORMATION
        # --------------------------------------------------
        logger.info("Step 2: Transformation")

        users_clean = clean_users(users)
        sales_clean = clean_sales(sales)

        merged = enrich_sales_with_users(users_clean, sales_clean)

        # --------------------------------------------------
        # 4. EXPORT (Processed)
        # --------------------------------------------------
        logger.info("Step 3: Saving processed data")

        save_processed(merged, "sales_enriched")

        logger.info("Pipeline finished successfully")

    except Exception as e:
        logger.error(f"Pipeline failed with error: {e}")
        raise


if __name__ == "__main__":
    main()
