#!/usr/bin/env python3
import requests

url = "https://en.wikipedia.org/w/api.php"

params = {
    "action": "query",
    "list": "allpages",
    "aplimit": 10,
    "format": "json"
}

session = requests.Session()

while True:

    response = session.get(url, params=params)
    data = response.json()

    for page in data["query"]["allpages"]:
        page_title = page["title"]

            "action": "query",
            "prop": "contributors",
            "titles": page_title,
            "format": "json"
        }

        contributors_response = session.get(url, params=contributors_params)
        contributors_data = contributors_response.json()

        data_params = {
            "action": "query",
            "prop": "extracts",
            "format": "json",
            "titles": page_title,
            "explaintext": 1,
        }


        data_response = session.get(url, params=data_params)
        data_data = data_response.json()

        pages = contributors_data["query"]["pages"]
        for page_id in pages:
            page = pages[page_id]
            contributors = page["contributors"]
            print(f"Editors for '{page_title}':")
            for contributor in contributors:
                print(contributor["name"])

        pages = data_data["query"]["pages"]
        for page_id in pages:
            page = pages[page_id]
            datas = page["extract"]
            print(f"data for '{page_title}':")
            print(datas)

    check if there are more pages to retrieve
    if "continue" in data:
       params.update(data["continue"])
    else:
       break
