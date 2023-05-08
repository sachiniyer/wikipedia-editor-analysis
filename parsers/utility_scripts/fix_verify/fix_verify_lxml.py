import csv
from lxml import etree
import sys
import os
import gc

if len(sys.argv) != 6:
    print("Usage: python xmlparser.py input.7z")
    sys.exit(1)

in_dir = sys.argv[1]
out_dir = sys.argv[2]
temp_dir = sys.argv[3]
error_file = sys.argv[4]
file_name = sys.argv[5]

files = os.listdir(temp_dir)


tags_to_extract = [
    "{http://www.mediawiki.org/xml/export-0.10/}title",
    "{http://www.mediawiki.org/xml/export-0.10/}text",
    "{http://www.mediawiki.org/xml/export-0.10/}username",
    "{http://www.mediawiki.org/xml/export-0.10/}id",
]


os.remove(f"{out_dir}/{file_name}.csv")

with open(f"{out_dir}/{file_name}.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(tags_to_extract)

    for event, elem in etree.iterparse(
        f"{temp_dir}/{file_name}", events=("start", "end")
    ):
        if (
            event == "start"
            and elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}page"
        ):
            csv_file.flush()
            gc.collect()
            page_dict = {k: "" for k in tags_to_extract}
            page_dict["{http://www.mediawiki.org/xml/export-0.10/}username"] = []

        elif (
            event == "end"
            and elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}username"
        ):
            page_dict["{http://www.mediawiki.org/xml/export-0.10/}username"].append(
                elem.text
            )

        elif (
            event == "end"
            and elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}id"
        ):
            if page_dict["{http://www.mediawiki.org/xml/export-0.10/}id"] == "":
                page_dict["{http://www.mediawiki.org/xml/export-0.10/}id"] = elem.text

        elif event == "end" and elem.tag in tags_to_extract:
            page_dict[elem.tag] = elem.text

        elif (
            event == "end"
            and elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}page"
        ):
            writer.writerow([page_dict[tag] for tag in tags_to_extract])

            csv_file.flush()
            page_dict.clear()
            gc.collect()
