""" Script containing the functions to perform the required analyses """

import pandas as pd
import json


def num_vaccinated_by_age(data_dir, output_dir):
    """
    Compute the number of vaccinated people divided by age range.
    :param data_dir: path to the directory containing the data
    :param output_dir: path to the directory containing the output files
    :return: json file --> {age_range: {dose1: number, dose2: number}}
    """
    data_dir = data_dir if data_dir[-1] == '/' else data_dir + '/'
    output_dir = output_dir if output_dir[-1] == '/' else output_dir + '/'
    csv_age_ranges = "anagrafica-vaccini-summary-latest.csv"
    df_age_ranges = pd.read_csv(data_dir + csv_age_ranges)
    out_dict = {}
    for i in range(len(df_age_ranges)):
        key = df_age_ranges['fascia_anagrafica'][i]
        value = {"dose1": int(df_age_ranges['prima_dose'][i]), "dose2": int(df_age_ranges['seconda_dose'][i])}
        out_dict[key] = value
    with open(output_dir + "num_vaccinated_by_age.json", "w") as outfile:
        json.dump(out_dict, outfile, indent='\t')
