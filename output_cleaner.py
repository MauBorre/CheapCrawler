import re

"""
    Necesario para limpiar el texto que exhibe el tag correspondiente al precio
    usando mercado libre.
    Solo implementado temporalmente para obtener resultados limpios del MVP
"""

def clean_it(text):
    magic_char = "$"
    for count, letters in enumerate(text):
        if letters == magic_char:
            return text[count:]
        
