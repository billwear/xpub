## dpub

Command line client for document publishing.

**Usage:**
  dpub [command] [source] [options]

**Available commands:**
  pull  Pull a document
  push  Push a document

**Available sources:**
  github     Push or pull a markdown document <> github
              - local github must be linked origin/master
	      - SSH authentication must be set up
  discourse  Push or pull a markdown document <> a discourse topic
              - URL & auth must be in a YAML file (see below)

**Available options:**
  file=<filename>        Markdown file to push or pull
                          - required for all sources
  topic=<topic-number>   Discourse topic number push target
                          - required for discourse
			  - set to "new" to create a new topic
  [config=<configfile>]  Config file containing URL & auth info
                          - optional for discourse
                          - defaults to /etc/dc.yaml
