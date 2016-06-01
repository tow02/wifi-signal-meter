import subprocess
import time
import argparse
import csv

# IEEE: 802.11bgn, ESSID: "MU-Wifi"
# Frequency: 2.412 GHz
# Bit Rate: 65 Mb/s, Tx-Power= 20 dBm
# Link Quality=53/70, Signal level = -57dBm

parser = argparse.ArgumentParser(description='Display WLAN signal strength')
parser.add_argument(dest='interface', nargs='?', default='wlan0',
                    help='wlan interface (default: wlan0)')
args = parser.parse_args()

cmd = subprocess.Popen('iwconfig %s' %args.interface, shell=True,
                        stdout=subprocess.PIPE)

unix_time = time.time()

l = [line.strip() for line in cmd.stdout]

elem1 = l[0].split()
ieee = elem1[2]
essid = elem1[3].split(':')[-1].strip('"')

elem2 = l[1].split()
frequency = elem2[1].split(':')[-1] + " " + elem2[2]


elem3 = l[2].split()
bit_rate = elem3[1].split("=")[-1] + " " + elem3[2]
tx_power = elem3[3].split("=")[-1] + " " + elem3[-1]

elem4 = l[5].split()
link_quality = elem4[1].split("=")[-1]
signal_level = elem4[3].split("=")[-1] + " " + elem4[-1]

# IEEE,ESSID,Frequency,BitRate,TxPower,LinkQuality,SignalLevel,UnixTime

with open("data.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow([ieee, essid, frequency, bit_rate, tx_power, link_quality, signal_level, unix_time])
