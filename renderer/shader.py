from OpenGL.GL import shaders
from OpenGL.GL import *

class Shader:

    def __init__(self, vertexShaderFile: str, fragmentShaderFile):
        with open(vertexShaderFile) as f:
            vertex_shader = f.read()

        with open(fragmentShaderFile) as f:
            fragment_shader = f.read()

        self.shader_program = shaders.compileProgram(
        shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
        shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))