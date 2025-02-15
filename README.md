# domainenum

A basic tool inspired by Sublist3r / subbrute specifically designed for my wildcard* scope bug-bounty needs. Quickly identify unique subdomains, their response codes, and the length of their response.
```
usage: domain_enum.py [-h] [-a] domain

Enumeration tool for finding and requesting HTML response.

positional arguments:
  domain      Domain which you wish to scan.

options:
  -h, --help  show this help message and exit
  -a          Display all information, no-ping by default.
```

### Example command
```bash
# python3 domain_enum.py TARGET_DOMAIN_HERE
python3 domain_enum.py google.com
```

### Installation
```bash
git clone https://github.com/dceit/domainenum
cd domainenum
pip install -r requirements.txt
python3 domain_enum.py
```

### Images
![Image of domain enum on Google](https://i.imgur.com/kaFkZ3R.png)

### References
[https://github.com/TheRook/subbrute](https://github.com/TheRook/subbrute)
