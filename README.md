# discourse_tools
## Tools to use the discourse API
Work in progress

dcpull.py
 - takes CLI params -t topic_number and -o output_file
 -- topic_number is the number after the /t/ in the discourse doucment URL
 -- output_file is where is stores clean, editable discourse markup or HTML (if the file had HTML in it)
  requires a yaml config file called "dc.yaml" that must contain
    base_url: the entire string that comes before the /t/nnn in your discourse URL
    api_username: your username for the discourse API you're accessing
    api_key: your API key for the discourse API you're accessing
    
    
