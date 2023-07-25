"""
    Crudo... pero hace su trabajo
"""

with open("config.txt", "r") as f:
    total_results_line = f.readline()
    default_article_line = f.readline()
    total_results = int(total_results_line.split()[2])
    default_article = default_article_line.split()[2]
    f.close
