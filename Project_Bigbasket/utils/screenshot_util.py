import os
from datetime import datetime


class ScreenshotUtil:

    @staticmethod
    def capture_screenshot(driver, test_name):

        base_dir = os.path.dirname(os.path.dirname(__file__))

        screenshot_dir = os.path.join(
            base_dir,
            "screenshots"
        )

        os.makedirs(screenshot_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
