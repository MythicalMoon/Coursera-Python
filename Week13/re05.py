import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

# (\S - non-whitespace character)

# (\S+@\S - any nonwhitespacer(-s)followed by '@'into another non whitespace )