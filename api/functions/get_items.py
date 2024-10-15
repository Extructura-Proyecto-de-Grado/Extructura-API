import os
import cv2
import pytesseract

from lib.enums.invoice_type_enum import InvoiceType

from lib.functions.utils.preprocess_image import preprocess_image
from lib.functions.utils.process_image import processImage
from lib.models.invoice_item import Item

from lib.functions.utils.delete_file import delete_file
from lib.functions.utils.process_item_image import processItemImage


# Devuelve el detalle de los productos


def getItems(invoice_type: InvoiceType, imageName: str):
    directory_in_str = "images/temp/items"
    directory = os.fsencode(directory_in_str)

    items = []
    printXYWHIteration = 0

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.startswith("item"):
            printXYWHIteration = printXYWHIteration + 1
            processImage(
                imageToProcessPath=("images/temp/items/" + filename),
                rectDimensions=(7, 250),
                boxWidthTresh=5,
                boxHeightTresh=0,
                outputImagePrefix="value",
                folder="images/temp/items/values",
                reverseSorting=True,
            )

            directory_in_str = "images/temp/items/values/"
            directory = os.fsencode(directory_in_str)

            valuesStr = []

            for file in os.listdir(directory):
                filename = os.fsdecode(file)
                img_file_path = "images/temp/items/values/" + filename
                image = cv2.imread(img_file_path)
                ocr_result = pytesseract.image_to_string(
                    image, lang="spa", config="--psm 6"
                )
                ocr_result = ocr_result.replace("\n\x0c", "")
                ocr_result = ocr_result.replace("\n", " ")
                valuesStr.append(ocr_result)
                # Elimino la imágen al terminar
                delete_file(img_file_path)
            if invoice_type == InvoiceType.A:
                if len(valuesStr) == 8:
                    item = Item(
                        cod="",
                        title=valuesStr[0],
                        amount=valuesStr[1],
                        measure=valuesStr[2],
                        unit_price=valuesStr[3],
                        discount_perc=valuesStr[4],
                        subtotal=valuesStr[5],
                        vat_fee=valuesStr[6],
                        subtotal_inc_fees=valuesStr[7],
                    )
                else:  # ==9
                    item = Item(
                        cod=valuesStr[0],
                        title=valuesStr[1],
                        amount=valuesStr[2],
                        measure=valuesStr[3],
                        unit_price=valuesStr[4],
                        discount_perc=valuesStr[5],
                        subtotal=valuesStr[6],
                        vat_fee=valuesStr[7],
                        subtotal_inc_fees=valuesStr[8],
                    )
            else:
                if len(valuesStr) == 7:
                    item = Item(
                        cod="",
                        title=valuesStr[0],
                        amount=valuesStr[1],
                        measure=valuesStr[2],
                        unit_price=valuesStr[3],
                        discount_perc=valuesStr[4],
                        discounted_subtotal=valuesStr[5],
                        subtotal=valuesStr[6],
                    )
                else:  # ==8
                    item = Item(
                        cod=valuesStr[0],
                        title=valuesStr[1],
                        amount=valuesStr[2],
                        measure=valuesStr[3],
                        unit_price=valuesStr[4],
                        discount_perc=valuesStr[5],
                        discounted_subtotal=valuesStr[6],
                        subtotal=valuesStr[7],
                    )

            items.append(item)
        else:
            continue
    return items
