Title: Homework Blog Post: Probably versus Maybe and li versus LI
Date: 2012-02-08T17:27:00
Slug: decause-homework-blog-post-probably-versus-maybe-and-li-versus-li
Author: decause
Tags: legacy, foss@rit
Category: legacy
URL: articles/decause/homework-blog-post-probably-versus-maybe-and-li-versus-li.html
save_as: articles/decause/homework-blog-post-probably-versus-maybe-and-li-versus-li.html
Summary: Here is the link to my github repo:  [Github](https://github.com/decause/floss-sem-homework1)  # Probably versus Maybe      -    // Play the background music     +    // Play the background music if sound is supported          if (soundIsSupported()) {              su.play(sources, 0, 156000, globalVolume, false);          }     @@ -150,14 +150,15 @@ function soundIsSupported() {          var a = new Audio();          var failures = 0;     +          for (var i = 0; i < sources.length; i++) {   ... 

Here is the link to my github repo:

[Github](https://github.com/decause/floss-sem-homework1)

## Probably versus Maybe

    -    // Play the background music
    +    // Play the background music if sound is supported
         if (soundIsSupported()) {
             su.play(sources, 0, 156000, globalVolume, false);
         }
    @@ -150,14 +150,15 @@ function soundIsSupported() {
         var a = new Audio();
         var failures = 0;
    +
         for (var i = 0; i < sources.length; i++) {
    -        if (a.canPlayType(sources[i][1]) !== "probably") {
    +        if (a.canPlayType(sources[i][1]) !== "maybe") {
                 failures++;
             }
         }
         if (failures !== sources.length) {
    -        su = new SoundUtil()
    +        su = new SoundUtil();
                 return true;
         } else {
             return false;

In the above code blocks, you can see the two very subtle changes that needed
to be made to enable sound in the example code we were to deploy for homework.
I think the author intended on not allowing the client to play sound if the
qualifier was "maybe", meaning that if there was an implicit _chance_ that the
browser could play a .mp3 or .ogg. As opposed to "probably" where the browser
explicitly claims to support these formats. Either way, after firebugging my
way around I found out that my browser was setting canPlayType to 'maybe', and
rather than changing what my browser was telling the code, I just changed the
qualifier and hoped for the best. It worked ;)

## li versus LI

The biggest lesson I learned was about case-(in)senstivity.

In the section where you use jQuery to select all of the "li" elements in the
build menu (or elements that have a parentNode tagname of "li"), at first I
just did like so:

    default:
                    if ((e.target.tagName === 'li' || e.target.parentNode.tagName === 'li')) {
                        var t = (e.target.tagName === 'li') ? e.target : e.target.parentNode;

Litltle did I know, that this is a case SENSITIVE operation, and that if you
don't get it right, it will just silently fail... After spending quite some
time hunting this one down, it eventually was a manual parsing of source files
with my eyeballs to see the very subtle CAPS difference.

    default:
                    if ((e.target.tagName === 'LI' || e.target.parentNode.tagName === 'LI')) {
                        var t = (e.target.tagName === 'LI') ? e.target : e.target.parentNode;

This was especially confusing since THE LI ELEMENTS WERE NOT IN CAPS IN THE
SOURCE CODE... and generally HTML is case insensitive...

Either way, it is done now, and in doing so, I found a bug in the code
example, and sent the patch back upstream to the author. It was totally
accepted :)

[My (quite trivial) Patch to the Course Textbook's example Code
Repo](https://github.com/andrespagella/Making-Isometric-Real-time-
Games/commit/6ac45dfd2d20e73b53666965bb9c93b4a3528d97)

