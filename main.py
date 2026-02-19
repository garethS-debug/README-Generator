from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from qtoask import question
import time

console = Console()
answers = prompt(question())
content = f"""
            #{answers['title']}
            # Description
            # {answers['description']}
            # Installation
            # {answers['installation']}
            # Usage
            # {answers['usage']}
            # Licence
            # {answers['licence']}
            # Author Name
            # {answers['author']}
            # Contact Information
            # {answers['contact']}
            """

with Progress() as progress:
    task = progress.add_task("Processing...", total=100)
    for _ in range(10):
        time.sleep(0.3)
        progress.update(task, advance=10)
        
console.print("[bold green]Task Complete![/bold green] ✅")




# # Display a formatted message with Rich
# console.print(
#     f"Hello, [bold {answers['title']}] {answers['description']}![/bold {answers['description']}]"
# )
