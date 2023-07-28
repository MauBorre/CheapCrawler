import requests
import bs4
from output_cleaner import clean_it
from url_generator import url_generator
from config_parser import total_results, default_article

import sys


"""
    Funcionaba como main() del proyecto.
    
    Run crawler.py "your article without quotes"

    Mauro Borré
"""

# ejecucion desde shell...
if len(sys.argv) > 1:
    ARTICULO = ' '.join(sys.argv[1:])
else:
    # Default
    ARTICULO = default_article


def scrapePrice(amount, article):

    ARTICULO = article
    URL = url_generator(ARTICULO)
    
    mercado_libre_class_price_tag = "andes-money-amount ui-search-price__part shops__price-part ui-search-price__part--medium andes-money-amount--cents-superscript"
    mercado_libre_class_link_tag = "ui-search-item__group__element shops__items-group-details ui-search-link"
    r = requests.get(URL)
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
            if count < int(amount): 
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

def run_crawler(amt, item):

    return scrapePrice(amt, item)


if __name__ == '__main__':
    scrapePrice(total_results, default_article)

"""
    TODO 
    Flexibilizar url_generator y output_cleaner en favor de otros e-commerce
    Extender los parametros de configuracion (personalizacion de la oferta buscada, periocidad de la busqueda, etc)
    GUI y System tray + desktop toast notifications (windows)


"""
