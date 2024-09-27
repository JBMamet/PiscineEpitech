import re
i,s=int(input()),input()
if i:print(i if re.search('[aeiouyAEIOUY]',s)or(i>41)else s)