# dpub(7) - edit and publish discourse topics

version 0.8, 26 June 2020

```
dpub [OPTION]...
```

<a name="description"></a>

# Description

**dpub**
gets, puts, and creates topics to/from discourse using the discourse API. It
converts between discourse markdown and JSON, as appropriate to the other options
selected.

The markdown files retrieved from discourse by
**dpub**
can be freely edited, as long as discourse markdown is retained.
These edited files can then reposted over the existing text by using the same topic number when putting them back, or used to create a new file, with topic number assigned
by discourse when the new topic is created.

**dpub**
is written in python; it requires at least python3 to be installed on the system where it will be used.

<a name="options"></a>

# Options


* **-g, --get**  
  Read a numbered TOPIC into FILENAME; requires -t TOPIC and -f FILENAME.
* **-p, --put**  
  Write FILENAME to TOPIC number; requires -t TOPIC and -f FILENAME.
* **-c, --create**  
  Create a new topic and write FILENAE to it; requires -f FILENAME.
  **Note:**
  All the above options are mutually exclusive. If they are used together, the
  results are currently unpredictable.

* **-f &lt;FILENAME&gt;, --file=FILENAME**  
  Sets the filename to be read (-p, -c) or written (-g) as part of the specified
  operation.
* **-k &lt;CONFIG_FILE&gt;, --config=CONFIG_FILE**  
  Sets the yaml configuration file that contains the discourse URL, the user's api-key,
  and the user's name for authentication purposes.  See FILES for a description of the
  required format.
* **-j &lt;JSON_FILE&gt;, --json=JSON_FILE**  
  Causes
  **dpub**
  to output the
  **post**
  JSON-encoded data to JSON_FILE before converting it to markdown.  Works only with the
  **-g**
  option.


* **-J &lt;TOPIC_JSON_FILE&gt;, --JSON=TOPIC_JSON_FILE**  
  Causes
  **dpub**
  to output the
  **topic**
  JSON-encoded data to TOPIC_JSON_FILE before converting it to markdown.  Works only with the
  **-g**
  option.


* **-h**  
  Prints program usage information and exits

<a name="files"></a>

# Files


* **dc.yaml**  
  Contains the information necessary to authenticate to the correct discourse API:

**base_url:**https://discourse.&lt;subdomain&gt;.&lt;suffix&gt;  
**api_username:**&lt;your_username&gt;  
**api_key:**&lt;api-key**string....................................&gt;**

<a name="bugs"></a>

# Bugs

Currently, the code does not check whether the user input more than one of the mutually
exclusive options
**-g**
/
**-p**
/
**-c**
on the same command line.  As a consequence, the behavior when specifying more than one of these options is unpredictable.

<a name="author"></a>

# Author

Bill Wear [wowear@gmail.com](mailto:wowear@gmail.com)

<a name="copyright"></a>

# Copyright

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
