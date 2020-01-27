# great_circle_calculator

Distance calculator tool

This tool is used for calculating great circle distances between sequential sets of lat/lon positions.
Distance is given in Km and Nautical Miles, and bearing from starting position towards end location is
in degrees (0 to 360). Distances are calculated using the haversine formula.

Input can be from CSV file, which has field headers specifying which column is latitude and longitude. other
fields are ignored.

Output is to GUI, and optionally to specified CSV file.
