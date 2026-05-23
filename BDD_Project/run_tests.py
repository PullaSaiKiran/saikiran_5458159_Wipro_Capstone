import os
import shutil
import subprocess

from datetime import datetime

from utils.logger import LogGen


# ==================================================
# LOGGER
# ==================================================

logger = LogGen.loggen()

# ==================================================
# EXECUTION START
# ==================================================

timestamp = datetime.now().strftime(
    "%Y%m%d_%H%M%S"
)

logger.info(
    "========================================"
)

logger.info(
    "AUTOMATION EXECUTION STARTED"
)

logger.info(
    "========================================"
)

# ==================================================
# CLEAN OLD ALLURE RESULTS
# ==================================================

if os.path.exists(
    "reports/allure-results"
):

    logger.info(
        "Deleting old allure-results folder"
    )

    shutil.rmtree(
        "reports/allure-results"
    )

# ==================================================
# CLEAN OLD ALLURE REPORT
# ==================================================

if os.path.exists(
    "reports/allure-report"
):

    logger.info(
        "Deleting old allure-report folder"
    )

    shutil.rmtree(
        "reports/allure-report"
    )

# ==================================================
# CREATE REQUIRED FOLDERS
# ==================================================

os.makedirs(
    "reports/allure-results",
    exist_ok=True
)

os.makedirs(
    "reports/allure-report",
    exist_ok=True
)

os.makedirs(
    "reports/screenshots",
    exist_ok=True
)

os.makedirs(
    "logs",
    exist_ok=True
)

# ==================================================
# RUN BEHAVE WITH ALLURE FORMATTER
# ==================================================

logger.info(
    "Starting Behave Test Execution"
)

behave_status = subprocess.run(

    "behave "
    "-f allure_behave.formatter:AllureFormatter "
    "-o reports/allure-results",

    shell=True
)

logger.info(
    f"Behave Execution Completed "
    f"with status code : "
    f"{behave_status.returncode}"
)

# ==================================================
# GENERATE ALLURE HTML REPORT
# ==================================================

logger.info(
    "Generating Allure HTML Report"
)

allure_generate_status = subprocess.run(

    "allure generate reports/allure-results "
    "-o reports/allure-report --clean",

    shell=True
)

logger.info(
    f"Allure Report Generated "
    f"with status code : "
    f"{allure_generate_status.returncode}"
)

# ==================================================
# OPEN ALLURE REPORT
# ==================================================

logger.info(
    "Opening Allure Report"
)

subprocess.run(

    "allure open reports/allure-report",

    shell=True
)

# ==================================================
# EXECUTION END
# ==================================================

logger.info(
    "AUTOMATION EXECUTION COMPLETED"
)

logger.info(
    "========================================"
)