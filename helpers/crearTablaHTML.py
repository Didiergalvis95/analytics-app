import pandas as pd
from bs4 import BeautifulSoup

def crearTabla(dataFrame, nombreTabla):
    archivoHTML = dataFrame.to_html()
    
    ruta=f"tables/{nombreTabla}.html"
    
    encabezadoHTML='''
        <!DOCTYPE html>
        <html>
            <head>
                <title>Tablas</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            </head>
        </html>
    '''    
    sopa=BeautifulSoup(archivoHTML, 'html.parser')    
    for tr in sopa.find_all('tr'):
        tr.attrs.pop('style',None)
        
    archivoHTML=str(sopa)
    archivoHTML=archivoHTML.replace('<table border="1" class="dataframe">', '<table class="table table-stripe">')
    
    with open(ruta,"w") as archivo:
        archivo.write(f"{encabezadoHTML}\n{archivoHTML}\n</body>\n</html>")