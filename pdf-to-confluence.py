# coding=utf-8
import sys
from atlassian import Confluence

root = str(sys.argv[1])
pdf = "Test.pdf"

confluence = Confluence(url=root, username=str(sys.argv[2]), password=str(sys.argv[3]))

print(str(sys.argv))

test = confluence.update_or_create(parent_id=2195457, title="Test", body="")
page = confluence.get_page_id(space="PDFTOCONFL", title = "Test")

print(str(page))
test = confluence.attach_file(filename="./Test.pdf",name="Test.pdf",page_id=page,content_type="application/pdf")

appending = f"""
  <h2>Link zur PDF</h2>
  <ac:link>
    <ri:attachment ri:filename="Test.pdf"/>
  </ac:link>
  <h2>Eingebettete PDF</h2>
  <ac:image>
    <ri:attachment ri:filename="Test.pdf"/>
  </ac:image>
"""
print(appending)

confluence.append_page(page, "Test", appending)
