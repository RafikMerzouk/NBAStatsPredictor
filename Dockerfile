# Utilisation d'une image de base Python
FROM python:3.10-slim

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers nécessaires
COPY . .

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande pour exécuter l'application
CMD ["python", "app.py"]
