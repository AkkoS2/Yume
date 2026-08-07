import os
import json
import random


locales = {}

def localizations(dir_path: str = "locales"):
    global locales
    locales.clear()

    if not os.path.exists(dir_path):
        print(f"Não achei a pasta {dir_path} :c")
        return

    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            if not filename.endswith(".json"):
                continue

            filepath = os.path.join(root, filename)
            
            otherpath = os.path.relpath(filepath, dir_path)
            parts = otherpath.split(os.sep)

            if len(parts) >= 3:
                lang = parts[0]
                folder = parts[1]
                category = filename.replace(".json", "")
                
                data = how_to_load_a_json_101(filepath)

                if data:
                    if lang not in locales:
                        locales[lang] = {}
                    if folder not in locales[lang]:
                        locales[lang][folder] = {}
                    
                    locales[lang][folder][category] = data
                    
    print(f"Achei algumas coisinhas: {list(locales.keys())}")


def get_language(lang: str, category: str, key: str, personality: str = None) -> str:
    if lang not in locales:
        lang = "en"

    try:
        if personality:
            data = locales[lang].get("personalities", {}).get(personality, {})
        else:
            data = locales[lang].get("commands", {}).get(category, {})


        resultado = data.get(key)

        if resultado:
            if isinstance(resultado, list):

                opcoes_validas = [frase for frase in resultado if frase.strip()]
                return random.choice(opcoes_validas) if opcoes_validas else "Faltou texto aqui! :c"
            
            return resultado

        return f"Cadê meus textos? :c \n {key}"

    except Exception as e:
        return f"Deu um erro aqui: {key} :c ({e})"
    

def how_to_load_a_json_101(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Não consegui carregar {filepath}: {e}. faz alguma coisa!! :c")
        return None