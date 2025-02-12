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
│   ├── processed/      
│── src/                      # Code source du projet
│   ├── data_processing.py    # Scripts pour charger et transformer les données
│   ├── train_model.py        # Script pour entraîner le modèle
│   ├── predict.py            # Script pour générer des prédictions
│── models/                   # Modèles entraînés (optionnel)
│   ├── best_model.pkl        # Sauvegarde du modèle entraîné
│── submissions/              # Fichiers de soumission
│   ├── submission.csv
│── requirements.txt          # Liste des packages Python nécessaires
│── environment.yml           # Configuration de l’environnement conda (optionnel)
│── README.md                 # Documentation principale du projet
│── LICENSE                   # Licence du projet
│── .gitignore                # Fichiers à ignorer par Git
```

## 📊 Données
Les données proviennent des arrêts de train en Île-de-France, avec des variables contextuelles et historiques.

## ⚙️ Installation
```bash
pip install -r requirements.txt
```