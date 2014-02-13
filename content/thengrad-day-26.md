Title: Day 26
Date: 2013-07-05T11:41:00
Slug: thengrad-day-26
Author: thengrad
Tags: legacy, foss@rit
Category: legacy
URL: articles/thengrad/day-26.html
save_as: articles/thengrad/day-26.html
Summary: With a little bit of work and fixing small typos I have now added a way for recipe to be selected in game. What I did was adapt the old way of doing the profit mini-game and put it at the end of the current end of the day log script. The way it works is that [LemonadeGui](https://github.com/FOSSRIT /lemonade-stand/blob/develop/LemonadeGui.py) stores two arrays. One is an array of the array of keys for each option. The other is an array of the current index number for each array of keys. Then eve ... 

With a little bit of work and fixing small typos I have now added a way for
recipe to be selected in game. What I did was adapt the old way of doing the
profit mini-game and put it at the end of the current end of the day log
script. The way it works is that [LemonadeGui](https://github.com/FOSSRIT
/lemonade-stand/blob/develop/LemonadeGui.py) stores two arrays. One is an
array of the array of keys for each option. The other is an array of the
current index number for each array of keys. Then event handler would
increment the index number using which mode the game was in as the current
matching index of both arrays. What I had to do was add the recipe options to
the array of array of keys, add a way to visually display which recipe was
selected and then, and then have it so that when the event handler would
handle the key pressed of enter on the end of the day mode it would then store
the recipe selected by the current index of the key for the dictionary to the
property in [LemonadeMain](https://github.com/FOSSRIT/lemonade-
stand/blob/develop/LemonadeMain.py). After that I added more recipes for
verity.

