import pandas as pd
import os

def load_rice():
    Rice = pd.read_csv(os.getcwd()+"/backend/app/datasets/data/riceClassification.csv")
    head = Rice.head(20)
    summary = Rice.sum()
    return Rice, head, summary

def load_world_population():
    WorldPopulation = pd.read_csv(os.getcwd()+"/backend/app/datasets/data/WorldPopulation.csv")
    head = WorldPopulation.head(20)
    summary = WorldPopulation.sum()
    return WorldPopulation, head, summary

def load_pokemon():
    Pokemon = pd.read_csv(os.getcwd()+"/backend/app/datasets/data/pokemon.csv")
    head = Pokemon.head(20)
    summary = Pokemon.sum()
    return Pokemon, head, summary

def load_water_potability():
    WaterPotability = pd.read_csv(os.getcwd()+"/backend/app/datasets/data/water_potability.csv")
    head = WaterPotability.head(20)
    summary = WaterPotability.sum()
    return WaterPotability, head, summary