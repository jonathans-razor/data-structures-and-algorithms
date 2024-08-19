import json
import argparse

def create_jsonld():
    jsonld_document = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "John Doe",
        "jobTitle": "Software Engineer",
        "telephone": "(123) 456-7890",
        "url": "http://www.johndoe.com"
    }
    return jsonld_document

def main():
    parser = argparse.ArgumentParser(description='Create and print a JSON-LD document.')
    args = parser.parse_args()

    jsonld_document = create_jsonld()
    print(json.dumps(jsonld_document, indent=4))

if __name__ == "__main__":
    main()