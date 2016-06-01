from wifi import Cell, Scheme
import time
import csv

print "Entering wifi-signal.py"

SSID = "MU-WiFi"
csv_file = "/home/pi/Desktop/wifi-signal-meter/data.csv"

cells = Cell.all('wlan0')
unix_time = time.time()

for cell in cells:
    if cell.ssid == SSID:
        with open(csv_file, 'a') as f:
            writer = csv.writer(f)
            # ssid,signal,quality,frequency,unix_time
            writer.writerow([cell.ssid, cell.signal, cell.quality, cell.frequency, unix_time])
            print "Write to data.csv"

print "Exit wifi-signal.py"
