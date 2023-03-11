import pywavefront
import itertools

def get_obj_vertices(filename):
    scene = pywavefront.Wavefront(filename, strict=False, collect_faces=True)
    scene.parse()
    faces = list(itertools.chain(*scene.mesh_list[0].faces))

    return scene.mesh_list[0].materials[0].vertices, faces



