############################################################################################
####                      LEITURA DIRETA DO ARQUIVO PARQUET                             ####
############################################################################################
import pandas as pd 
import polars as pl 
from datetime import datetime
# pip install fastparquet,  para ler o arquivo parquet
import matplotlib.pyplot as plt
import numpy as np

ENDERECO_DADOS = r'./../dados/'

try:
    print('Lendo arquivo Parquet ...')
    inicio = datetime.now()

    df_plano_execucao = (
        pl.scan_parquet(
            ENDERECO_DADOS + 'bolsa_familia.parquet' # Dados
            # Delimitar as Séries
            # --- Técnica de agrupamento
            # Agrupamento

            # Soma

            # Ordenar
                                        
        )
    )
    df_bolsa_familia = df_plano_execucao.collect()  # Coletando os dados
    print(df_bolsa_familia.head())

except Exception as e:
    print(f'Erro ao ler arquivo parquet {e}')