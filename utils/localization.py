# Bibliotecas
import os
import json


locales = {}


def load(dir: str = "locales"):

    global locales
    locales.clear()

    if not os.path.exists(dir):
        print(f"Não achei a pasta {dir} :c")
        return
    
    for root, dirs, files in os.walk(dir):

        for filename in files:

            if filename.endswith(".json"):
                filepath = os.path.join(root, filename)

                otherpath = os.path.relpath(filepath, dir)
                parts = otherpath.split(os.sep)

                lang = parts[0]
                category = filename.replace(".json", "")


                if lang not in locales:
                    locales[lang] = {}

                try:

                    with open(filepath, "r", encoding="utf-8") as f:
                        locales[lang][category] = json.load(f)
                
                except Exception as e:
                    print(f"Não consegui carregar {filepath}: {e}. faz alguma coisa!! :c")

    print(f"Idiomas Carregados: {list(locales.keys())}")