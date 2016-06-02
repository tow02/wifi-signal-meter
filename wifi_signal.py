from wifi import Cell, Scheme
import csv
import arrow

print "Entering wifi-signal.py"

SSID = "MU-WiFi"
csv_file = "/home/pi/Desktop/wifi-signal-meter/data.csv"

cells = Cell.all('wlan0')
time = arrow.now().isoformat()

found = False

# ssid,signal,quality,frequency,datetime

with open(csv_file, 'a') as f:
    writer = csv.writer(f)
    for cell in cells:
        if cell.ssid == SSID:
            found = True
            print "Found MU-WiFi"
        writer.writerow([cell.ssid, cell.signal, cell.quality, cell.frequency, time])

    if not found:
        print "Not found MU-WiFi"
        writer.writerow([SSID, '0', '0', '0', time])

print "Exit wifi-signal.py"
