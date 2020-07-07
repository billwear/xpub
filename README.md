## dpub
Command line client for document publishing, especially with Discourse and Github.

### Usage
dpub [command] [source] [options]

### Command tree
<ul>
<li>pull - Pull a document</li>
<ul>
<li>github - pull a markdown document from github, by name.  A local github must be linked origin/master, and SSH authentication must be set up.
<ul>
<li>file=<em>filename</em> (required)
</ul>
<li>discourse - pull a markdown document from discourse, by topic number. The discourse URL & auth must be in a YAML file (see below).
<ul>
<li>file=<em>filename</em> (required)
<li>topic=<em>topic number</em> (required)
<li>config=<em>config file</em> (optional, defaults to /etc/dc.yaml)
</ul>
</ul>
<li>push - Push a document</li>
<ul>
<li>github - push a markdown document to github, by name. A local github must be linked origin/master, and SSH authentication must be set up.
<ul>
<li>file=<em>filename</em> (required)
</ul>
<li>discourse - push a markdown document to discourse, by topic number. The discourse URL & auth must be in a YAML file (see below).
<ul>
<li>file=<em>filename</em> (required)
<li>topic=<em>topic number</em> (required); set to "new" to create a new topic
<li>config=<em>config file</em> (optional, defaults to /etc/dc.yaml)
</ul>
</ul>


### Copyright
MIT License
Copyright (c) 2020 Bill Wear
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
