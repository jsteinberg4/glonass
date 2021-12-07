# Author: Joshua Cheng
# quick script to split large csv into separate files for each table

import pandas as pd
from typing import List


def splitCSV(df: pd.DataFrame, filename: str, pk: str, cols: List[str]) -> None:
    df.to_csv(f'final_data/{filename}', index=False,
              columns=[pk] + cols)


def main():
    data = pd.read_csv('hipparcos_reduced.csv')

    PK = 'HIP'  # primary key for all tables
    tables = {
        'star_catalog': ['Catalog', 'Survey'],
        'star_position': ['RAdeg', 'DEdeg', 'Plx', 'pmRA', 'pmDE', 'e_RAdeg', 'e_DEdeg', 'e_Plx', 'F1', 'F2'],
        'star_system': ['Ncomp', 'MultFlag', 'm_HIP', 'theta', 'rho', 'e_rho'],
        'star_characteristics': ['Vmag', 'Hpmag', 'e_Hpmag', 'Hpscat', 'o_Hpmag', 'm_Hpmag', 'Hpmax', 'HPmin', 'Period', 'HvarType', 'Source']}

    for k, v in tables.items():
        splitCSV(data, f'{k}.csv', PK, v)


if __name__ == '__main__':
    main()
