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
    df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    # Filtrando informações
    df_filtrado = df_bolsa_familia.filter(pl.col('VALOR PARCELA') > 3500)
    print(df_filtrado.shape)

    print(df_bolsa_familia.head())
    print(df_bolsa_familia.sort('VALOR PARCELA', descending=True).head(20))

    final = datetime.now()
    print(f'\nTotal do tempo gasto {final - inicio}')

except Exception as e:
    print(f'Erro ao ler arquivo parquet {e}')