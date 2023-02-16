import requests
from bs4 import BeautifulSoup
import re

# Url del mayoritas sucursal Neuquén
url = "https://www.vital.com.ar/ofertas/neuquen/"

# Obteniendo el html de la url
response = requests.get(url)

# bs4 para listar el contenido de la página
soup = BeautifulSoup(response.content, "html.parser")

# links en la pagina
links = soup.find_all("a")

# bucle para encontrar pdfs
for link in links:
    # Check si link contiene pdf
    href = link.get("href")
    if href and re.search(".pdf$", href):
        # Construct the URL of the PDF file
        if not href.startswith("https"):
            href = url + href

        # request get para descargar el archivo
        pdf_response = requests.get(href)

        # saving
        filename = href.split("/")[-1]
        with open(filename, "wb") as f:
            f.write(pdf_response.content)
