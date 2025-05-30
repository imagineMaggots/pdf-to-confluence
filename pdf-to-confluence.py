import sys
from atlassian import Confluence

confluence = Confluence(
    url=str(sys.argv[1]),
    username=str(sys.argv[2]),
    password=str(sys.argv[3])
)

print("Hello World")
print(str(sys.argv))
