# json.dump e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# # Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null
import json
from pprint import pprint
from typing import TypedDict

class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imbd_rating: float
    year: int
    characters: list[str]
    budget: None | float


string_json = """
{
    "title": "O Senhor dos Aneis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings; The Fellowship of the Ring",
    "is_movie": true,
    "imbd_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "legolas", "Boromir"],
    "budget": null
}
"""
filme: Movie = json.loads(string_json)
json_string = json.dumps(filme, ensure_ascii=False, indent=4)
# pprint(filme)
# print(filme['year'] + 10)
pprint(json_string)
