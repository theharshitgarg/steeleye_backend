import os
import zipfile

import requests

from helpers.converters import XMLToCSVConverter
from helpers.parsers import XMLParser
from loggers import logger


def main():
    logger.info("Program started")
    parser = XMLParser()
    link = parser.get_first_link("data/select.xml")

    if not link:
        logger.warning("No link exists")

    response = requests.get(link)

    with open('data/zip/xml_download.zip', 'wb') as output:
        output.write(response.content)

    logger.info("File download successful")

    with zipfile.ZipFile('data/zip/xml_download.zip', 'r') as zip_ref:
        zip_ref.extractall('data/unzip')

    logger.info("File unzipped successful")

    for filename in os.listdir('data/unzip'):
        logger.info(f"Professing file {filename}")

        if filename.endswith(".xml"):
            filepath = os.path.join('data/unzip', filename)
            destination_file = '.'.join(filename.split('.')[:-1]) + '.csv'
            destination_path = os.path.join('data/csv', destination_file)
            converter = XMLToCSVConverter(filepath, destination_path)
            converter.convert()

            logger.info(f"File created at path {destination_path}")

    logger.info('Task completed .... :)')


if __name__ == '__main__':
    main()
