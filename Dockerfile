# Verwende das Snyk Python CLI Docker-Image als Basis
FROM snyk/snyk-cli:python-3.8

# Erstelle das Verzeichnis /project und setze es als Arbeitsverzeichnis
WORKDIR /project

# Kopiere alle Dateien in das Arbeitsverzeichnis
COPY . /project

# Installiere nvm, Node.js und npm, und setze Pfade richtig
RUN apt-get update && apt-get install -y curl && \
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash && \
    . ~/.nvm/nvm.sh && \
    nvm install 14 && \
    nvm use 14 && \
    nvm alias default 14 && \
    npm install -g snyk

# Installiere Python-Abhängigkeiten
RUN python3 -m pip install --upgrade pip && \
    pip install -r python_Calculator/requirements.txt

# Setze das Startkommando
CMD ["bash"]
