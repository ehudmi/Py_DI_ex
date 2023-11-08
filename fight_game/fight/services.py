import requests
import json
import re
from random import randint

# load API key from config file
with open("config/_env_var.json") as file:
    data = json.load(file)
API_KEY = data["MY_API_KEY"]

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
        "X-RapidAPI-Key": API_KEY,
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
    url = "https://bing-image-search1.p.rapidapi.com/images/search"
    querystring = {"q": name}
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "bing-image-search1.p.rapidapi.com",
    }
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
