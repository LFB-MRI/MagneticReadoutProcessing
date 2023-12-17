import argparse
import sys
import re
import json
parser = argparse.ArgumentParser(description='Process some markdown to pandoc listings compatible listings')
parser.add_argument('file', type=str, help='markdownfile to process')
args = parser.parse_args()

#file_to_open: str = "./thesis_document_tmp.md"
file_to_open = args.file

if not args.file:
    sys.exit(0)
print(file_to_open)







text_content:str = ""
lines : [str] = []
with open(file_to_open,'r') as file:
    text_content = file.read()
    lines = text_content.split('\n')
    
    
    
    regex_end = re.compile(r"^[\s]*```[\s]*$", re.IGNORECASE) # FOR CLOSING CASE ```
    regex_simple = re.compile(r"^[\s]*```([a-z0-9]*)([\s][{].*[}])*[\s]*$") # FOR SIMPLE CASES ```bash and ```php
    #regex_json = re.compile(r"[\s]*([A-Za-z0-9]*)[=]([\"][^\"]*)[\"]")
    # ```bash  => ~~~ { .php }
    for idx, line in enumerate(lines):
            result = regex_simple.search(lines[idx])
            #lines[idx] = regex_simple.sub("~~~", lines[idx])
            if result:
                gres = result.groups(1)
                if len(gres) > 0 and len(gres[0]) > 0:
                    print(gres[0])

                    if len(gres) > 1 and len(str(gres[1])) > 1: # FOR COMPLEX
                        json_str = str(gres[1]).replace("{", "").replace("}", "")
                        # CONSTRUCT NEW LINE ~~~ { .<language> caption="XYZ" test="123" }
                        lines[idx] = '~~~ § {} {} $'.format(".{}".format(gres[0]), json_str).replace("§", "{").replace("$", "}")
                        print(lines[idx])
                    else:
                        # CONSTRUCT NEW LINE ~~~ { .<language> }
                        lines[idx] = '~~~ § .{} $'.format(gres[0]).replace("§", "{").replace("$", "}")

                else:
                     lines[idx] = regex_end.sub("~~~", lines[idx])
 


    # ```  => ~~~
    #for idx, line in enumerate(lines):
    #        lines[idx] = regex_end.sub("~~~", lines[idx])



with open( file_to_open + ".listings", 'w+') as writer:
    writer.write("\n".join(lines))