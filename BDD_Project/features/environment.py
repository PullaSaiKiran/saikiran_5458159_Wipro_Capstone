import os
import allure

from utils.driver_factory import (
    DriverFactory
)

from utils.logger import (
    logger
)

from utils.screenshot import (
    capture_screenshot
)


# ==================================================
# BEFORE ALL
# ==================================================

def before_all(context):

    context.config_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "config",
        "config.ini"
    )

    logger.info(
        "================================================="
    )

    logger.info(
        "AUTOMATION EXECUTION STARTED"
    )

    logger.info(
        "================================================="
    )


# ==================================================
# BEFORE SCENARIO
# ==================================================

def before_scenario(
        context,
        scenario
):

    logger.info(
        f"Starting Scenario : "
        f"{scenario.name}"
    )

    context.driver = DriverFactory.get_driver(
        context.config_path
    )

    context.driver.maximize_window()


# ==================================================
# AFTER SCENARIO
# ==================================================

def after_scenario(
        context,
        scenario
):

    screenshot_folder = (
        "reports/screenshots"
    )

    os.makedirs(
        screenshot_folder,
        exist_ok=True
    )

    screenshot_path = capture_screenshot(
        context.driver,
        scenario.name
    )

    # ==========================================
    # ATTACH SCREENSHOT TO ALLURE
    # ==========================================

    if os.path.exists(
            screenshot_path
    ):

        allure.attach.file(

            screenshot_path,

            name="Screenshot",

            attachment_type=allure.attachment_type.PNG
        )

    # ==========================================
    # ATTACH LOG FILE
    # ==========================================

    log_path = "logs/automation.log"

    if os.path.exists(
            log_path
    ):

        allure.attach.file(

            log_path,

            name="Execution Logs",

            attachment_type=allure.attachment_type.TEXT
        )

    # ==========================================
    # STATUS
    # ==========================================

    if scenario.status == "failed":

        logger.error(
            f"Scenario FAILED : "
            f"{scenario.name}"
        )

    else:

        logger.info(
            f"Scenario PASSED : "
            f"{scenario.name}"
        )

    context.driver.quit()


# ==================================================
# AFTER ALL
# ==================================================

def after_all(context):

    logger.info(
        "================================================="
    )

    logger.info(
        "TEST EXECUTION COMPLETED"
    )

    logger.info(
        "================================================="
    )