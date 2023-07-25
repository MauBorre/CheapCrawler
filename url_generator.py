"""
    Este generador deberia servir para multiples sitios, pero por ahora
    solo generaremos URLS para mercado libre

    el formato utilizado por mercado libre es:
    "https.../mi-articulo#D[A:mi%20articulo]

"""
def querify(keyword):
    """
    mi articulo nuevo -> mi%20articulo%20nuevo
    """
    append_str = '%20'
    splitted = keyword.split() # para separar la oracion en elementos separados de una lista
    prefix = [append_str + word for word in splitted]
    clean = ''.join(prefix)
    return clean[3:]



def url_generator(keyword):
    BASE = "https://listado.mercadolibre.com.ar/"
    if len(keyword.split()) == 1:
        return BASE + keyword + '#D[A:' + keyword + ']'
    else:
        return BASE + keyword.replace(" ", "-") + '#D[A:' + querify(keyword) + ']'
         
# print(url_generator('mi articulo nuevo'))

