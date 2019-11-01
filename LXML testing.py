from lxml.etree import tostring
from lxml import etree
from lxml.builder import E
from infrabel_utils.db import get_postgres_cache_engine
from infrabel_utils import db
import pandas as pd
# print(tostring(E.results(E.Country(name='Germany',Code='DE',Storage='Basic',Status='Fresh',Type='Photo')), pretty_print=True, xml_declaration=True, encoding='UTF-8'))

from IPython.display import display, HTML
display(HTML(data="""
<style>
    div#notebook-container    { width: 95%; }
    div#menubar-container     { width: 65%; }
    div#maintoolbar-container { width: 99%; }
</style>
"""))

# Create the root element

page= etree.Element('results')

# Make a new document tree

doc = etree.ElementTree(page)

# Add the subelements

pageElement = etree.SubElement(page, 'Country', name='Germany', Code='DE', Storage='Basic')
pageElement2 = etree.SubElement(page, 'Country', name='France', Code='FR', Storage='Basic')
pageElement3 = etree.SubElement(page, 'Country', name='Belgium', Code='BE', Storage='Basic')
pageElement4 = etree.SubElement(page, 'Country', name='England', Code='EN', Storage='Heavy')
pageElement5 = etree.SubElement(page, 'Country', name='Scotland', Code='SCO', Storage='Cool')
pageElement5 = etree.SubElement(page, 'Country', name='United States', Code='US', Storage='Hidden & Dangerous')


# For multiple attributes, use as shown above.


# Save to XML file

# outFile = open('output.xml','w')
doc.write('output.xml', xml_declaration=True, encoding='utf-8',pretty_print=True)

import xml.etree.cElementTree as et
parsedXML = et.parse('output.xml')

for node in parsedXML.getroot():
    name = node.attrib.get('name')
    code = node.attrib.get('Code')
    storage = node.attrib.get('Storage')
    print(name, code, storage)
	
Shelters.head().to_xml('test.xml')