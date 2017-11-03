
from ez_wifi_09 import*
import time
#

print "This is an automatic login to Foo network"
URL='wireless.um.edu' 
EMAIL = 'rmenon20'
PASSWORD = 'Lordoftheflies3!'

print 'checkwifi', wifi_get_state()
print wifi_get_configured_networks()

wifi_configure_new_network('umd-secure', False, 1, 'WPA-WPA2-PEAP', password='Lordoftheflies3!', identity='rmenon20')
wifi_scan_for_networks()
while wifi_is_scanning():
    time.sleep(0.5)
while wifi_get_state() != 'COMPLETED':
    wifi_connect_transient_network('umd-secure', False, 1, 'WPA-WPA2-PEAP', password='Lordoftheflies3!', identity='rmenon20')
    time.sleep(0.75)
    print wifi_get_state(), len(wifi_get_scanned_networks())
#wifi_configure_new_network(ssid, hidden, priority, security_type, password=None, identity=None)