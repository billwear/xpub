#!/bin/bash
#
# note, must be run sudo
# also note, you may have to create /usr/local/share/man/man7 (also sudo)
#
sudo cp dpub.7 /usr/local/share/man/man7
sudo gzip /usr/local/share/man/man1/dpub.7
sudo mandb
