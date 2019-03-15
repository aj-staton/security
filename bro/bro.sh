#!/bin/bash

bro -r *.pcap

# Searching for the networks main DNS server....
cat dns.log | bro-cut query | uniq -c > dns.txt

# Looking for frequented external addresses....
cat conn.log | bro-cut id.resp_h | sort | uniq -c | sort -n > ext.txt

# Finidng the most common app-layer protocol...
#   The 'sort | uniq -c | sort -n' in the cut allows me to remove duplicates.
cat conn.log | bro-cur proto | sort | uniq -c | sort -n > applayer.txt

