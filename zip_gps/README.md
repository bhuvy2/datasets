# Zip to GPS Datasets

This dataset takes 5 Digit U.S. ZIP code and maps them to their shape centroid.
Here are the qualities of the dataset

* The universe of possible zip codes are all accounted for in each particular year though they do change monthly while this aggregation is yearly
* The sample space is the universe
* The sampling method was conducted by the U.S. census below
* The derived data computes a number of columns
    * `zip_code` The zip code as of the particular year
    * `centroid_longitude` Given the shape described in the shapefile, what is the longitudinal component of the centroid
    * `centroid_latitude` Same as above but latitude
    * `internal_point_latitude` (Optional) The internal reference point provided in the census mapping
    * `internal_point_longitude` (Optional) The internal reference point provided in the mapping
    * `area` The internal area of the zip code
    * `convex_hull_area` The area of the convex hull. Can be used as a proxy measure for "normality" of the data

The data was gathered from <https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2009.html>

The datasets and script are under the CC0.
