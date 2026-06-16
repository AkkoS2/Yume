from collections import defaultdict
import os
import json


locales = defaultdict(dict)


def localizations(dir: str = "locales"):

    global locales
    locales.clear()

    if not os.path.exists(dir):
        print(f"Não achei a pasta {dir} :c")

        return

    for root, dirs, files in os.walk(dir):

        for filename in files:

            if not filename.endswith(".json"):
                continue

            filepath = os.path.join(root, filename)
            otherpath = os.path.relpath(filepath, dir)
            parts = otherpath.split(os.sep)

            lang = parts[0]
            category = filename.replace(".json", "")
            langs = how_to_load_a_json_101(filepath)

            if langs:
                locales[lang][category] = langs
                    

    print(f"Achei alguns idiomas, quer ver? {list(locales.keys())}")


# Deixar menos aninhado isso aqui depois, ficou feinho :c
# Talvez tem que dividir essa coisinha aqui, ou deixae tudo em uma def grandona
def get_language(lang: str, category: str, key: str, personality: str = None) -> str:

    try:

        if lang not in locales:
            lang = "en"

        data = locales[lang].get(category, {})

        if personality and key in data and personality in data[key]:
            return data[key][personality]

        return data.get(key, f"Cadê meus textos? :c \n {category}.{key}")

    except Exception:
        return f"Deu um erro aqui: {category}.{key} :c"
    

def how_to_load_a_json_101(filepath):

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    
    except Exception as e:

        print(f"Não consegui carregar {filepath}: {e}. faz alguma coisa!! :c")
        return None
    