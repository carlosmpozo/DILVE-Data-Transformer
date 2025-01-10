import xml.etree.ElementTree as ET

def parse_onix_xml(xml_data):
    root = ET.fromstring(xml_data)
    books = []

    for product in root.findall(".//Product"):
        book = {
            "ISBN": product.findtext("ProductIdentifier/IDValue"),
            "Title": product.findtext("DescriptiveDetail/TitleDetail/TitleElement/TitleText"),
            "Publisher": product.findtext("PublishingDetail/Publisher/PublisherName"),
            "PublicationDate": product.findtext("PublishingDetail/PublishingDate/Date"),
        }
        books.append(book)

    return books

