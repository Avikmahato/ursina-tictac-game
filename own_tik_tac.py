from ursina import*
app=Ursina()
player=Entity(name='O',color=color.red)
cur=Tooltip(text=player.name,color=player.color,scale=2,enabled=True)
cur.background=False
ply=[[None,None,None],
    [None,None,None],
    [None,None,None]]
for i in range(3):
    for j in range(3):
        but=Button(parent=scene,position=(i,j))
        ply[i][j]=but
        def on_click(bapi=but):
            bapi.text=player.name
            bapi.color=player.color
            bapi.collision=False
            winner()
            if player.name=='O':
                player.name='X'
                player.color=color.green
            else:
                player.name='O'
                player.color=color.red
            cur.text=player.name
            cur.color=player.color
        but.on_click=on_click
def winner():
    Name=player.name
    won=(
        (ply[0][1].text==Name and ply[0][0].text==Name and ply[0][2].text==Name)or
        (ply[0][0].text==Name and ply[1][1].text==Name and ply[2][2].text==Name)or
        (ply[0][2].text==Name and ply[1][1].text==Name and ply[2][0].text==Name)or
        (ply[0][0].text==Name and ply[1][0].text==Name and ply[2][0].text==Name)or
        (ply[2][0].text==Name and ply[2][1].text==Name and ply[2][2].text==Name)or
        (ply[0][2].text==Name and ply[1][2].text==Name and ply[2][2].text==Name)or
        (ply[0][1].text==Name and ply[1][1].text==Name and ply[2][1].text==Name)or
        (ply[1][0].text==Name and ply[1][1].text==Name and ply[1][2].text==Name))
    if won:
        if Name=='X':
            print_on_screen("Avik Mahato Is Winner",scale=3,duration=10,position=(-.30,.40))
        else:
            print_on_screen("Susmita Mahato Is Winner",scale=3,duration=10,position=(-.30,.40))
app.run()