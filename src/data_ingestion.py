from typing import List
import pandas as pd
import requests
import zipfile
import os
from io import BytesIO
import config
import shutil


def ingest_credit_data(url: str) -> pd.DataFrame:
    
    # 1. Configuração inicial a partir do arquivo de configuração.
    raw_data_dir = config.RAW_DATA_DIR
    processed_data_dir = config.PROCESSED_DATA_DIR
    data_filename = config.GERMAN_CREDIT_DATA
    processed_filepath = os.path.join(processed_data_dir, data_filename)

    # 2. Download do arquivo e extração do arquivo .data
    if download_zip_file(url, raw_data_dir):
        if extract_data_file_from_zip(data_filename, raw_data_dir, processed_data_dir):
            return load_data_file(processed_filepath)


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


def extract_data_file_from_zip(filename: str, source_folder_path: str, destination_folder_path: str, file_extension: str = ".data") -> bool:
    try:
        for found_filename in os.listdir(source_folder_path):
            if found_filename.endswith(file_extension):
                source_filepath = os.path.join(source_folder_path, found_filename)
                renamed_source_filepath = os.path.join(source_folder_path, filename)

                if os.path.exists(renamed_source_filepath):
                    os.remove(renamed_source_filepath)
                os.rename(source_filepath, renamed_source_filepath)
                
                os.makedirs(destination_folder_path, exist_ok=True)
                
                final_destination_filepath = os.path.join(destination_folder_path, filename)
                
                if os.path.exists(final_destination_filepath):
                    os.remove(final_destination_filepath)
                shutil.move(renamed_source_filepath, final_destination_filepath)
            
            else:
                filepath_to_delete = os.path.join(source_folder_path, found_filename)
                if os.path.isfile(filepath_to_delete):
                    os.remove(filepath_to_delete)
    except Exception as e:
        print(f"Ocorreu um erro ao extrair e mover o arquivo .data: {e}")
        return False

    return True

def load_data_file(data_file_path: str, column_names: List = config.COLUMN_NAMES) -> pd.DataFrame:
    return pd.read_csv(
        data_file_path,
        sep=r'\s+',
        header=None,
        names=column_names,
        encoding='latin1'
    )
