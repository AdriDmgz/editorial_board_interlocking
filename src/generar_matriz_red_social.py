import re
from timeit import repeat
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
#from sparse_dot_topn import awesome_cossim_topn
#from ngram import NGram
from fuzzywuzzy import fuzz


path = f'data/'
filename = '1EBMembers_v5.0_FinalAffiliation_Fixed_Unified'
extension = 'xlsx'

df = pd.read_excel(f'{path}/{filename}.{extension}')
df = df.drop_duplicates(subset=['UnifName','UnifAffiliationName','UnifAffiliationCountry','JournalId'])
df.to_excel(path + filename + '_NoDuplicates.' + extension, index=False)

#df['JournalId'] = df['JournalId'].astype(str).str[1:].astype('int32')
df = df.rename(columns={'UnifName': 'Name', 'UnifAffiliationName': 'AffiliationName', 'UnifAffiliationCountry': 'AffiliationCountry'})
groupby = df.groupby(['Name','AffiliationName','AffiliationCountry'],dropna=False)
print(str(groupby.ngroups)+" unique editors")

df.insert(0,'Id',groupby.ngroup())

editors_ids = np.sort(df['Id'].unique())
journals_ids = np.sort(df['JournalId'].unique())

final_df = df.drop(['JournalId'], axis=1).drop_duplicates(subset=['Id'])
final_df.to_excel(f'{path}/1EBMembers_v5.0_Final.{extension}', index=False)

ids_array = np.concatenate([editors_ids,journals_ids])
df_nodes = pd.DataFrame({'Id':ids_array})
df_nodes.to_excel(f'{path}/0nodes_v5.0.xlsx', index=False)

ids = df['Id']
journals = df['JournalId'] 

df_edges = pd.crosstab(ids,journals)
print("Crosstab done")
df_edges.replace(0,np.nan,inplace=True)
df_edges = df_edges.astype(dtype="Int64") # Para que los valores se impriman como int, no como float
print("Generating CSV")
df_edges.to_csv(f'{path}/0edges_v5.0.csv', index=False, header=False, sep=';')