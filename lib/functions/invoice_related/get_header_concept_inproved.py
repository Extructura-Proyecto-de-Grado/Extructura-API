import os
import cv2
import pytesseract
from fuzzywuzzy import fuzz

from lib.functions.utils.find_first_character_of_a_string import (
    findFirstCharacterOfAString,
)


def getHeaderConceptImproved(
    key_to_match, file_name_prefix, directory_in_str, invoiceFileName
):
    directory = os.fsencode(directory_in_str)

    max_ratio = 0

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.startswith(file_name_prefix):
            img_file_path = directory_in_str + "/" + filename
            image = cv2.imread(img_file_path)
            ocr_result = pytesseract.image_to_string(
                image, lang="spa", config="--psm 6"
            )
            ocr_result = ocr_result.replace("\n\x0c", "")
            ocr_result = ocr_result.replace("\n", " ")
            substrings = [":", ";", ","]
            key = ocr_result[
                : findFirstCharacterOfAString(ocr_result, *substrings) :
            ].strip()
            ratio = fuzz.ratio(key, key_to_match)
            if ratio > max_ratio:
                max_ratio = ratio
                value = ocr_result[
                    findFirstCharacterOfAString(ocr_result, *substrings) + 1 : :
                ].strip()

    return value
