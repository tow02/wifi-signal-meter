# Include the Dropbox SDK
import dropbox
import arrow
import gzip
from secret import access_token

client = dropbox.client.DropboxClient(access_token)
# print 'linked account: ', client.account_info()

time = arrow.now().isoformat()

work_directory = '/home/pi/Desktop/wifi-signal-meter/'
source_filename = '/home/pi/Desktop/wifi-signal-meter/data.csv'
destination_filename = '/icns171/' + time + '.csv'

try:
    f_csv = open(source_filename, 'r')
    response = client.put_file(destination_filename, f_csv)
    # print "uploaded:", response
    f_csv.close()
except Exception as e:
    print e
