Title: Day 29
Date: 2013-07-05T15:44:00
Slug: thengrad-day-29
Author: thengrad
Tags: legacy, foss@rit
Category: legacy
Summary: I figured out what huge source of the errors I was getting thrown at me when I added the strawberry's were from. They way the recipes were being displayed hinged on every ingredient appearing in every recipe. I found this to be a bit of an problem for allowing Lemonade Stand to be flexible. So I created a feature branch where I changed it so that if it doesn't find an ingredient in the recipe dictionary it will just add it with an amount 0. This way there can be a bunch of ingredients and recipe ... 

I figured out what huge source of the errors I was getting thrown at me when I
added the strawberry's were from. They way the recipes were being displayed
hinged on every ingredient appearing in every recipe. I found this to be a bit
of an problem for allowing Lemonade Stand to be flexible. So I created a
feature branch where I changed it so that if it doesn't find an ingredient in
the recipe dictionary it will just add it with an amount 0. This way there can
be a bunch of ingredients and recipes with out having to go through and make
sure that every ingredient is a least listed under every recipe in the
[constants.py](https://github.com/FOSSRIT/lemonade-
stand/blob/develop/constants.py)

