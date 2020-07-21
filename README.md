### xpub - general purpose translation and publishing tool

**xpub** lets you push, pull, and convert files.  To use dpub:

1. Install it in your path.
2. Type 'xpub' at the command line, and follow the help prompts to see how it works.

**xpub** uses whole word commands and options.  If you type a partial command sequence, xpub will give you hints for what else is needed.

At any point, you can add a "-h" to get detailed help for that command sequence.

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
 - yaml

Most of these are standard, except maybe `markdown` and `jinja2`, but I always list all the dependencies just in case.
