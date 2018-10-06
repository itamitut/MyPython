import os
import re
for filename in os.listdir("."):
    if filename.endswith(".template"):
        outfilename = re.sub(r".template", "", filename)
        with open(filename, 'r') as a, open(outfilename, 'w') as a1:
            for line in a:
                line = re.sub(r'(#.*?#)', 'Новый шаблон', line)
                a1.write(line)
