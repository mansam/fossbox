Title: MediaWiki Visualization
URL: projects/mediawiki-visualization
save_as: projects/mediawiki-visualization/index.html

MediaWiki Visualization is a python program that watches a wiki for changes
using the MediaWiki API. It loads up a list of pages and their link structures
and then watches the change log. When a page is changed it links the user to
the page as well as linking to any pages it links to.

The visualization is currently using
[ubigraph](http://ubietylab.net/ubigraph/) to draw the visualization with the
help of the networkx python module. It also uses the [twisted
framework](http://twistedmatrix.com) to pull the api at a configurable
interval.

## Examples

This is an example on rit's [Ritpedia](http://www.rit.edu/ritpedia).

[MediaWiki Visualization Preview](http://www.youtube.com/watch?v=Sau6l9TOhgk)

Note: The second mode disables the users and just shows the pages and how they
are linked. Note that this is still a very new wiki.

I have [uploaded another video](http://www.youtube.com/watch?v=tUEDN5OkGUQ)
with the ability to pull the page list.

## Get Involved

Source: [mediawiki_visualization on
gitorious.org](http://gitorious.org/jlew/mediawiki_visualization)

Future Plans: Keep track of categories for every page. That will allow it to
look a bit more linked as some wikis rely on the category system as part of
its navigation scheme.

[Mediawiki Visualization blog](http://jlewopensource.blogspot.com/search/label
/Media%20Wiki%20Visualization).

