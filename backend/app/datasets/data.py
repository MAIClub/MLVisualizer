import pandas as pd
import os


def read_csv(file_name):
    data = pd.read_csv("{}/backend/app/datasets/data/{}".format(os.getcwd(), file_name))
    head = data.head(20)
    summary = data.sum()
    return data, head, summary

def load_rice():
    return read_csv("riceClassification.csv")

def load_world_population():
    return read_csv("WorldPopulation.csv")

def load_pokemon():
    return read_csv("pokemon.csv")

def load_water_potability():
    return read_csv("water_potability.csv")

