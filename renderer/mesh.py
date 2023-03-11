from OpenGL.GL import *
import ctypes

class Mesh:

    def __init__(self, vertices: list[float], colors: list[float], indices: list[int]) -> None:
        self.indiceslen = len(indices)
        self.len = len(vertices)
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        self.colors =glGenBuffers(1)
        self.indices = glGenBuffers(1)
        self.set_vbo_data(vertices)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(0))
        self.set_color_data(colors)
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(0))
        if self.indiceslen != 0:
            self.set_indices_data(indices)
        glBindVertexArray(0)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    def set_vbo_data(self, vertices: list[float]):
        dataArray = (GLfloat*len(vertices))(*vertices)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, len(dataArray)*4, dataArray, GL_STATIC_DRAW)

    def set_color_data(self, colors: list[float]):
        dataArray = (GLfloat*len(colors))(*colors)
        glBindBuffer(GL_ARRAY_BUFFER, self.colors)
        glBufferData(GL_ARRAY_BUFFER, len(dataArray)*4, dataArray, GL_STATIC_DRAW)

    def set_indices_data(self, indices: list[int]):
        dataArray = (GLint*len(indices))(*indices)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.indices)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(dataArray)*4, dataArray, GL_STATIC_DRAW)


