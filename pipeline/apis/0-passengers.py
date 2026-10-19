#!/usr/bin/env python3
"""Find starships that can hold a number of passengers from SWAPI API"""
import requests


def availableShips(passengerCount):
    """Find starships that can hold a number of passengers from SWAPI API"""
    url = 'https://swapi-api.hbtn.io/api/starships/'
    available_ships = []
    while url:
        data = requests.get(url).json()
        url = data['next']
        starships = data['results']
        for starship in starships:
            passengers = starship['passengers'].replace(",", "")
            if passengers is None or passengers in ['n/a', 'unknown']:
                continue
            if int(passengers) >= passengerCount:
                available_ships.append(starship.get('name'))

    return available_ships
