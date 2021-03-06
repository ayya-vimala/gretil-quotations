import sys
import re
import csv

def process_head(head,a_string):
    result_string = "<tr><td style=\"word-wrap: break-word\" valign=\"top\" width=\"1000\"><div style=\"width:500px;\">" + a_string + head.strip() + "</div></td>"
    return result_string

    
def process_quote(quote):
    result_string = "<td style=\"word-wrap: break-word\" valign=\"top\">"
    quote = quote.split("#")
    if len(quote) > 1:
        quote_name = ""
        m = re.search("^([^.]+)",quote[1])
        if m:
            if len(m.group(0)) > 5:
                quote_name = m.group(0) + ".html"
                quote_name = quote_name.replace("_combined","")
        if len(quote) == 4:
            result_string += "<a target=\"_blank\" href=\"" + quote_name + "#" + quote[2] +"\">" + quote[1] + "</a> " + quote[2] + " (" + quote[0] + "): <br/>" + quote[3] .strip() + "</td>"
        return result_string
    else:
        return ""
filename = sys.argv[1]
f1 = open(filename,'r')
file_csv = csv.reader(f1)
output = "<html><head><meta charset=\"UTF-8\"></head><table style=\"width:100%\" border=\"1\">\n"
output += "<br/><a href=\"gretil-original/" + filename[:-3] + "htm\">View original HTML file with complete header information</a><br/>"
ladder = []
last_number = 0
last_line = []
last_a_string = ""
for line in file_csv:
    if len(line) > 1:
        current_number = int(line[0])
        a_string = ""
        if last_number == 0:
            last_number = current_number
            last_line = line
        for i in range(last_number,current_number):
            a_string += "<a id=" + str(i) + "></a>"
        output += process_head(last_line[1],a_string)
        if len(line) > 2:
            for quote in last_line[2:22]:
                output += process_quote(quote)
        output += "</tr>\n"
        last_number = current_number
        last_line = line
output = output + "</table></html>"
with open(filename[:-3] + "html", "w") as text_file:
    text_file.write(output)

