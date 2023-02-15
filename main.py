from typing import Optional
import pandas as pd
from argparse import ArgumentParser
from os import listdir
from os.path import isfile, join
from functools import reduce
def create_parser() -> ArgumentParser :
    parser = ArgumentParser(description="Merge csv or xlsx files into one csv file.")
    parser.add_argument(
        "--merge_on",
        type=str,
        dest="merge_on",
        help="name of column to merge files",
        default="protocol title",
        required=False,
    )
    parser.add_argument(
        "--input_folder",
        dest="input_folder",
        type=str,
        help="path to folder with input files (e.g. `./inputs`)",
        default="./inputs",
        required=False,
    )
    parser.add_argument(
        "--output",
        dest="output",
        type=str,
        help="path and filename of output csv file(e.g. `output.csv`)",
        default="./output.csv",
        required=False,
    )
    return parser
    
def get_dataframes(input_folder: str) -> list[pd.DataFrame]:
    files = [join(input_folder, f) for f in listdir(input_folder) if isfile(join(input_folder, f))]
    dfs = []
    for f in files:
        try:
            if f.endswith("xls") or f.endswith("xlsx"):
                dfs.append(pd.read_excel(f))
            else:
                dfs.append(pd.read_csv(f))
        except Exception as e:
            print (f"Unable to read {f}")
            print (e)
    return dfs

def get_output(dfs: list[pd.DataFrame], key: str) -> Optional[pd.DataFrame] :
    if not dfs:
        return
    if len(dfs) == 1:
        return dfs[0]
    else:
        try:
            return reduce(lambda x, y: pd.merge(x, y, on=key, how="outer"), dfs)
        except Exception as e:
            print("unable to merge files")
            print (e)
    
    

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    files = [join(args.input_folder, f) for f in listdir(args.input_folder) if isfile(join(args.input_folder, f))]
    dfs = get_dataframes(args.input_folder)
    df = get_output(dfs, args.merge_on)
    if isinstance(df, pd.DataFrame):
        df.to_csv(args.output, index=False)