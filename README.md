# discourse_tools
## Tools to use the discourse API

### dcpull
 - takes CLI params -t topic_number and -o output_file
   - **topic_number** is the number after the /t/ in the discourse doucment URL
   - **output_file** is where dcpull stores clean, editable discourse markup or HTML (if the file has HTML)
 - requires a yaml config file called "/etc/dc.yaml" that must contain
   - **base_url:** the entire string that comes before the /t/nnn in your discourse URL
   - **api_username:** your username for the discourse API you're accessing
   - **api_key:** your API key for the discourse API you're accessing
 - utilizes subprocess.Popen running a curl to retrieve the post_id
   - directly pulling from topics isn't reliable in the discourse API
 - utilizes subprocess.Popen running curl to pull the post by post_id
 
### dcpush
 - takes CLI params -t topic_number and -i input file
   - **topic_number** is the number after the /t/ in the discourse document URL
   - **input_file** is a file containing clean discourse markup to replace current topic contents
 - requires yaml config file as above
 - utilizes subprocess.Popen running a curl to retrieve the post_id
 - utilizes subprocess.check_output to overwrite input file contents on topic
 - note that, for reasons yet unknown, overwriting a post fails if the raw string size is less than 9000 characters
   - this is handled by padding the output string with blanks to 9000 characters
   - during the PUT command, the extra spaces are collapsed to one space, so the file is normal when posted,
     both in the discourse markup and in the generated HTML
