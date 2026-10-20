#!/usr/bin/env python3
"""Returns the list of names of the home planets of all sentient species
    from SWAPI API"""
import requests


def sentientPlanets():
    """Returns the list of names of the home planets of all sentient species
        from SWAPI API"""
    base_url = 'https://swapi-api.hbtn.io/api/'
    url = base_url + 'species/'
    while url:
        data = requests.get(url).json()
        species = data['results']
        sentient_planets = []
        for specie in species:
            if (specie['classification'] == 'sentient'
                    or specie['designation'] == 'sentient'):
                homeworld_url = specie['homeworld']
                if homeworld_url is None:
                    continue
                homeworld_data = requests.get(homeworld_url).json()
                if homeworld_data['name'] in [None, 'unknown']:
                    continue
                sentient_planets.append(homeworld_data['name'])

        url = data['next']

    return sentient_planets
