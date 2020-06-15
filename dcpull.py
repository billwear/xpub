#!python3
# python script to pull a specific discourse post by topic number
#
# you need to supply parameters base_url, api_username, and api_key
# in a file in cwd called "dc.yaml"
#
# you supply -t topic_number and -o output_file on the command line
#
# output_file will contain cleaned, editable discourse markup
# or HTML if the original file contained HTML
#
import subprocess, json, sys, getopt
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def main(argv):
    topic = ''
    textfile = ''
    dash_t = False
    dash_o = False

    try:
        opts, args = getopt.getopt(argv,"ht:o:",["topic=","ofile="])
    except getopt.GetoptError:
        print('dcpull.py -t <topicnumber> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('dcpull.py -t <topicnumber> -o <outputfile>')
            sys.exit()
        elif opt in ("-t", "--topic"):
            dash_t = True
            topic = arg
        elif opt in ("-o", "--ofile"):
            dash_o = True
            textfile = arg

    if(dash_t == False):
        print('missing required option "-t"')
        print('dcpull.py -t <topicnumber> -o <outputfile>')
        sys.exit(3)
    if(dash_o == False):
        print('missing required option "-o"')
        print('ecpull.py -t <topicnumber> -o <outputfile>')
        sys.exit(4)

    config_file = open("dc.yaml","r")
    config_data = load(config_file, Loader=Loader)
    
    f = open('topic.pull', 'w')
    proc = subprocess.Popen([
        'curl',
        '-X',
        'GET',
        '-H',
        'Api-Key: ' + config_data['api_key'],
        '-H',
        'Api-Username: ' + config_data['api_username'],
        '-H',
        'Content-Type: application/json',
        config_data['base_url'] + '/t/{'+str(topic)+'}.json'],
        stdout=subprocess.PIPE
    )
    output = proc.stdout.read()
    topic_json = json.loads(output)
    post_id = topic_json['post_stream']['posts'][0]['id']
    f2 = open('post.pull', 'w')
    proc2 = subprocess.Popen([
        'curl',
        '-X',
        'GET',
        '-H',
        'Api-Key: ' + config_data['api_key'],
        '-H',
        'Api-Username: ' + config_data['api_username'],
        '-H',
        'Content-Type: application/json',
        config_data['base_url'] + '/posts/{'+str(post_id)+'}.json'],
        stdout=subprocess.PIPE
    )
    output2 = proc2.stdout.read()
    post_json = json.loads(output2)
    raw = post_json['raw']
    f = open(textfile, "w")
    f.write(raw)

if __name__ == "__main__":
    main(sys.argv[1:])


