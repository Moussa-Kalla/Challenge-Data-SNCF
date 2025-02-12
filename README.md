# Challenge Data SNCF (SNCF-Transilien) : Prédiction du temps d'attente à quai

## 📌 Description du projet
Ce projet vise à prédire le temps d'attente à quai des trains SNCF-Transilien en utilisant des modèles de Machine Learning et des séries temporelles.

## 📂 Structure du projet

```
Challenge-SNCF-Transilien/
│── data/                    # Dossier pour les jeux de données
│   ├── raw/                 # Données brutes (non modifiées)
│   │   ├── x_train.csv
│   │   ├── x_test.csv
│   │   ├── y_train.csv
│   │   ├── y_sample.csv
│   ├── processed/            # Données après prétraitement
│── notebooks/                # Jupyter Notebooks pour l'exploration et le modèle
│── src/                      # Code source du projet
│── models/                   # Modèles entraînés
│── submissions/              # Fichiers de soumission
│── requirements.txt          # Liste des packages Python nécessaires
│── README.md                 # Documentation principale du projet
│── .gitignore                # Fichiers à ignorer par Git
```

## 📊 Données
Les données proviennent des arrêts de train en Île-de-France, avec des variables contextuelles et historiques.

## ⚙️ Installation
```bash
pip install -r requirements.txt
```