from glfw import *

def init(entity):
    entity.alpha = 0.01

def update(entity, key, signal, deltaTime):
    if key.is_pressed(KEY_F):
        signal('Fullscreen')
    if key.is_pressed(KEY_ESCAPE):
        signal('ExitFullscreen')
    if key.is_pressed(KEY_D):
        cameraPos = signal("GetCameraPosition")
        x = float(cameraPos[0])
        x -= 1 * deltaTime
        cameraPos[0]= x
    if key.is_pressed(KEY_A):
        cameraPos = signal("GetCameraPosition")
        x = float(cameraPos[0])
        x += 1 * deltaTime
        cameraPos[0]= x
    if key.is_pressed(KEY_W):
        cameraPos = signal("GetCameraPosition")
        x = float(cameraPos[2])
        x += 10 * deltaTime
        cameraPos[2]= x
        