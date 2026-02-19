from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
from rich.progress import Progress

# get user inputs
questions = [
    {"type": "input", "name": "Project Title", "message": "What is your project title?"},
    {"type": "input", "name": "color", "message": "What is your favorite color?"},
]