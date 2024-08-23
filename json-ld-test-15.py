import requests
import json
from pyld import jsonld
from pprint import pprint

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)
    print("Fetched users data:")
    pprint(response.json())  # Pretty-printing fetched data
    return response.json()

def compact_jsonld(data):
    context = {
        "@context": {
            "name": "http://schema.org/name",
            "username": "http://schema.org/alternateName",
            "email": "http://schema.org/email",
            "address": "http://schema.org/address",
            "street": "http://schema.org/streetAddress",
            "suite": "http://schema.org/suite",
            "city": "http://schema.org/addressLocality",
            "zipcode": "http://schema.org/postalCode",
            "geo": "http://schema.org/geo",
            "lat": "http://schema.org/latitude",
            "lng": "http://schema.org/longitude",
            "phone": "http://schema.org/telephone",
            "website": "http://schema.org/url",
            "company": "http://schema.org/organization",
            "companyName": "http://schema.org/name",
            "catchPhrase": "http://schema.org/description",
            "bs": "http://schema.org/keywords"
        }
    }
    compacted = jsonld.compact({"@graph": data}, context)
    print("Compacted JSON-LD data:")
    pprint(compacted)  # Pretty-printing compacted data
    return compacted

def main():
    users = fetch_users()
    compacted_users = compact_jsonld(users)
    print(json.dumps(compacted_users, indent=2))

if __name__ == "__main__":
    main()
