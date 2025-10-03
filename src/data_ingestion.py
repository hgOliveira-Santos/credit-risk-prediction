import pandas as pd
import config

def ingest_credit_data(url: str) -> pd.DataFrame:
    
    # 1. Configuração inicial a partir do arquivo de configuração.
    zip_save_path = config.RAW_DATA_DIR
    data_filename = config.GERMAN_CREDIT_DATA

    # 2. Download do arquivo.
    download_zip_file(url, zip_save_path)

    return 


def download_zip_file(url: str, destination_folder: str) -> bool:
    pass


def extract_datafile_from_zip(zip_path: str, destination_folder: str, file_extension: str = ".data") -> str:
    pass