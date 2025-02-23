# Challenge Data (SNCF-Transilien) : Prédiction du temps d'attente à quai

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
│   │   └── y_sample.csv   
│── src/ 
│   ├── data_processing.py
│   ├── main.py
│   ├── metrics_and_plots.py
│   ├── train_model.py       
│   ├── predict.py 
│   └── train_model.py             
│── submissions/              
│   └──  submission.csv
│── .gitignore 
│── README.md  
└── requirements.txt                    
```

## Données
Les données proviennent des arrêts de train en Île-de-France, avec des variables contextuelles et historiques.

## Installation
```bash
git clone https://github.com/Moussa-Kalla/Challenge-Data-SNCF
```

```bash
pip install -r requirements.txt
```
```bash
python src/main.py
```
