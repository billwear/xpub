## dpub
Command line client for document publishing, especially with Discourse and Github.

***Usage***<br/>
dpub [command] [source] [options]

***Available commands***
 **pull** | Pull a document
 **push** | Push a document

<dt>Available sources</dt>
github: Push or pull a markdown document <> github. A local github must be linked origin/master, and SSH authentication must be set up.<br/
discourse: Push or pull a markdown document <> a discourse topic. The discourse URL & auth must be in a YAML file (see below).</dd>

<dt>Available options</dt>
<file=<filename>        Markdown file to push or pull
                          - required for all sources
  topic=<topic-number>   Discourse topic number push target
                          - required for discourse
			  - set to "new" to create a new topic
  [config=<configfile>]  Config file containing URL & auth info
                          - optional for discourse
                          - defaults to /etc/dc.yaml
</dl>

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
