"""
    Funcion de utilidad para escribir el archivo config.txt desde la interfaz grafica.
    total_results = ...
    default_article = ...
"""

def write_to_conf(amount, item):
    with open("config.txt", "w") as f:
        total_results_line = f.write(f"total_results = {amount}")
        f.write("\n")
        default_article_line = f.write(f"default_article = {item}")
        f.close