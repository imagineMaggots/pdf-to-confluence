# coding=utf-8
import sys
from atlassian import Confluence

pdf = "Test.pdf"

confluence = Confluence(url=str(sys.argv[1]), username=str(sys.argv[2]), password=str(sys.argv[3]))

print(str(sys.argv))

test = confluence.update_or_create(parent_id=2195457, title="Test", body="")
page = confluence.get_page_id(space="PDFTOCONFL", title = "Test")

print(str(page))
test = confluence.attach_file(filename="./Test.pdf",name="Test.pdf",page_id=page,content_type="application/pdf")

attachment = "attachments/"+str(page)+"/Test.pdf"

appending = f"""<p>
  <h2>Link zur PDF</h2>
  <ac:link>
    <ri:attachment ri:filename="Test.pdf"/>
  </ac:link>

  <h2>Eingebettete PDF</h2>
  <object data="{attachment}" type="application/pdf" width="100%" height="500px">
      <p>Unable to display PDF file.</p>
  </object>
  
</p>"""

confluence.append_page(page, "Test", appending)
