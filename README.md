# Netwitness spam email campaign analyzer
A quick first release of an useful script for the identification of spam emails campaigns

## Cases
The classification is based on 4 cases:

- email.src has more than 1 value (len(email.src) > 1)
- email[0] != all(email.src)
- every value in email[1:] is not in email.dst
- len(email.dst) != (len(email)-1)

## Input File
The easiest way is to download all the meta as json. At the moment the input file name is hardcoded, put the file in the same folder and change the name of the file at line 14.

[Download meta as Json](https://community.netwitness.com/t5/netwitness-platform-online/download-data-in-the-events-view/ta-p/669880)

## Output
The script returns a csv file 


