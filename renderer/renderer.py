from OpenGL.GL import *
from .shader import Shader
from .scene import Scene
from .camera import Camera
import pyrr
import numpy as np
import time

class Renderer:

    def __init__(self, shader: Shader) -> None:
        self.program = shader
        glClearColor(0, 0, 0, 1)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)
        glUseProgram(self.program.shader_program)
        self.projection_uniform = glGetUniformLocation(self.program.shader_program, "projection")
        self.view_uniform = glGetUniformLocation(self.program.shader_program, "view") 
        self.model_uniform = glGetUniformLocation(self.program.shader_program, "model")
        self.camera = Camera([0, 0, 0], [0, 0, 0])
        self.projection_matrix = pyrr.matrix44.create_perspective_projection(45, 800/600, 0.1, 1000, dtype=np.float32)

    def set_projection_matrix(self, fov = 45, width=800, height=600):
        self.projection_matrix = pyrr.matrix44.create_perspective_projection(fov, width/height, 0.1, 1000, dtype=np.float32)
    def set_viewport(self, x:int, y:int, width:int, height:int):
        glViewport(x, y, width, height)

    def render(self, scene: Scene):
        #start = time.time()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUniformMatrix4fv(self.projection_uniform, 1, GL_FALSE, self.projection_matrix)
        view_matrix = pyrr.matrix44.create_identity(dtype=np.float32)
        view_matrix = pyrr.matrix44.multiply(
            view_matrix,
            pyrr.matrix44.create_from_eulers(np.radians(self.camera.eulers), dtype=np.float32)
        )
        view_matrix = pyrr.matrix44.multiply(
            view_matrix,
            pyrr.matrix44.create_from_translation(self.camera.postion, dtype=np.float32)
        )

        glUniformMatrix4fv(self.view_uniform, 1, GL_FALSE, view_matrix )

        for entity in scene.entities:
            if entity.mesh is not None:
                
                model_matrix = pyrr.matrix44.create_identity()
                model_matrix = pyrr.matrix44.multiply(
                    m1 = model_matrix,
                    m2 = pyrr.matrix44.create_from_translation(entity.position, dtype=np.float32)
                )
                glUniformMatrix4fv(self.model_uniform, 1, GL_FALSE, model_matrix)

                glBindVertexArray(entity.mesh.vao)
                if entity.mesh.indiceslen != 0:
                    glDrawElements(GL_TRIANGLES, entity.mesh.indiceslen, GL_INT, None)
                else:
                    glDrawArrays(GL_TRIANGLES, 0, int(entity.mesh.len/3))
        glBindVertexArray(0)
        
        # passed  = time.time() - start
        # if passed != 0:
        #     print(1000 / passed)
        