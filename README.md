## Tiled

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

# Tiled

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

# Terrain

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

# isometric

keep tile width
height needs to be cut off

# import Tiled into pygame

- import data via csv/json
- use pytmx module
