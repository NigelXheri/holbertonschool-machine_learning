#!/usr/bin/env python3
"""Prints the location of a specific user from SWAPI API"""
import argparse
import requests
import time

if __name__ == "__main__":
    """Prints the location of a specific user from SWAPI API"""

    parser = argparse.ArgumentParser(prog="user_location.py")
    parser.add_argument('url')
    args = parser.parse_args()
    user = args.url

    response = requests.get(user)
    status_code = response.status_code
    data = response.json()
    if status_code == 404:
        print('Not found')
        exit(1)
    if status_code == 403:
        print('Reset in {:.0f} min'
              .format((int(response.headers['x-ratelimit-reset'])
                       - time.time())/60))
        exit(1)
    print(data['location'])
