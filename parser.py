from lxml import etree


class XmlParser(object):
    def __init__(self, document):
        self.document = document

    def parse(self):
        data = {}
        categories_dict = {}
        tree = etree.parse(self.document)
        root = tree.getroot()
        for shop in root.findall('shop'):
            for categories in shop.findall('categories'):
                for category in categories.findall('category'):
                    categories_dict[category.attrib['id']] = category.text
            for offers in shop.findall('offers'):
                for offer in offers.findall('offer'):
                    offer_id = 'yml-offer_{0}'.format(offer.attrib['id'])
                    name = offer.find('name')
                    if name is not None:
                        name = name.text
                    else:
                        name = '{0} {1}'.format(offer.find('vendor').text, offer.find('model').text)
                    category = offer.find('categoryId').text
                    price = offer.find('price').text
                    data[offer_id] = '{0}: {1} : {2}'.format(categories_dict[category], name, price)
        return data
