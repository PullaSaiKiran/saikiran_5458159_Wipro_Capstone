import os

from datetime import datetime

from utils.logger import (
    logger
)


def capture_screenshot(
        driver,
        scenario_name
):

    folder = "reports/screenshots"

    os.makedirs(
        folder,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    safe_name = (
        scenario_name
        .replace(" ", "_")
        .replace("/", "_")
    )

    file_path = (
        f"{folder}/"
        f"{safe_name}_{timestamp}.png"
    )

    driver.save_screenshot(
        file_path
    )

    logger.info(
        f"Screenshot saved : "
        f"{file_path}"
    )

    return file_path