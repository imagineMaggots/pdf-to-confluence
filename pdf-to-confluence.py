# coding=utf-8
import sys
from atlassian import Confluence

pdf = "Test.pdf"

confluence = Confluence(url=str(sys.argv[1]), username=str(sys.argv[2]), password=str(sys.argv[3]))

print(str(sys.argv))

test = confluence.update_or_create(parent_id=2195457, title="Test", body="Test")
test = confluence.attach_file(filename="pdf-to-confluence/",content=".pdf",name="Test.pdf",title="Test",content_type="application/pdf")
