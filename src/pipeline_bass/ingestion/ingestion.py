
from pipeline_bass.utils.logger import get_logger


logger = get_logger(
    name="data_pipeline.ingestion",
    component="ingestion",
    json_format=True
)


def test_logger() -> None:
    """
    Charge un fichier JSON en DataFrame.
    """
    logger.info("Ingestion module loaded.")

    
    


