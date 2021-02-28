import csv
import logging
import xml.sax

from lxml import etree

logger = logging.getLogger()


class XMLToCSVConverter():
    FIELDNAMES = ['Id', 'FullNm', 'ShrtNm', 'ClssfctnTp', 'NtnlCcy', 'Issr']

    def __init__(self, source_path, destination_path):
        self.source_path = source_path
        self.destination_path = destination_path

    @property
    def context(self):
        context = etree.iterparse(
            self.source_path, events=('start', 'end',),
            tag='{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}TermntdRcrd'
        )

        return context

    def remove_namespace(self, element):
        for elem in element.findall('.//'):
            elem.tag = etree.QName(elem.tag).localname

        return element

    def get_data(self, element):
        element = self.remove_namespace(element)
        row = {}

        for elem in element.findall('./FinInstrmGnlAttrbts/'):
            logger.debug("Element : {0} Tag : {1}".format(elem, elem.tag))

            if elem.tag == 'Id':
                row['Id'] = elem.text

            elif elem.tag == 'FullNm':
                row['FullNm'] = elem.text

            elif elem.tag == 'ShrtNm':
                row['ShrtNm'] = elem.text

            elif elem.tag == 'ClssfctnTp':
                row['ClssfctnTp'] = elem.text

            elif elem.tag == 'NtnlCcy':
                row['NtnlCcy'] = elem.text

        try:
            row["Issr"] = element.find('./Issr').text

        except AttributeError:
            pass

        return row

    def convert(self):
        with open(self.destination_path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.FIELDNAMES)
            writer.writeheader()

            for event, elem in self.context:
                data = self.get_data(elem)
                print(data)
                writer.writerow(data)

        logger.info("Conversion successful {}".format(self.destination_path))
