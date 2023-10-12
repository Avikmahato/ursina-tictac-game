from ursina import*
speed=.1
def update():
    global speed
    cube.x+=speed
    if abs(cube.x)>4 :
        speed*=-1   
    
def input(key):
    global speed 
    if held_keys['y']:
        cube.x=cube.y
app=Ursina()

cube=Entity(model='cube',scale=.5)
app.run()