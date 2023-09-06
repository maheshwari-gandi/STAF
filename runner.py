import logging
import os
import subprocess

from sys import stdout, stderr
from Utilities.config import obj_read_config
from robot import run
from Utilities.custom_logger import generate_logs


class Runner:
    @staticmethod
    def check_result_dir():
        """
        checks
        result
        :return:
        """
        proj = os.path.dirname(os.path.abspath(__file__))
        result_directory = os.path.join(proj, "results")
        if not (os.path.exists(result_directory) and os.path.isdir(result_directory)):
            os.makedirs(proj + r'\Results')
        logs_directory = os.path.join(result_directory, "Logs")
        print(logs_directory)
        if not (os.path.exists(logs_directory) and os.path.isdir(logs_directory)):
            os.makedirs(logs_directory)
        return logs_directory



    @staticmethod
    def run_robot(script,test_file):
        allure_result = os.path.abspath('Results/allure')
        test_suite = os.path.join(script, test_file).replace("/", "\\")
        if os.path.exists(test_suite):
            report_dir = os.path.join("Results",test_file)
            logging.info("Running %s testcase file",test_file)
            run(test_suite,
                outputdir=report_dir,
                stderr=stderr,
                stdout=stdout,
                listener='allure_robotframework;' + allure_result,
                )

    @staticmethod
    def generate_test_report():
        allure_result = os.path.abspath('results/allure')
        p = subprocess.Popen("allure serve " + allure_result,
                             stdout=subprocess.PIPE,
                             shell=True,
                             stderr=stderr)

        flag = 1
        while flag != 0:
            flag = int(input("enter '0' to end process  "))
            if flag == 0:
                p.kill()

if __name__ == '__main__':
    dir = Runner.check_result_dir()
    generate_logs(dir)
    test_case_json = r'C:\Users\GANMAHES\RobotPlatform\select_file.json'
    script = os.path.abspath('TestSuites/Facebook/TestCasesRobot')
    try:
        test_file = obj_read_config.read_data(test_case_json,"file_to_be_run")
        suite_file = os.path.join(script, test_file).replace("/", "\\")
        if os.path.exists(suite_file):
            logging.info("This execution runs " + test_file)
            Runner.run_robot(script,test_file)
    except (IOError, FileNotFoundError, FileExistsError)as _e_:
        logging.exception(_e_)

    Runner.generate_test_report()
