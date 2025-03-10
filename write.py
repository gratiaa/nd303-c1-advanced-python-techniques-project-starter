"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`,
each of which accept an `results` stream of close approaches and a path
to which to write the data.  These functions are invoked by the main
module with the output of the `limit` function and the filename supplied
by the user at the command line. The file's extension determines which
of these functions is used.  You'll edit this file in Part 4.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each
    output row corresponds to the information in a single close approach
    from the `results` stream and its associated near-Earth object.
    :param results: An iterable of `CloseApproach` objects. :param
    filename: A Path-like object pointing to where the data should be
    saved.
    """
    fieldnames = (
        'datetime_utc',
        'distance_au',
        'velocity_km_s',
        'designation',
        'name',
        'diameter_km',
        'potentially_hazardous')

    with open(filename, mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            neo = NearEarthObject(
                result.neo.designation,
                result.neo.name,
                result.neo.diameter,
                result.neo.hazardous).serialize()
            approach = CloseApproach(
                result.neo.designation,
                result.time, result.distance, result.velocity).serialize()

            neo_values = list(neo.values())
            neo_keys = list(neo.keys())
            approach_values = list(approach.values())
            approach_keys = list(approach.keys())

            dict_keys = approach_keys + neo_keys
            dict_values = approach_values + neo_values

            writer.writerow(dict(zip(dict_keys, dict_values)))


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the
    output is a list containing dictionaries, each mapping
    `CloseApproach` attributes to their values and the 'neo' key mapping
    to a dictionary of the associated NEO's attributes.  :param results:
    An iterable of `CloseApproach` objects. :param filename: A Path-like
    object pointing to where the data should be saved.
    """
    with open(filename, mode='w') as file:
        list = []
        for result in results:
            neo = NearEarthObject(
                result.neo.designation,
                result.neo.name,
                result.neo.diameter,
                result.neo.hazardous).serialize()
            approach = CloseApproach(
                result.neo.designation,
                result.time, result.distance, result.velocity).serialize()
            approach['neo'] = neo
            list.append(approach)
        json.dump(list, file)
