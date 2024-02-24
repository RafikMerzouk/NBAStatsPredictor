# Utilisez une image Jupyter de base
FROM jupyter/datascience-notebook

# Définissez le répertoire de travail
WORKDIR /mnt

# Copiez tous les fichiers dans le conteneur
COPY ./ /mnt

# Installez les dépendances supplémentaires
RUN pip install -r requirements.txt

# Exposez le port pour Jupyter Notebook
EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token='GPEUR'", "--NotebookApp.password=''"]