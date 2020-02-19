# great_circle_calculator v1.1

Distance calculator tool

This tool is used for calculating great circle distances between sequential sets of lat/lon positions.
Distance is given in Km and Nautical Miles, and bearing from starting position towards end location is
in degrees (0 to 360). Distances are calculated in UTM/WGS84 projection if coordinates are located in the
same zone, otherwise from the ellipsioidal model WGS84 is used. If speed is provided, the travel time will
also be calculated.

Input can be from CSV file, which has field headers specifying which column is latitude and longitude, 
and optionally speed. Other fields are ignored.

Latitude and Longitude values can be in:
    decimal degrees
    Degrees Minutes Seconds e.g.  41 25 01N, or S17 33 08.352 (location of N/S E/W identifier can be anywhere)
    degrees decimal minutes e.g. N41 25.117, or 120 58.292W (location of N/S E/W identifier can be anywhere)
Note: DMS/DM must be separated by spaces.

Output is to GUI, and optionally to specified CSV file.

Written for Python 3.6+, and PyQt5

Executable can be generated using pyinstaller, with command:
pyinstaller --hidden-import PyQt5.sip --onefile great_circle_distance.py
