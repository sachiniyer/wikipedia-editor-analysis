#!/usr/bin/env python3
import requests

# set up the API endpoint URL
url = "https://en.wikipedia.org/w/api.php"

# set the parameters for the API request
params = {
    "action": "query",
    "list": "allpages",
    "aplimit": 10,  # number of pages to retrieve in each API call
    "format": "json"
}

# set up a session object to handle cookies and headers
session = requests.Session()

# loop over each batch of pages and get the list of contributors for each page
while True:
    # make the API request and get the response data as JSON
    response = session.get(url, params=params)
    data = response.json()

    # loop over each page and get the contributors
    for page in data["query"]["allpages"]:
        page_title = page["title"]

        # set the parameters for the contributors API request
        contributors_params = {
            "action": "query",
            "prop": "contributors",
            "titles": page_title,
            "format": "json"
        }

        # make the API request and get the response data as JSON
        contributors_response = session.get(url, params=contributors_params)
        contributors_data = contributors_response.json()

        # set the parameters for the data API request

        data_params = {
            "action": "query",
            "prop": "extracts",
            "format": "json",
            "titles": page_title,
            "explaintext": 1,
        }


        data_response = session.get(url, params=data_params)
        data_data = data_response.json()
        print(data_data)
        # extract the contributor information and print it to the console
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
