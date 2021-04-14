""" Script containing the functions to perform the required analyses """

import pandas as pd
import json
from collections import Counter


def num_vaccinated_by_age(data_dir, output_dir):
    """
    Compute the number of vaccinated people divided by age range.
    :param data_dir: path to the directory containing the data
    :param output_dir: path to the directory containing the output files
    :return: json file --> {age_range: {dose1: number, dose2: number}}
    """
    data_dir = data_dir if data_dir[-1] == '/' else data_dir + '/'
    output_dir = output_dir if output_dir[-1] == '/' else output_dir + '/'
    csv_name = "anagrafica-vaccini-summary-latest.csv"
    df_age_ranges = pd.read_csv(data_dir + csv_name)
    out_dict = {}
    for i in range(len(df_age_ranges)):
        key = df_age_ranges['fascia_anagrafica'][i]
        value = {"dose1": int(df_age_ranges['prima_dose'][i]), "dose2": int(df_age_ranges['seconda_dose'][i])}
        out_dict[key] = value
    with open(output_dir + "num_vaccinated_by_age.json", "w") as outfile:
        json.dump(out_dict, outfile, indent='\t')


def num_administrations_per_category(data_dir, output_dir):
    """
    Compute the number of administrations performed per each category.
    :param data_dir: path to the directory containing the data
    :param output_dir: path to the directory containing the output files
    :return: json file --> {age_range: {dose1: number, dose2: number}}
    """
    data_dir = data_dir if data_dir[-1] == '/' else data_dir + '/'
    output_dir = output_dir if output_dir[-1] == '/' else output_dir + '/'
    csv_name = "somministrazioni-vaccini-summary-latest.csv"
    df_categories = pd.read_csv(data_dir + csv_name)
    out_dict = Counter()
    keys = ["categoria_operatori_sanitari_sociosanitari", "categoria_personale_non_sanitario", "categoria_ospiti_rsa",
            "categoria_over80", "categoria_forze_armate", "categoria_personale_scolastico", "categoria_altro"]
    for i in range(len(df_categories)):
        for k in keys:
            out_dict[k] += int(df_categories[k][i])
    with open(output_dir + "num_administrations_per_category.json", "w") as outfile:
        json.dump(out_dict, outfile, indent='\t')
