# Bisk

- theme: risk it for the biscuit

## key concept

- risk but with biscuits
- different biscuits are different biscuits
- different factions are different brands
- humans will eat from a stockpile but if stockpile is too low they will eat your units
- procgen map within tin fixed size and dimensions
- three factions: red, green, blue
- win condition: take all territory, highest stockpile after a certain amount of time
- risk style tile map, 20 regions, named and funny names
- five resources: wheat, sugar, cream, cocoa
- stockpile slider

## Structure

- pygame
- main:
	- loading the game
 	- title screen
- game loop
	- updating screen
	- map generation at initialisation
	- taking input
- faction class
	- units
	- colour
	- name
	- territories
	- stockpile
- unit class
	- value
	- requirements
- ui class
- map class
	- generation
	- region list
- region class
	- resource list
	- unit generation number
- combat manager
	- resolve combats each turn
	- list of takeovers
