
from math import radians, cos, sin, asin, sqrt, atan2, degrees
import sys
import csv

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QListWidgetItem

from distance_calc_toolGUI import Ui_MainWindow

__version__ = 1.0

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    
    lats and lons in decimal degrees.
    returns distance in km
    """
    # convert decimal degrees to radians    
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a),sqrt(1-a))
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return abs(km)
    

def convert_to_dd(pos_str):
    '''
    Converts a given latitude or longitude from DMS or DM into decimal degrees.
    Component degrees minutes and seconds need to be space separated.
    
    Accepted formats:
    DMS: 41 25 01N or 120 58 57W
    DMS: S17 33 08.352 or W69 01 29.74 
    
    DM: N41 25.117 and W120 58.292
    DM: 41 25.117N and 120 58.292W
    
    returns decimal degrees as a float
    '''
    
    if pos_str == "":
        print("Cannot convert nothing!!!")
        return None
    
    try:
        dd = float(pos_str)
        return dd
    except ValueError:
        #musn't be in decimal degrees...        
        pass        
        
    make_negative = False
    #need to check to see if we need to make the position signed
    if any(x in pos_str.upper() for x in ['N', 'S', 'E', 'W']):        
        if any(x in pos_str.upper() for x in ['S', 'W']):            
            #need to convert S to negative, W to negative
            make_negative = True        
        pos_str = "{}".format(pos_str.upper().replace('N','').replace('S','').replace('E','').replace('W',''))
            
    bits = pos_str.split()
    try:
        dd = float(bits[0]) + float(bits[1])/60    
        if len(bits) == 3:
            #degrees minutes seconds        
            dd += float(bits[2])/(60*60)
    except ValueError:
        print("Could not parse string to float: {}".format(pos_str))
        raise ValueError("Invalid string: {}".format(pos_str)) 
    if make_negative:
        dd = dd * -1        
        
    return dd
    
    
def find_bearing(lat1, lon1, lat2, lon2):
    '''
    Finds the bearing from the first set of coordinates to the second, in degrees. Ensures
    the bearing is between 0 and 360 degrees.
    
    params: lats and lons need to be in decimal degrees.
    
    returns bearing in degrees as a float.    
    '''
    
    dlon = radians(lon2 - lon1)
    
    rlat1 = radians(lat1)
    rlon1 = radians(lon1)
    rlat2 = radians(lat2)
    rlon2 = radians(lon2)
    x = sin(dlon) * cos(rlat2)
    y = (cos(rlat1) * sin(rlat2)) - (sin(rlat1) * cos(rlat2) * cos(dlon))
    bearing = (degrees(atan2(x,y)) + 360) % 360    
    return bearing
    

class GreatCircleDistanceCalculator(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)
        
        self.load_csv_button.clicked.connect(self.get_csv_filepath)
        self.output_csv_button.clicked.connect(self.get_output_filepath)
        self.use_csv = True
        self.csv_file = ''
        self.csv_filepath_lineEdit.textChanged.connect(self.save_csv_filepath)
        self.output_file = ''
        self.output_filepath_lineEdit.textChanged.connect(self.save_output_filepath)
        
        self.use_fields_checkbox.stateChanged.connect(self.toggle_input)
        
        self.run_button.clicked.connect(self.find_distance)
        
        
    def get_csv_filepath(self):
        self.csv_file, _ = QFileDialog.getOpenFileName(None, "Select input CSV file")
        self.csv_filepath_lineEdit.setText(self.csv_file)
        self.use_csv = True
        self.save_csv_filepath()
        
    def save_csv_filepath(self):        
        self.csv_file = self.csv_filepath_lineEdit.text()
        
    def get_output_filepath(self):
        self.output_file, _ = QFileDialog.getSaveFileName(None, "Select Output CSV file")
        self.output_filepath_lineEdit.setText(self.output_file)
        self.save_csv_filepath()
        
    def save_output_filepath(self):
        self.output_file = self.output_filepath_lineEdit.text()
        
    def toggle_input(self, state):
    
        self.use_csv = not self.use_fields_checkbox.isChecked()
        self.csv_filepath_lineEdit.setReadOnly(self.use_csv)
        self.load_csv_button.setEnabled(self.use_csv)
        
        
    def find_distance(self):
        if self.use_csv:
            if not self.csv_file:
                self.txt.setText("No csv file specified")
            else:
                self.txt.setText('')
                self.run_csv_file()
        else:
            self.run_fields()

    def run_fields(self):
        '''
        Takes the positions from the manual input fields and calculates great circle distance
        in kilometers and nautical miles, as well as bearing from north in degrees.
        
        Note: only outputs to GUI, not to CSV.
        '''
    
        try:
            lat1 = convert_to_dd(self.latitude_input_1.text())
            lon1 = convert_to_dd(self.longitude_input_1.text())
            lat2 = convert_to_dd(self.latitude_input_2.text())
            lon2 = convert_to_dd(self.longitude_input_2.text())
        except ValueError as err:
            self.txt.setText("Error parsing position: {}".format(err.message))
            return
            
        
        if lat1 is None or lon1 is None or lat2 is None or lon2 is None:            
            self.txt.setText("Missing latitude or longitude field")
            return
        
        km = haversine(lon1, lat1, lon2, lat2)
        nmi = km / 1.852
        
        bearing = find_bearing(lat1, lon1, lat2, lon2)
        
        self.txt.setText("{:.3f} km, {:.3f} nmi, bearing: {:.1f}".format(km, nmi, bearing))
        
        
    def run_csv_file(self):
        '''
        Reads a given CSV file of sequential locations, and calculates great circle
        distance between the proceeding points. It is assumed that the locations
        provided are the sequence in which to calculate distances.
        
        The fields for latitude and longitude are determined by searching the header
        for fields containing 'lat' and 'lon', and is case insensitive for the search.
        
        The distances and bearings are output to the GUI, and optionally output to 
        CSV as well, if a filename is provided.
        '''

        with open(self.csv_file) as csvfile:

            lat_idx, lon_idx = None, None
            
            reader = csv.reader(csvfile)
            headers = next(reader, None)    
            
            for field_idx in range(len(headers)):        
                if 'lat' in headers[field_idx].lower():            
                    lat_idx = field_idx
                elif 'lon' in headers[field_idx].lower():            
                    lon_idx = field_idx    
            
            if lat_idx is None or lon_idx is None:
                self.txt.setText("cannot find lat/lon header fields in {}".format(self.csv_file))
                return
            
            past_first = False
            lats, lons, kms, nmis, bearings = [], [], [], [], []
            for row in reader:        
                lats.append(convert_to_dd(row[lat_idx]))
                lons.append(convert_to_dd(row[lon_idx]))
                
                if past_first:
                    kms.append(haversine(lons[-2],lats[-2], lons[-1], lats[-1]))
                    nmis.append(kms[-1] / 1.852) #conversion from km to nautical miles
                    bearings.append(find_bearing(lats[-2], lons[-2],lats[-1], lons[-1]))
                    #self.txt.append("{}, {} to {}, {} --> {}km\n".format(lats[-2], lons[-2], lats[-1],lons[-1], kms[-1]))
                    self.txt.append("{:.3f} km, {:.3f} nmi, {:.2f} deg".format(kms[-1], nmis[-1], bearings[-1]))
                else:
                    past_first = True
                    
        if self.output_file:
            with open(self.output_file, 'w') as outfile:
                outfile.write("{},{},{},{},{},{},{}\n".format("latitude_1","longitude_1","latitude_2","longitude_2","distance (km)", "distance (nmi)","bearing (degrees)"))
                for i in range(len(kms)):
                    outfile.write("{},{},{},{},{:.3f},{:.3f},{:.3f}\n".format(lats[i],lons[i],lats[i+1],lons[i+1],kms[i], nmis[i], bearings[i]))




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QMainWindow()
    dialog.setWindowTitle("Distanace calculator tool v{}".format(__version__))
    prog = GreatCircleDistanceCalculator(dialog) 
    dialog.show()
    sys.exit(app.exec_())
    
    








