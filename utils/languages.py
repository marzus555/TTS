import os
import json

from TTS.datasets.preprocess import get_preprocessor_by_name


def make_languages_json_path(out_path):
    """Returns conventional languages.json location."""
    return os.path.join(out_path, "languages.json")


def load_language_mapping(out_path):
    """Loads language mapping if already present."""
    try:
        with open(make_languages_json_path(out_path)) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_language_mapping(out_path, language_mapping):
    """Saves language mapping if not yet present."""
    languages_json_path = make_languages_json_path(out_path)
    with open(languages_json_path, "w") as f:
        json.dump(language_mapping, f, indent=4)


def get_languages(items):
    """Returns a sorted, unique list of languages in a given dataset."""
    languages = {e[2] for e in items}
    return sorted(languages)
