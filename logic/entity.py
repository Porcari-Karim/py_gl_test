from renderer.mesh import Mesh

def Vec3(x: float = 0, y: float = 0, z: float = 0,):
    return [x, y, z]

class Entity:

    def __init__(self, mesh: Mesh) -> None:
        self.mesh = mesh
        self.position = Vec3()
        self.rotation = Vec3()
        self.script = None

    def update(self, *args):
        if self.script is not None:
            self.script(self, *args)


    