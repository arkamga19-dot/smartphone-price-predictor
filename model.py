import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import LabelEncoder

# Charger les données
df = pd.read_csv('smartphones.csv')
print("Données chargées ✅")
print(df.head())

# Encoder la colonne 'marque'
le = LabelEncoder()
df['marque_encoded'] = le.fit_transform(df['marque'])

# Features et cible
X = df[['marque_encoded', 'ram_gb', 'stockage_gb', 
        'batterie_mah', 'camera_mp', 'ecran_pouces']]
y = df['prix_euros']

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Modèle Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

# Résultats
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"\nR² Score : {r2:.4f}")
print(f"RMSE     : {rmse:.2f} €")

# Visualisation
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, color='blue', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], 
         [y_test.min(), y_test.max()], 'r--')
plt.title('Prédictions vs Prix réels')
plt.xlabel('Prix réel (€)')
plt.ylabel('Prix prédit (€)')
plt.grid(True)
plt.savefig('resultats.png')
plt.show()
print("Graphique sauvegardé ✅")