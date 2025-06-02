# coding=utf-8
import sys
from atlassian import Confluence

confluence = Confluence(
                            url=str(sys.argv[1]),
                            username=str(sys.argv[2]),
                            password=str(sys.argv[3])
                        )

print(str(sys.argv))

test = confluence.create_page(space="DEMO", title = "Test Titel", body = "Test Körper")

print(test)
