#!/usr/bin/env python3

import geopandas
import argparse

def main(args):
    file_name = args.file
    zip_gdf = geopandas.read_file(file_name)
    zip_gdf.rename(columns=dict(ZCTA5CE10='zip_code', INTPTLAT10='internal_point_latitude', INTPTLON10='internal_point_longitude'), inplace=True)
    zip_gdf['centroid_longitude'] = zip_gdf['geometry'].centroid.x
    zip_gdf['centroid_latitude'] = zip_gdf['geometry'].centroid.y
    zip_gdf['area'] = zip_gdf['geometry'].area
    zip_gdf['convex_hull_area'] = zip_gdf['geometry'].convex_hull.area
    zip_gdf[['zip_code', 'centroid_longitude', 'centroid_latitude', 'internal_point_latitude', 'internal_point_longitude', 'area', 'convex_hull_area']].to_csv('Output file name', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Convert Tiger/Line Shape file to CSV")
    parser.add_argument('file', help='File to convert')
    parser.add_argument('outfile', help='Output file name')
    args = parser.parse_args()
    main(args)
