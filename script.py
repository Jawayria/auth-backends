import subprocess

bash_command = 'semantic-release print-version'
process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)