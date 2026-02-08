import sys
import os
from datetime import datetime

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def pytest_configure(config):
    """
    Adds a timestamp to the HTML report filename.
    """
    if hasattr(config.option, 'htmlpath'):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        report_dir = os.path.dirname(config.option.htmlpath)
        report_name = f"report_{timestamp}.html"
        config.option.htmlpath = os.path.join(report_dir, report_name)
