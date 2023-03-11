from window.window import init_windowing_system, create_window
from renderer.scene import Load_Scene
from renderer.shader import Shader
from renderer.renderer import Renderer
from .keys import KeyHandler
import time
import glfw

class Application:

    def __init__(self, sceneName) -> None:
        init_windowing_system()
        self.window = create_window(800, 600, "PY GL Test")
        self.window.use_context()
        self.myShader = Shader("shaders/baseVertex.glsl", "shaders/baseFrag.glsl")
        self.myRenderer = Renderer(self.myShader)
        self.scene = Load_Scene(sceneName)
        self.keyHandler = KeyHandler(self.window.window)
        self.lastFrame = None

        #States
        self.fullscreen = False

    def run(self):
        if self.lastFrame == None:
            self.lastFrame = time.time()

        def signal(sig, *args):
            return self.handle_signal(sig, args)
        
        while not self.window.should_close():
            self.window.poll_events()
            deltaTime = time.time() - self.lastFrame
            self.lastFrame = time.time()
            for entity in self.scene.entities:
                entity.update(self.keyHandler, signal, deltaTime)
            self.myRenderer.render(self.scene)
            self.window.present()
            
            

    def handle_signal(self, signal, *args):
        if signal == "Fullscreen":
            if not self.fullscreen:
                monitor = glfw.get_primary_monitor()
                mode = glfw.get_video_mode(monitor)
                glfw.set_window_monitor(self.window.window, monitor, 0, 0, mode.size.width, mode.size.height, 60)
                glfw.maximize_window(self.window.window)
                self.myRenderer.set_projection_matrix(width=mode.size.width, height=mode.size.height)
                self.myRenderer.set_viewport(0, 0, mode.size.width, mode.size.height)
                self.fullscreen = True
        if signal =="ExitFullscreen":
            if self.fullscreen:
                monitor = glfw.get_primary_monitor()
                mode = glfw.get_video_mode(monitor)
                glfw.set_window_monitor(self.window.window, None, 0, 0, self.window.width, self.window.height, 60)
                xpos = int((mode.size.width/2) - (self.window.width/2))
                ypos = int((mode.size.height/2) - (self.window.height/2))
                glfw.set_window_pos(self.window.window, xpos, ypos)
                self.myRenderer.set_viewport(0, 0, self.window.width, self.window.height)
                self.myRenderer.set_projection_matrix(width=self.window.width, height=self.window.height)
                self.fullscreen = False
            
        if signal == "GetCameraPosition":
            return self.myRenderer.camera.postion
        if signal == "SetCameraPosition":
            coords = list(args)
            if len(coords) != 3:
                print("SetCameraPosition needs 3 integers as arguments")
            self.myRenderer.camera.postion = coords