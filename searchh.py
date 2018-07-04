lorem_text ="lorem is a big boy having guts in his personality"
import re
found= re.search("is.*in",lorem_text)
print(found)
#search in lib search object found match-is the first half output

print(found.start)