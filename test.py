import tempfile
print(tempfile.gettempdir())




import re
print(re.match('\\d{3}[-]\\d{8}','088-13169171',flags=0))

print(re.match('^\d{15}|\d{18}$','3960128052123454'))