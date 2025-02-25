# Projet Invest

Bienvenue dans le projet Invest ! Ce projet est une application web construite avec Django, conçue pour gérer les investissements. Ce document vous guidera à travers les étapes nécessaires pour démarrer le projet sur votre machine locale.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Python 3.x
- pip (gestionnaire de paquets Python)
- virtualenv (optionnel mais recommandé pour créer un environnement virtuel)

## Installation

### Cloner le dépôt

Clonez le dépôt sur votre machine locale en utilisant la commande suivante :

```bash
git clone https://github.com/youmasther/invest.git

```

### Créer un environnement virtuel

Il est recommandé de créer un environnement virtuel pour isoler les dépendances du projet. Vous pouvez créer un environnement virtuel en utilisant virtualenv ou tout autre gestionnaire d'environnement virtuel de votre choix.

```bash
cd invest
python -m venv env
```

### Activer l'environnement virtuel

- Sur Windows :

```bash
.\env\Scripts\activate
```

- Sur macOS/Linux :

```bash
source env/bin/activate
```

### Installer les dépendances

Installez les dépendances du projet à partir du fichier requirements.txt :

```bash
pip install -r requirements.txt
```

### Appliquer les migrations

```bash
python invest/manage.py migrate
```
### Créé un super utilisateur

```bash
python invest/manage.py createsuperuser
```

### Démarer le serveur

```bash
python invest/manage.py runserver
```

Vous pouvez maintenant accéder à l'application à l'adresse http://127.0.0.1:8000/.
