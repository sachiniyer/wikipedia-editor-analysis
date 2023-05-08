import csv
import xml.etree.ElementTree as ET
import sys
import os

if len(sys.argv) != 5:
    print("Usage: python xmlparser.py input.7z")
    sys.exit(1)

file_name = sys.argv[1]
in_dir = sys.argv[2]
out_dir = sys.argv[3]
temp_dir = sys.argv[4]

if os.path.isfile(f"{temp_dir}/{file_name}") or os.path.isfile(
    f"{out_dir}/{file_name}.csv"
):
    print("file already exists")
    sys.exit()

os.system(f"/scratch/si2073/7z -y x {in_dir}/{file_name}.7z -o{temp_dir}")

tags_to_extract = [
    "{http://www.mediawiki.org/xml/export-0.10/}title",
    "{http://www.mediawiki.org/xml/export-0.10/}text",
    "{http://www.mediawiki.org/xml/export-0.10/}username",
    "{http://www.mediawiki.org/xml/export-0.10/}id",
]

with open(f"{out_dir}/{file_name}.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(tags_to_extract)

    for event, elem in ET.iterparse(f"{temp_dir}/{file_name}", events=("start", "end")):
        if (
            event == "start"
            and elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}page"
        ):
            page_dict = {
                "{http://www.mediawiki.org/xml/export-0.10/}title": "",
                "{http://www.mediawiki.org/xml/export-0.10/}text": "",
                "{http://www.mediawiki.org/xml/export-0.10/}id": "",
                "{http://www.mediawiki.org/xml/export-0.10/}username": [],
                "{http://www.mediawiki.org/xml/export-0.10/}ip": [],
            }
        elif (
            event == "end"
            and elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}id"
        ):
            if page_dict["{http://www.mediawiki.org/xml/export-0.10/}id"] == "":
                page_dict["{http://www.mediawiki.org/xml/export-0.10/}id"] = elem.text

        elif (
            event == "end"
            and elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}title"
        ):
            page_dict["{http://www.mediawiki.org/xml/export-0.10/}title"] = elem.text

        elif (
            event == "end"
            and elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}text"
        ):
            page_dict["{http://www.mediawiki.org/xml/export-0.10/}text"] = elem.text

        elif (
            event == "end"
            and elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}username"
        ):
            page_dict["{http://www.mediawiki.org/xml/export-0.10/}username"].append(
                elem.text
            )

        elif (
            event == "end"
            and elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}page"
        ):
            # print(page_dict)
            writer.writerow([page_dict.get(tag, "") for tag in tags_to_extract])
            csv_file.flush()

            page_dict.clear()

            elem.clear()

os.remove(f"{temp_dir}/{file_name}")
