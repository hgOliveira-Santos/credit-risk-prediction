
import pandas as pd
import requests
import zipfile
import os
from io import BytesIO
import config
from urllib3 import response 

def ingest_credit_data(url: str) -> pd.DataFrame:
    
    # 1. Configuração inicial a partir do arquivo de configuração.
    raw_data_dir = config.RAW_DATA_DIR
    processed_data_dir = config.PROCESSED_DATA_DIR
    data_filename = config.GERMAN_CREDIT_DATA
    processed_filepath = os.path.join(processed_data_dir, data_filename)

    # 2. Download do arquivo.
    res = download_zip_file(url, raw_data_dir)


def download_zip_file(url: str, destination_folder: str) -> bool:
    print(f"Baixando e extraindo arquivos de: {url}")
    try:
        os.makedirs(destination_folder, exist_ok=True)
        
        response = requests.get(url)
        response.raise_for_status()  

        with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(destination_folder)
        
        print(f"Arquivos extraídos com sucesso para: {destination_folder}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Erro durante o download: {e}")
        return False
    except zipfile.BadZipFile:
        print("Erro: O arquivo baixado não é um ZIP válido ou está corrompido.")
        return False
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return False


def extract_datafile_from_zip(filename: str, file_path: str, destination_folder: str, file_extension: str = ".data") -> str:
    return