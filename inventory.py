import requests
from xml.etree import ElementTree
import xmltodict
import json

def main():
    url = "https://www.re3data.org/api/beta/repositories?query=&countries%5B%5D=CAN"
    response = requests.get(url)
    repositories_list = ElementTree.fromstring(response.content)

    repositories = []
    count = 1
    for repository in list(repositories_list):
        response = requests.get(repository.find("link").get("href"))
        o = xmltodict.parse(response.content)
        repository_metadata = o["r3d:re3data"]["r3d:repository"]
        repositories.append(repository_metadata)
        print("Repository {} of {}: {}".format(count, len(list(repositories_list)), repository_metadata["r3d:repositoryName"]["#text"]))
        count += 1
    with open("repositories.json", 'w') as f:
        f.write(json.dumps(repositories))

if __name__ == "__main__":
    main()