# Include the Dropbox SDK
import dropbox
from secret import access_token

client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()

try:
    client.file_delete('/icns171/backup_data.csv')
except Exception as e:
    print e

try:
    client.file_move('/icns171/data.csv', '/icns171/backup_data.csv')
except Exception as e:
    print e

try:
    f = open('/home/pi/Desktop/wifi-signal-meter/data.csv', 'r')
    response = client.put_file('/icns171/data.csv', f)
    print "uploaded:", response
    f.close()
except Exception as e:
    print e
