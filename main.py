from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
from rich.progress import Progress

console = Console()

# get user inputs
questions = [
    {"type": "input", "name": "title", "message": "What is your project title?"},
    {"type": "input", "name": "description", "message": "What is the description?"},
]

answers = prompt(questions)

# Display a formatted message with Rich
console.print(
    f"Hello, [bold {answers['title']}] {answers['description']}![/bold {answers['description']}]"
)
