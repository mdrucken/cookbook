import os
from lxml import etree

with open("src/recipeml.xsd", 'r') as file:
    schema_content = file.read()
    xsd_doc = etree.XML(schema_content)
    schema = etree.XMLSchema(xsd_doc)


FOLDER = "src"
for filename in os.listdir(FOLDER):
    file_path = os.path.join(FOLDER, filename)
    with open(file_path, 'r') as file:
        xml_content = file.read()
        try:
            xml_doc = etree.XML(xml_content)
        except ValueError as ve:
            print(f"Failed to read {file_path}\n{ve}")
            continue
        valid = schema.validate(xml_doc)
        if not valid:
            print(f"XML file {file_path} is NOT valid against the provided XSD schema.")
            # Print validation errors
            for error in schema.error_log:
                print(error)