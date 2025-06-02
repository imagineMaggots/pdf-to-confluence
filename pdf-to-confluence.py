# coding=utf-8
import sys
from atlassian import Confluence


confluence = Confluence(url=str(sys.argv[1]), username=str(sys.argv[2]), password=str(sys.argv[3]))

print(str(sys.argv))

test = confluence.update_or_create(
    parent_id=None,
    page_id=2195457,
    title="This is the title",
    body="This is the new body",
)

