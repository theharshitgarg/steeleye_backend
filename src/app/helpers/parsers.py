import xml.etree.ElementTree as ET


class XMLParser():
    """Parser for XML file
    """

    def __init__(self):
        self._tree = None
        self._data: str = ""

    def _parse(self, data):
        return data

    def get_first_link(self, path='data/select.xml') -> str:
        """Returns the first download link.

        Args:
            path (str, optional): a valid path to an XML file. Defaults to 'data/select.xml'.

        Returns:
            [str]: a URL if exists, otherwise empty string. 
        """
        root = ET.parse(path)
        result = root.findall('*')[1]
        for i in result.findall(".//doc"):
            if i.findtext('str[@name="file_type"]').upper() == "DLTINS":
                value = i.findtext('str[@name="download_link"]')
                if not value:
                    continue
                else:
                    return value

        return ""
