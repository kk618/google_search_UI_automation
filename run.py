import pytest
import time
import subprocess
import os


if __name__ == '__main__':
    tmp = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    pytest.main(['-s','./tests/test_google_search.py',f'--alluredir=report/{tmp}/json/', '--reruns=0', '--reruns-delay=1'])
    cmd = f'allure generate report/{tmp}/json/ -o report/{tmp}/html/'
    os.popen(cmd)
    subprocess.call(cmd, shell=True)