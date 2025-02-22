# Challenge Data SNCF (SNCF-Transilien) : Prédiction du temps d'attente à quai

## Description du projet
Ce projet vise à prédire le temps d'attente à quai des trains SNCF-Transilien en utilisant des modèles de Machine Learning et des séries temporelles.

## 📂 Structure du projet

```
Challenge-SNCF-Transilien/
│── data/  
│   ├── raw/    
│   │   ├── x_train.csv
│   │   ├── x_test.csv
│   │   ├── y_train.csv
│   │   ├── y_sample.csv
│   ├── processed/      
│── src/ 
│   ├── data_processing.py   
│   ├── train_model.py       
│   ├── predict.py           
│── models/                 
│   ├── best_model.pkl       
│── submissions/              
│   ├── submission.csv
│── .gitignore 
│── README.md  
│── requirements.txt                    
```

## Données
Les données proviennent des arrêts de train en Île-de-France, avec des variables contextuelles et historiques.

## Installation
```bash
pip install -r requirements.txt
```