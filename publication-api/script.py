# conda env create -f environment.yml
# conda env update -f environment.yml
from dep_pubs import DepartmentPublications
from writers import BibtexPublicationWriter, MarkdownPublicationWriter
from config import department, bibtex_elements, markdown_elements
import sys
import traceback

try:
    d = DepartmentPublications(department, bibtex_elements, markdown_elements)
    d.find_department_publications()
    md = MarkdownPublicationWriter(d)
    bib = BibtexPublicationWriter(d)
    bib.export()
    md.export()
except:
    traceback.print_exc()
    # Useful for bash scripting (run until exit code = 0)
    sys.exit(1)
