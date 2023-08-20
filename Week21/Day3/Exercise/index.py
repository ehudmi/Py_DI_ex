import json

json_file = "C:/Github/Python_Bootcamp/Py_DI_ex/Week21/Day3/Exercise/file.json"
with open(json_file, "r") as file_obj:
    family = json.load(file_obj)
for key, value in family.items():
    if key == "children":
        for item in value:
            for k, v in item.items():
                print(f"the {k} is {v}")
for item in family["children"]:
    item.update({"favorite_color": "blue"})
# print(family["children"])

with open(json_file, "w") as file_obj:
    json.dump(family, file_obj, indent=2, sort_keys=True)
