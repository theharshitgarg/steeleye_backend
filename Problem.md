# Steel EYE Recruitment problem Statement

## Tip

And one final tip: KISS – Keep It Short and Simple. Don’t overcomplicate it, make it simple, efficient, easy to maintain and easy for the user to use.

Brief:

    The requirement needs to be developed in Python 3
    Code should follow pep8 standards and should include pydoc, logging & unit tests
    Please provide github link for review.

## Requirement

    ```
    1. Download the xml from this link
    2. From the xml, please parse through to the first download link whose file_type is DLTINS and download the zip
    3. Extract the xml from the zip.
    4. Convert the contents of the xml into a CSV with the following header:

        FinInstrmGnlAttrbts.Id
        FinInstrmGnlAttrbts.FullNm
        FinInstrmGnlAttrbts.ClssfctnTp
        FinInstrmGnlAttrbts.CmmdtyDerivInd
        FinInstrmGnlAttrbts.NtnlCcy
        Issr

    5. Store the csv from step 4) in an AWS S3 bucket
    6. The above function should be run as an AWS Lambda (Optional)
    ```

## Assessment criteria

    Percentage of requirements satisfied
    How clean the code is - in particular simplicity, adhering to python code style conventions and error handling.
    Follows PEP 8 guidelines
    We expect pydoc for each class and function with optional type hints(nice to have)
    Follows standard logging (no print statements). Logs are essential part of troubleshooting application.
    Unit tests with good code coverage
