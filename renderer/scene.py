from OpenGL.GL import *
from .mesh import Mesh
from logic.entity import Entity
from logic.module import get_module
import yaml
import colorama
from test import get_obj_vertices

class Scene:

    def __init__(self, entities: list[Entity]) -> None:
        self.entities = entities

def Load_Scene(sceneYmlFile: str):
    result = Scene([])
    with open(sceneYmlFile) as f:
        parsed_file = yaml.safe_load(f)
    for entity in parsed_file["entities"]:
        name = list(entity.keys())[0]
        entity = entity[name]
        vertices = entity["vertices"]
        vertices, indices = get_obj_vertices(vertices)
        temp_entity = Entity(Mesh(vertices, vertices, []))
        #print(indices) #TO DO !
        temp_entity.position = entity["position"]
        temp_entity.rotation = entity["rotation"]
        try:
            script_package = get_module(entity["script"])
            temp_entity.script = script_package.update
            script_package.init(temp_entity)
        except Exception as e:
            print(e)
            temp_entity.script = None
        result.entities.append(temp_entity)
        # print(colorama.Fore.GREEN)
        # print(f"Loaded entity ", end="")
        # print(colorama.Fore.WHITE + f"{name}: {entity}")
    print(colorama.Style.RESET_ALL)
    return result
        
