### xpub - general purpose translation and publishing tool

**xpub** moves files between local directories, github, and discourse -- and converts discourse markdown to html.  It can deal with a single file, an entire directory, or a range of discourse topics.

Install it in your path and type `xpub help` to get started.

-----

**xpub** needs the following libraries:

 - sys
 - subprocess
 - json
 - os
 - time
 - re
 - markdown
 - jinja2
 - click
 - yaml

Most of these are standard.

Helper files for xpub include the following:

* dcstat - collects statistics about open, closed, and in-progress discourse posts, creates a report, and prints it.  Currently contains a specific list of posts for MAAS team, needs to be modified to read a list or scan all.

* mkurls - creates discourse URL map entries from a directory of .md files, using the filenames to create the URLs.

* bmake - creates makefile entrie from a directory of .md master files and a subdirectory called "originals" that contains the specific RAD versions of the files.

* foo - creates RAD menu blocks at start of every file, based on master file name and names of corresponding files in subdir "originals."  Very specific to MAAS RAD at the moment.

* clean_navigation.sh - pull the navigation section, URL mapping list, and URL redirect list out of any specified file.  Used to create multiple copies of MAAS doc's "index.html" proxy, without damaging the root proxy file, which has to have all that information in it.