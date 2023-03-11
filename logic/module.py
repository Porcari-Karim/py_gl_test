import importlib

imported_modules = {}

def get_module(module_name: str):

    result = imported_modules.get(module_name, None)
    if result is None:
        result = importlib.import_module(module_name, "")
        imported_modules[module_name] = result
    return result
