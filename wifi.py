import os
import subprocess

# can also be written as subprocess.check_output(['netsh', 'wlan', 'show', 'networks']) but ascii decoding is needed afterwards
# or os.popen("netsh wlan show profile").read()

ssids = []
keys = []

nets = subprocess.run(['netsh', 'wlan', 'show', 'networks'], capture_output = True).stdout.decode()

ssid_data = subprocess.run(['netsh', 'wlan', 'show', 'profile'], capture_output = True).stdout.decode()
ssid_rows = ssid_data.split('\n')

for i in ssid_rows:
    if "All User Profile" in i:
        ssid = i.replace("All User Profile     :", "").strip()
        ssids.append(ssid)

for k in ssids:
    out_data = os.popen(f"netsh wlan show profile \"{k}\" key=clear").read()
    out_rows = out_data.split('\n')
    for z in out_rows:
        if "Key Content" in z:
            key = z.replace("Key Content            :", "").strip()
            keys.append(key)
        if "Key Index" in z:  # instead of key content (this means a key is not available)
            keys.append("None")

print('\n[*] All Networks\n')
print(nets)

print('\n[*] Previously Connected Networks + Keys\n')
for ssid, key in zip(ssids, keys):
    print(f'{ssid.ljust(25)} >> {key.rjust(25)}\n')
