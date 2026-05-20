import os
import allure

from datetime import datetime


def take_screenshot(driver, name):

    folder = "reports/screenshots"

    os.makedirs(
        folder,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    file_path = (
        f"{folder}/{name}_{timestamp}.png"
    )

    driver.save_screenshot(
        file_path
    )

    # ATTACH TO ALLURE REPORT

    allure.attach.file(
        file_path,
        name=name,
        attachment_type=allure.attachment_type.PNG
    )

    print(
        f"Screenshot Saved: {file_path}"
    )