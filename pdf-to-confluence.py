# coding=utf-8
import sys
from atlassian import Confluence

pdf = "Test.pdf"

confluence = Confluence(url=str(sys.argv[1]), username=str(sys.argv[2]), password=str(sys.argv[3]))

print(str(sys.argv))

test = confluence.update_or_create(parent_id=2195457, title="Test", body="Test")

page = confluence.get_page_id(space="PDFTOCONFL", title = "Test")

print(str(page))

test = confluence.attach_file(filename="./Test.pdf",name="Test.pdf",page_id=page,content_type="application/pdf")

appending = f"""<p>
  <ac:link>
    <ri:attachment ri:filename="{Test.pdf}"/>
  </ac:link>
</p>"""

confluence.append_page(page, "Test", appending)
