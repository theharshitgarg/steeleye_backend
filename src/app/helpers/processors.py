import logging

from lxml import etree

logger = logging.getLogger()


class XMLProcessor():
    """Custom XML Procesor for the task.

    Attributes
    ----------
    path : str
        path for the source XML file

    Methods
    -------
    remove_namespace()
        Removes the namespace from a tag. 

    get_row_data()
        Prepares the data into dict format.
    """

    def __init__(self, filepath):
        self._path = filepath
    
    @property
    def source_path(self):
        return self._path

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
    
    def _get_data(self, element) -> dict:
        """Process the XML for the required data.

        This function processes the required data.

        Args:
            element ([XML element]): An XML element node

        Returns:
            [dict]: a dict containing extracted values
        """

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
            row["Issr"] = ""

        return row
    
    def get_row_data(self) -> dict:
        """Prepare the data for the caller

        Returns:
            dict: a dict of items processed by this class

        Yields:
            Iterator[dict]: a dict of items processed by this class
        """
        for event, elem in self.context:
            data = self._get_data(elem)
            yield data
