#!/usr/bin/python3
#
# dpub, a publishing assistant which can push and pull from various sources
# currently, those source include github and discourse, where the github is
# defined by the current working directory, and the discourse instance is
# defined by a configuration file; this program tries to use natural language
# as much as possible, for example:
#
# dpub push file discstats.md to discourse topic 1515
# dpub pull all files from github
# dpub pull all files from dicourse matching category 5
# dpub push file foo.c to github
#
# dpub push
#      pull

import argparse


def setmenu():
    main_parser = argparse.ArgumentParser(
        "dpub",
        "doc publishing program",
        '"dpub command -h" for details'
    )
    pos1parser = main_parser.add_subparsers(
        dest="pos1"
    )
    parser_push = pos1parser.add_parser(
        'push',
        help="push a file(s) to a destination"
    )
    parser_pull = pos1parser.add_parser(
        'pull',
        help="pull a file(s) from a source"
    )
    parser_convert = pos1parser.add_parser(
        'convert',
        help="convert a file locally"
    )
    parser_split = pos1parser.add_parser(
        'split',
        help="split a document into versions, based on tags"
    )
    push_sub = parser_push.add_subparsers(
        dest="push_l2"
    )
    parser_push_github = push_sub.add_parser(
        'github',
        help="github corresponding to current local clone directory"
    )
    ppg_gr = parser_push_github.add_mutually_exclusive_group(
        required=True
    )
    ppg_gr.add_argument(
        '-f',
        '--file',
        nargs=1,
        help="file to push to github",
        dest="file"
    )
    ppg_gr.add_argument('-a','--all', action='store_true',help="push all files to github",dest="gitpushall")
    parser_push_discourse = push_sub.add_parser(
        'discourse',
        help='discourse found at URL specified in config file'
    )
    ppg_gr2 = parser_push_discourse.add_mutually_exclusive_group(required=True)
    ppg_gr2.add_argument(
        '-f',
        '--file',
        nargs=1,
        help="file to push to discourse",
        dest="file"
    )
    ppg_gr2.add_argument(
        '-a',
        '--all',
        action='store_true',
        help="bulk file push, based on title and topic gathered from filename",
        dest="all"
    )
    ppg_gr3 = parser_push_discourse.add_mutually_exclusive_group(required=True)
    ppg_gr3.add_argument(
        '-t',
        '--tnum',
        nargs=1,
        help="topic number to which to push the file",
        dest="topic",
        type=int
    )
    ppg_gr3.add_argument(
        '-n',
        '--new',
        action='store_true',
        help="push file to discourse, creating a new topic in the process",
        dest="new"
    )
    ppg_gr3.add_argument(
        "-b",
        "--bulk",
        action='store_true',
        help="topic flag to confirm bulk push",
        dest="bulk"
    )
    parser_push_discourse.add_argument(
        '-T',
        '--title',
        nargs=1,
        help="title for new document",
        dest="title"
    )
    parser_push_discourse.add_argument(
        '-k',
        '--cat',
        nargs=1,
        type=int,
        help="category for new document",
        dest="cat"
    )
    parser_push_discourse.add_argument(
        '-c',
        '--cfg',
        nargs=1,
        help="alternate config file with discourse URL & auth params",
        dest="config"
    )
    parser_push_discourse.add_argument(
        '-m',
        '--match',
        action="append",
        dest="tags",
        default=[],
        help='specify conditional tags (one tag per "-m") to enable conditional paragraphs when pushing a discourse file'
    )

    # level 2 pull subparser: github / discourse
    pull_sub = parser_pull.add_subparsers(dest="pull_l2")
    parser_pull_github = pull_sub.add_parser(
        'github',
        help="github corresponding to current local clone directory"
    )
    ppg_grp = parser_pull_github.add_mutually_exclusive_group(required=True)
    ppg_grp.add_argument('-f','--file',nargs=1,help="file to pull from github",dest="file")
    ppg_grp.add_argument('-a','--all', action='store_true',help="pull all files from github",dest="gitall")
    parser_pull_discourse = pull_sub.add_parser(
        'discourse',
        help='discourse found at URL specified in config file'
    )
    ppg_grp2 = parser_pull_discourse.add_mutually_exclusive_group(required=True)
    ppg_grp2.add_argument(
        '-f',
        '--file',
        nargs=1,
        help="file to pull from discourse",
        dest="file"
    )
    ppg_grp2.add_argument(
        '-r',
        '--range',
        nargs=2,
        help="-r <start> <end>: pull topics from start to end",
        dest="range",
        type=int
    )
    ppg_grp3 = parser_pull_discourse.add_mutually_exclusive_group(required=True)
    ppg_grp3.add_argument(
        '-t',
        '--tnum',
        nargs=1,
        help="topic number from which to pull the file",
        dest="topic",
        type=int
    )
    ppg_grp3.add_argument(
        '-b',
        '--bulk',
        action='store_true',
        help='confirms bulk pull indicated with "-a"',
        dest="bulk"
    )
    parser_pull_discourse.add_argument(
        '-k',
        '--cat',
        nargs=1,
        help="restrict discourse category to CAT",
        dest="cat",
        type=int
    )
    parser_pull_discourse.add_argument(
        '-l',
        '--live',
        action='store_true',
        help="do not pull deleted articles",
        dest="nodeleted"
    )
    parser_pull_discourse.add_argument(
        '-c',
        '--cfg',
        nargs=1,
        help="alternate config file with discourse URL & auth params",
        dest="config"
    )
    parser_pull_discourse.add_argument(
        '-j',
        '--json',
        action='store_true',
        help='store topic JSON in "topic.json" (useless with -a)',
        dest="topicjson"
    )
    parser_pull_discourse.add_argument(
        '-J',
        '--JSON',
        action='store_true',
        help='store post JSON in "post.json" (useless with -a)',
        dest="postjson"
    )

    return main_parser
