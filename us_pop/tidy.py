import pandas as pd
import argparse

area_key = "geographic_area"

def main(args):
    fname = args.file

    # Skip the ornate Excel
    df = pd.read_excel(fname, skiprows=1, header=2)

    # Rename the geographical area column
    cols = list(df.columns)
    cols[0] = area_key
    df.columns = cols

    # Drop April 1st Columns
    df.drop(df.columns[1:3], axis=1, inplace=True)

    # Filter out metadata
    ur_row = df.ix[df[area_key].str.lower()=='puerto rico'].index.tolist()
    df = df.iloc[:max(ur_row)+1]
    df[area_key] = df[area_key].str.replace(r'^[.]', '')

    # No blank rows
    df = df[df[area_key].notna()]

    # Tidy it
    tidied = pd.melt(df, id_vars=[area_key], var_name="year", value_name="population")
    tidied.to_csv(args.outfile, index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Tidy the population data from the census')
    parser.add_argument('file', help='File to parse')
    parser.add_argument('outfile', help='File to parse')
    args = parser.parse_args()
    main(args)
