# Host Scanner
Scan hosts in your network

## How to use?
Open terminal and run following commands
```
>> sudo apt-get install git
```
```
>> git clone https://github.com/engineseller/host-scanner
```
```
>> cd host-scanner
```
```
>> chmod 755 ./hostScanner.py
```
```
>> python3 hostScanner.py -s 192.168.1.0 -e 192.168.1.256 -p 135
```

## Simple Options
```
>> python3 hostScanner.py -s <startip> -e <endip> -p <port>
```
