import os
import json


locales = {}


def localizations(dir: str = "locales"):

    global locales
    locales.clear()

    if not os.path.exists(dir):
        print(f"Não achei a pasta {dir} :c")
        return
    
    for root, files in os.walk(dir):

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

    print(f"Achei alguns idiomas, quer ver? {list(locales.keys())}")


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