# Author: Joshua Cheng
# generate INSERT INTO SQL commands to insert large amounts of data because the data import wizard is incredibly slow and LOAD DATA requires modification of settings that I couldn't figure out how to do
"""
Note: need to adjust max_allowed_packet using: SET GLOBAL max_allowed_packet = 10000000;
"""

import pandas as pd
from tqdm import tqdm


def insertInto(filename: str) -> str:
    df = pd.read_csv(f'final_data/{filename}')
    cmd = f"INSERT INTO {filename[:-4]} VALUES \n"
    cmds = []
    for i, row in tqdm(df.iterrows()):
        ls = []
        for c in row:
            ls.append(c.__repr__() if not pd.isna(c) else 'NULL')
        cmds.append(f"({','.join(ls)})")
    cmd += ",\n".join(cmds) + ';'
    return cmd


def createTable(filename: str) -> str:
    df = pd.read_csv(f'final_data/{filename}')
    cmd = f'DROP TABLE IF EXISTS {filename[:-4]};\n'
    cmd += f'CREATE TABLE {filename[:-4]} (\n'
    cmds = []
    for t in df:
        s = f'\t{t} '
        if df[t].dtype == 'int64':
            s += 'INT'
        elif df[t].dtype == 'float':
            s += 'DOUBLE'
        elif df[t].dtype == 'object':  # string
            s += 'VARCHAR(255)'
        else:
            raise NameError('unknown type')
        cmds.append(s)
    cmd += ',\n'.join(cmds)
    cmd += f'\n);\nALTER TABLE {filename[:-4]} ADD PRIMARY KEY (HIP);\n'
    if not filename == 'star_catalog.csv':
        cmd += f'ALTER TABLE {filename[:-4]} ADD FOREIGN KEY (HIP) REFERENCES star_catalog(HIP);'
    return cmd


def main():
    ls = ['star_catalog.csv', 'star_characteristics.csv',
          'star_position.csv', 'star_system.csv']
    for filename in ls:
        with open(f'final_data/{filename[:-4]}.sql', 'w') as f:
            f.write(
                f'USE db_glonass;\n{createTable(filename)}\n{insertInto(filename)}')


if __name__ == "__main__":
    main()
