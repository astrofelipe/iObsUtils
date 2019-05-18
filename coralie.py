import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='Coralie catalog to iObserve')
parser.add_argument('Catalog', type=str)

args = parser.parse_args()

catalog = pd.read_csv(args.Catalog, sep='\t')
catalog = catalog.iloc[1:,1:4]
print(catalog)
catalog.to_csv(path_or_buf=args.Catalog.replace('.cat','_iob.txt'), sep=' ', header=False, index=False)
