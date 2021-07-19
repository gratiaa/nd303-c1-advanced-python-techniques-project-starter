"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []
    with open(neo_csv_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            pdes = row["pdes"]
            name = row["name"] if len(row["name"]) > 0 else None
            diameter = float(row["diameter"]) if len(
                row["diameter"]) > 0 else float('nan')
            pha = row["pha"] == 'Y'
            neo = NearEarthObject(pdes, name, diameter, pha)
            neos.append(neo)
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches = []
    with open(cad_json_path, mode='r') as file:
        data = json.load(file)
        content_list = data['data']
        for content in content_list:
            designation = content[0]
            time = content[3]
            distance = float(content[4] if len(content[4]) > 0 else '0')
            velocity = float(content[7] if len(content[7]) > 0 else '0')
            approach = CloseApproach(designation, time, distance, velocity)
            approaches.append(approach)
    return approaches
