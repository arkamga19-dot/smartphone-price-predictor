import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

# Générer 100 smartphones réalistes
marques = ['Apple', 'Samsung', 'Google', 'Xiaomi', 'OnePlus', 'Sony', 'Oppo']
prix_base = {'Apple': 900, 'Samsung': 700, 'Google': 650, 
             'Xiaomi': 400, 'OnePlus': 600, 'Sony': 700, 'Oppo': 500}

data = []
for i in range(100):
    marque = random.choice(marques)
    ram = random.choice([4, 6, 8, 12, 16])
    stockage = random.choice([64, 128, 256, 512])
    batterie = random.randint(3000, 6000)
    camera = random.choice([12, 48, 50, 64, 108, 200])
    ecran = round(random.uniform(5.5, 7.0), 1)
    
    # Prix basé sur les specs
    prix = prix_base[marque]
    prix += ram * 20
    prix += stockage * 0.5
    prix += (batterie - 3000) * 0.05
    prix += camera * 1.5
    prix += random.randint(-50, 50)
    
    data.append([marque, ram, stockage, batterie, camera, ecran, round(prix)])

df = pd.DataFrame(data, columns=['marque', 'ram_gb', 'stockage_gb', 
                                  'batterie_mah', 'camera_mp', 
                                  'ecran_pouces', 'prix_euros'])

df.to_csv('smartphones.csv', index=False)
print(f"Dataset enrichi ✅ - {len(df)} smartphones")
print(df.head())