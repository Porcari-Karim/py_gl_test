import glfw
from .glfw import GlfwWindow
from .base import BaseWindow
import signal
import atexit

glwf_initialized: bool = False


def handle_exit(*args):
    print("Handling End of the program")
    if glwf_initialized:
        glfw.terminate()

#Bindind the handle exit function to kill signal + exit signal + error signal
def init_windowing_system():
    initGLFW()
    atexit.register(handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)
    signal.signal(signal.SIGINT, handle_exit)

def initGLFW():
    if not glfw.init():
        return None
    global glwf_initialized 
    glwf_initialized = True
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

def create_window(width: int, height:int, title:str)-> BaseWindow:
    
    if glwf_initialized:
        window = GlfwWindow(width, height, title)
        return window

