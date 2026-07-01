############################################################################################
####                      LEITURA DIRETA DO ARQUIVO PARQUET                             ####
############################################################################################
import pandas as pd 
import polars as pl 
from datetime import datetime
# pip install fastparquet,  para ler o arquivo parquet

ENDERECO_DADOS = r'./../dados/'

try:
    print('Lendo arquivo Parquet ...')
    inicio = datetime.now()
    # With pandas
    #df_bolsa_familia = pd.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    # With polars
    #df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    # Leitura preguiçosa With polars
    #df_bolsa_familia = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    #print(df_bolsa_familia.head())
    
    ###############
    df_plano_execucao = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    df_bolsa_familia = df_plano_execucao.collect()  # Coletando os dados
    print(df_bolsa_familia.head())

    final = datetime.now()
    print(f'\nTotal do tempo gasto {final - inicio}')

except Exception as e:
    print(f'Erro ao ler arquivo parquet {e}')