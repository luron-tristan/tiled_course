# Tiled

creates level layouts

imports graphics and lets you place elements to create your level
it only creates the layout, NOT the game logic

Tiled => painting level
3 elements:

- canvas we are painting on: Map
- colors: Tilesets
- brushes: tools

When opening a tileset
=> /!\ check the size of each tiles /!\

## Tiled

center = canvas => where we create our level

top-right: layers => different layes we can draw on, to put elements on top of each other

top: brushes, used to place tiles on the map

left: information panel

tabs: every single map or tileset opened goes into a tab

bottom-right: Tilesets => colors we are going to use

add multiple layers to draw different types of elements

- floor
- plants and rocks

tile probability => used for rate in random

objects: graphics of any size placed wherever you want on the map
insert tile
shapes => useful for player entering area...
text => not working in pygame?
when create new map: tile render order, mostly right down => elements down and right appear in front
NAME EVERYTHING

## Terrain

special tiles that react to their surroundings
3 different ways to create these tiles

- check corners
- check edges
- check corners + edges

terrains tilesets
terrain brush (T)

terrains + motifs

stick to simple terrains sets

export as
.tmx,
.csv, => exporting a number (id)
.json

## isometric

keep tile width
height needs to be cut off

## import Tiled into pygame

- import data via csv/json => long process
- use pytmx module => easier way

# pygame

tmx_data = load_pygame(".\\data\\tmx\\basic.tmx")
print(dir(tmx_data))

<!-- get layers -->

print(tmx_data.layers) # get all layers
for layer in tmx_data.visible_layers: # get visible layers
print(layer)

print(tmx_data.layernames) # get all layer names as dict
print(tmx_data.get_layer_by_name('Floor')) # get one layer by name

print(tmx_data.objectgroups)
for obj in tmx_data.objectgroups: # get object layers
print(obj)

### get tiles

layer = tmx*data.get_layer_by_name('Floor')
print(dir(layer))
for x, y, surf in layer.tiles(): # get all the information
print(x * 128)
print(y \_ 128)
print(surf)
x & y refer to the tile inside of the map
to get actual position, x&y \* size of the tileset

print(layer.data)
print(layer.name)
print(layer.id)

### get objects

object_layer = tmx_data.get_layer_by_name("Objects")
print(dir(object_layer))

for obj in tmx_data.objects:
print(obj)

for obj in object_layer: # x, y and image
print(obj.x)
print(obj.y)
print(obj.image)
if obj.type == "Shape":
if obj.name == "Marker": # only useful for position
print(obj.x)
print(obj.y)

if obj.name == "Rectangle":
print(obj.x)
print(obj.y)
print(obj.width)
print(obj.height)
print(obj.as_points)

if obj.name == "Ellipse":
print(obj)

if obj.name == "Polygon":
print(obj.as_points) # bounding box of the polygon
print(obj.points)
