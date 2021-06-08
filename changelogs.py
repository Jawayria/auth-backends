import subprocess
import sys
from datetime import date
import fileinput

# Save new changelogs in temp.md
changelogs_cmd = "semantic-release changelog"
process = subprocess.Popen(changelogs_cmd.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
output = "## [" + sys.argv[1] + "] - " + str(date.today()) + "\n"+output.decode("utf-8")

file = open('temp.md', 'w')
file.writelines(output)
file.close()

# Convert the changelogs to rst
pandoc_cmd = "pandoc temp.md -f markdown_strict -t rst -o temp.rst"
process = subprocess.Popen(pandoc_cmd.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

# append the changelogs in CHANGELOG.rst
file = open('temp.rst', 'r')
changelogs = file.read()

for line in fileinput.FileInput("CHANGELOG.rst", inplace=1):
    if ".. <New logs>" in line:
        line = line.replace(line, line+"\n"+changelogs)
        print(line)
    else:
        print(line.split('\n')[0])
