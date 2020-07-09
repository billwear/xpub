#!/usr/bin/python3

import argparse

# entry point for importing code
def setmenu():
    parser = argparse.ArgumentParser(
        "dpub",
        "doc publishing program",
        'Enter "dpub command -h" for details'
    )
    subparserL1 = parser.add_subparsers(
        dest="l1"
    )
    parser_push = subparserL1.add_parser(
        'push',
        help="push a file to a destination"
    )
    parser_pull = subparserL1.add_parser(
        'pull',
        help="pull a file from a source"
    )
    parser_convert = subparserL1.add_parser(
        'convert',
        help="convert a file locally"
    )
    parser_split = subparserL1.add_parser(
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
        help="filename to push to github",
        dest="gitpushfile"
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
        help="filename to push to discourse",
        dest="discpushfile"
    )
    ppg_gr3 = parser_push_discourse.add_mutually_exclusive_group(required=True)
    ppg_gr3.add_argument(
        '-t',
        '--tnum',
        nargs=1,
        help="topic number to which to push the file",
        dest="discpushtopic",
        type=int
    )
    ppg_gr3.add_argument(
        '-n',
        '--new',
        action='store_true',
        help="push file to discourse, creating a new topic in the process",
        dest="discpushnew"
    )
    parser_push_discourse.add_argument(
        '-T',
        '--title',
        nargs=1,
        help="title for new document",
        dest="discpushnewtitle"
    )
    parser_push_discourse.add_argument(
        '-k',
        '--cat',
        nargs=1,
        type=int,
        help="category for new document",
        dest="discpushnewcategory"
    )
    parser_push_discourse.add_argument(
        '-c',
        '--cfg',
        nargs=1,
        help="alternate config file with discourse URL & auth params",
        dest="discpushconfig"
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
    ppg_grp.add_argument('-f','--file',nargs=1,help="filename to pull from github",dest="gitfile")
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
        help="filename to pull from discourse",
        dest="discpullfile"
    )
    ppg_grp2.add_argument(
        '-r',
        '--range',
        nargs=2,
        help="-r <start> <end>: pull topics from start to end",
        dest="discpullrange",
        type=int
    )
    ppg_grp3 = parser_pull_discourse.add_mutually_exclusive_group(required=True)
    ppg_grp3.add_argument(
        '-t',
        '--tnum',
        nargs=1,
        help="topic number from which to pull the file",
        dest="discpulltopic",
        type=int
    )
    ppg_grp3.add_argument(
        '-b',
        '--bulk',
        action='store_true',
        help='confirms bulk pull indicated with "-a"',
        dest="discpullbulk"
    )
    parser_pull_discourse.add_argument(
        '-k',
        '--cat',
        nargs=1,
        help="restrict discourse category to CAT",
        dest="discpullcat",
        type=int
    )
    parser_pull_discourse.add_argument(
        '-l',
        '--live',
        action='store_true',
        help="do not pull deleted articles",
        dest="discnodeleted"
    )
    parser_pull_discourse.add_argument(
        '-c',
        '--cfg',
        nargs=1,
        help="alternate config file with discourse URL & auth params",
        dest="discpullconfigfile"
    )
    parser_pull_discourse.add_argument(
        '-j',
        '--json',
        action='store_true',
        help='store topic JSON in "topic.json" (useless with -a)',
        dest="disctopicjson"
    )
    parser_pull_discourse.add_argument(
        '-J',
        '--JSON',
        action='store_true',
        help='store post JSON in "post.json" (useless with -a)',
        dest="discpostjson"
    )

    return parser
