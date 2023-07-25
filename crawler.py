import requests
import bs4
from output_cleaner import clean_it
from url_generator import url_generator
import sys
from config_parser import total_results, default_article

"""
    Funciona como main() del proyecto.
    El programa buscara coincidencias en la web bajo parametros especificos, tales como articulo y longitud de lista a mostrar.
    El chiste es que se haga automaticamente en segundo plano y pueda mostrar notificaciones en el escritorio.
    La cantidad de elementos generados es configurable desde config.txt.
    Work in progress...
    Mauro Borré
"""

# Run crawler.py "your_article_without_quotes"
if len(sys.argv) > 1:
    ARTICULO = ' '.join(sys.argv[1:])
else:
    # Default
    ARTICULO = default_article

URL = url_generator(ARTICULO)

def scrapePrice(url):
    mercado_libre_class_price_tag = "andes-money-amount ui-search-price__part shops__price-part ui-search-price__part--medium andes-money-amount--cents-superscript"
    mercado_libre_class_link_tag = "ui-search-item__group__element shops__items-group-details ui-search-link"
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')

    # Filters
    my_prices = soup.find_all('span', {'class' : mercado_libre_class_price_tag})
    my_location = soup.find_all('a', {'class' : mercado_libre_class_link_tag})

    """ 
        el output deberia ser un JSON para facilitar la 
        extension de su funcionalidad a otros modulos
    """
    with open("output.txt", "w") as outfile:
        outfile.write(f"Se ha revisado la URL: {URL}")
        outfile.write("\n");outfile.write("\n")
        outfile.write(f"En busqueda del articulo: {ARTICULO}")
        outfile.write("\n");outfile.write("\n")

        for count, linea in enumerate(my_prices):
            if count < total_results: 
                outfile.write("Articulo Nro "+str(count+1)+": ")
                #outfile.write("$"+linea.get_text())
                # Si no se usa clean_it el precio no sale bien...
                outfile.write(str(clean_it(linea.get_text())))
                outfile.write("\n")
                outfile.write("Ubicacion: " + str(my_location[count]['href']))
                outfile.write("\n")
                outfile.write("\n")
        outfile.close()
    return

scrapePrice(URL)

"""
    TODO 
    Flexibilizar url_generator y output_cleaner en favor de otros e-commerce
    Extender los parametros de configuracion (personalizacion de la oferta buscada, periocidad de la busqueda, etc)
    GUI y System tray + desktop toast notifications (windows)


"""
