# Verwende das Snyk Python CLI Docker-Image als Basis
FROM snyk/snyk-cli:python-3.8

# Erstelle das Verzeichnis /project und setze es als Arbeitsverzeichnis
WORKDIR /project

# Kopiere alle Dateien in das Arbeitsverzeichnis
COPY . /project

# Installiere alle Abhängigkeiten
RUN apt-get update && apt-get install -y nodejs npm && \
    npm install -g snyk && \
    python3 -m pip install --upgrade pip && \
    pip install -r python_Calculator/requirements.txt

# Setze das Startkommando
CMD ["bash"]
