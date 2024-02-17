import argparse
import sys
import re
import json
parser = argparse.ArgumentParser(description='Process some markdown to pandoc listings compatible listings')
parser.add_argument('fin', type=str, help='markdownfile to process')
parser.add_argument('fout', type=str, help='.tex output file')

file_to_export = "./thesis_references_alias.tex"
file_to_open = "./thesis_document.tex"


try:
#    args = parser.parse_args()

#    if args.fin:
#        file_to_open = args.fin
    print(file_to_open)


 #   if not args.fout:
 #       file_to_export = args.fout
    print(file_to_open)
except Exception as e:
    pass





text_content:str = ""
lines : [str] = []

out_lines : [str] = []
with open(file_to_open,'r') as file:
    text_content = file.read()
    #lines = text_content.split('\n')
    
    
    regex_pattern = r"\\customcite{(\w+)}"
    regex = re.compile(regex_pattern, re.IGNORECASE) # FOR CLOSING CASE ```

    groups = re.findall(regex, text_content)
    unique_groups = list(set(groups))
    # SCAN FOR \customcite{ AND PARSE \customcite{xXx}
    # GET GROUPS
    for idx, gr in enumerate(unique_groups):
        
        cite: str = gr #"SB2010"
        cite_text: str = gr #"SB2010"
        #xout_lines.append("\\"+"citefield{"+ "{}".format(cite) + "}{"+ "{}".format('shortauthor') + "}")
        out_lines.append("\\"+"defcitealias{"+ "{}".format(cite) + "}{"+ "{}".format(cite_text) + "}")
        out_lines.append("\n")





with open( file_to_export, 'w+') as writer:
    writer.write("\n".join(out_lines))