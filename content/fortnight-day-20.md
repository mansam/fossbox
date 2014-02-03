Title: Day 20
Date: 2013-06-25T10:11:00
Slug: fortnight-day-20
Author: fortnight
Tags: legacy, foss@rit
Category: legacy
Summary: # Bash Script Snorkeling  So, as I mentioned previously, I'm taking notes on School Server code and scripts to understand what they consist of. However, it is still quite the rocky road, when I come across lines full of symbols I don't understand.  For example:  if [ "$1" = '-h' -o $# -gt 1 ]; then  for file in 'find $DOMAIN_CONFIG_DIR -maxdepth 1 -type f -perm /u+x ! -name "*~" -print | sort' ;  do  ["${file%.cfsaved}" != "${file}" ] && continue  ["${file%.rpmsave}" != "${file}" ] && continue   ... 

# Bash Script Snorkeling

So, as I mentioned previously, I'm taking notes on School Server code and
scripts to understand what they consist of. However, it is still quite the
rocky road, when I come across lines full of symbols I don't understand.

For example:

if [ "$1" = '-h' -o $# -gt 1 ]; then

for file in 'find $DOMAIN_CONFIG_DIR -maxdepth 1 -type f -perm /u+x ! -name
"*~" -print | sort' ;

do

["${file%.cfsaved}" != "${file}" ] && continue

["${file%.rpmsave}" != "${file}" ] && continue

["${file%.rpmorig}" != "${file}" ] && continue

["${file%.rpmnew}" != "${file}" ] && continue

["${file%.swp}" != "${file}" ] && continue

["${file%.v}" != "${file}" ] && continue

eval $file $new_domain_name;

echo "xs-domain-config ran $file" | tee -a $LOG

done

In Psuedo code, this can be translated into:

if (the first argument is the help option or the number of arguments is
greater than one)

loop through each file in the directory saved as DOMAIN_CONFIG_DIR, but only
open files you've permission to execute, don't go deeper into directories.

for each file, ignore it if it ends in ".cfsaved", ".rpmsave", ".rpmorig",
".rpmnew", ".swp", "v", otherwise, run the file with the variable
"new_domain_name" as its argument, and then append "xs-domain-config ran 'name
of file' " to the log.

For some info on Bash Scripting, click [here](http://www.tldp.org/LDP/Bash-
Beginners-Guide/html/sect_07_01.html) or [there](http://www.tldp.org/LDP/Bash-
Beginners-Guide/html/sect_03_02.html). Bash scripting can do some cool stuff,
like install a school server, or make you really frustrated as you struggle to
install a school server.

[My feelings for the
day](http://meme5.net/#t=LOST_IN_BASH_SCRIPT;b=BETTER_DRINK_MY_OWN_PISS;i
=meme-beargrylls;)

