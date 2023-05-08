import csv
import xml.etree.ElementTree as ET
import sys
import os

if len(sys.argv) != 5:
    print("Usage: python xmlparser.py input.7z")
    sys.exit(1)
    
in_dir = sys.argv[1]
out_dir = sys.argv[2]
temp_dir = sys.argv[3]
error_file = sys.argv[4]

files = os.listdir(temp_dir)

tags_to_extract = ['{http://www.mediawiki.org/xml/export-0.10/}title', 
                   '{http://www.mediawiki.org/xml/export-0.10/}text',
                   '{http://www.mediawiki.org/xml/export-0.10/}username',
                   '{http://www.mediawiki.org/xml/export-0.10/}id']

for file_name in files:
    print(file_name)
    print(f'/scratch/si2073/7z -y x {in_dir}/{file_name}.7z -o{temp_dir}')

