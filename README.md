# wifi-check
> Uses the netsh tool <br>
> Finds the wifi passwords of networks you have previously connected to <br>
> Does NOT attempt to crack passwords of other networks

#### Usage
```python
python3 wifi.py
```

#### Sample Output
```
[*] All Networks


Interface name : Wi-Fi
There are 1 networks currently visible.

SSID 1 : HomeNetwork
    Network type            : Infrastructure
    Authentication          : WPA3-Personal
    Encryption              : CCMP



[*] Previously Connected Networks + Keys
DeltaWiFi.com             >>                      None

Caribou Coffee            >>                      None

HomeNetwork               >>                      Password123
```

