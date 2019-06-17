#!/usr/bin/env python3

import geopandas
import argparse

def main(args):
    file_name = args.file
    zip_gdf = geopandas.read_file(file_name)
    mapping = dict()
    for col in zip_gdf.columns:
        lcol = col.lower()
        if lcol.startswith('ZCTA5CE'.lower()):
            mapping[col] = 'zip_code'
        if lcol.startswith('INTPTLAT'.lower()):
            mapping[col] = 'internal_point_latitude'
        if lcol.startswith('INTPTLON'.lower()):
            mapping[col] = 'internal_point_longitude'
    zip_gdf.rename(columns=mapping, inplace=True)
    zip_gdf['centroid_longitude'] = zip_gdf['geometry'].centroid.x
    zip_gdf['centroid_latitude'] = zip_gdf['geometry'].centroid.y
    zip_gdf['area'] = zip_gdf['geometry'].area
    zip_gdf['convex_hull_area'] = zip_gdf['geometry'].convex_hull.area
    export_keys = ['centroid_longitude', 'centroid_latitude', 'area', 'convex_hull_area',] 
    export_keys = list(mapping.values()) + export_keys
    zip_gdf[export_keys].to_csv(args.outfile, index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Convert Tiger/Line Shape file to CSV")
    parser.add_argument('file', help='File to convert')
    parser.add_argument('outfile', help='Output file name')
    args = parser.parse_args()
    main(args)
