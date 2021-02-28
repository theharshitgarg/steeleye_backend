import csv
import logging


from processors import XMLProcessor

logger = logging.getLogger()


class XMLToCSVConverter():
    """Conerter class for xml to csv.
    
    Attributes
    ----------
    FIELDNAMES: list[str]
        a list of useful output fields
    source_path : str
        a  source XML file path
    destination_path : str
        a file path for CSV file
    _xml_processor: XMLProcessor
        an object that handles XML operations

    Methods
    -------
    convert()
        Converts XML file to CSV
    """

    FIELDNAMES = ['Id', 'FullNm', 'ShrtNm', 'ClssfctnTp', 'NtnlCcy', 'Issr']

    def __init__(self, source_path: str, destination_path: str):
        """
        Parameters
        ----------
        source_path : str
            The source file path
        destination_path : str
            The destination file path
        """

        self.source_path = source_path
        self.destination_path = destination_path
        self._xml_processor = XMLProcessor(source_path)

    def convert(self):
        with open(self.destination_path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.FIELDNAMES)
            writer.writeheader()

            for row in self._xml_processor.get_row_data():
                print(row)
                writer.writerow(row)

        logger.info("Conversion successful {}".format(self.destination_path))
