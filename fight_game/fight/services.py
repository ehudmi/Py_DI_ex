import requests
import re
from random import randint
from environ import Env

# load API key from environment variable
env = Env()
RAPID_API_KEY = env("RAPID_API_KEY")
BING_API_KEY = env("BING_API_KEY")

SUBSTITUTIONS = {
    ", ": " ",
    ", and ": " ",
    " and ": " ",
    " to the ": " ",
    " of the ": " ",
    " in the ": " ",
    " the ": " ",
    " to ": " ",
    " of ": " ",
    " in ": " ",
    "   ": " ",
    "  ": " ",
}


# function to replace substrings in a string
def replace(string, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile("|".join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], string)


# function to get data from the Historical Figures API
def get_API_figure(request, value, offset):
    url = "https://historical-figures-by-api-ninjas.p.rapidapi.com/v1/historicalfigures"
    querystring = {"name": value, "offset": offset}
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "historical-figures-by-api-ninjas.p.rapidapi.com",
    }
    response = requests.get(url, headers=headers, params=querystring)
    figure_json = response.json()
    figure_list = []
    for figure in figure_json:
        name = figure["name"]
        title_occupation = replace(figure["title"], SUBSTITUTIONS)
        occupation = None
        # if the figure has an occupation, split it into a list of strings
        if figure["info"].get("occupations", "") != "":
            occupation = figure["info"].get("occupations")
            if type(occupation) == list:
                for i in range(len(occupation)):
                    occupation[i] = occupation[i].lower()
            else:
                if occupation.find(",") != -1:
                    occupation = occupation.lower().split(", ")
                else:
                    occupation = occupation.lower().split(" ")
        # if the figure has no occupation, try to get one from the name
        if figure["info"].get("occupations", "") == "" and name.find("(") != -1:
            name_occupation = (
                name[name.find("(") + 1 : name.find(")")].lower().split(" ")
            )
            occupation = name_occupation
        # if the figure has no occupation and no occupation in the name, try to get one from the title
        if figure["info"].get("occupations", "") == "" and name.find("(") == -1:
            occupation = title_occupation.split(" ")[1:9]
            for i in range(len(occupation)):
                occupation[i] = occupation[i].lower()
        figure_list.append(
            {
                "name": figure["name"],
                "title": figure["title"],
                "occupation": occupation,
            }
        )
    return figure_list


# function to get data from the Bing Image Search API
def get_API_image(request, name):
    url = "https://api.bing.microsoft.com/v7.0/images/search"
    querystring = {"q": name}
    headers = {"Ocp-Apim-Subscription-Key": BING_API_KEY}
    response = requests.get(url, headers=headers, params=querystring)
    image_json = response.json()
    image_list = []
    for image in image_json["value"]:
        image_list.append(
            {
                "id": image["imageId"],
                "name": image["name"],
                "image_url": image["contentUrl"],
            }
        )
    return image_list


# function to get data from the Wikipedia API
def get_API_WIKI_info(request, name):
    url = "https://en.wikipedia.org/w/api.php"
    querystring = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": "",
        "explaintext": "",
        "redirects": 1,
        "titles": name,
    }
    response = requests.get(url, params=querystring)
    wiki_json = response.json()
    wiki_list = []
    for page in wiki_json["query"]["pages"]:
        wiki_list.append(
            {
                "title": wiki_json["query"]["pages"][page]["title"],
                "extract": wiki_json["query"]["pages"][page]["extract"],
            }
        )
    return wiki_list[0]["extract"]


# function to calculate the score for a figure
def calc_score(notoriety, luck):
    score = 0
    intelligence = randint(1, 6)
    strength = randint(1, 6)
    if notoriety > 6:
        score += notoriety
    else:
        score += notoriety * 2
    if luck > 6:
        score += luck
    else:
        score += luck * 2
    score += intelligence
    score += strength
    score_dict = {
        "notoriety": notoriety,
        "luck": luck,
        "intelligence": intelligence,
        "strength": strength,
        "score": score,
    }
    return score_dict
