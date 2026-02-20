from PyInquirer import prompt
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from qtoask import Questions
import time

console = Console()
# answers = prompt(question())

class App:
    def run(self):
        answers = prompt(Questions.question())
        

        content = f"""
#{answers['title']}
            
## Description
{answers['description']}
## Installation
{answers['installation']}
## Usage
{answers['usage']}
## Licence
{answers['licence']}
## Author Name
{answers['author']}
## Contact Information
{answers['contact']}
"""

with Progress() as progress:
    task = progress.add_task("Processing...", total=100)
    for _ in range(10):
        time.sleep(0.15)
        progress.update(task, advance=10)
        

with open ("README.md", "w") as readme:
    readme.write(content)

console.print("[bold green]Task Complete![/bold green] ✅")

if __name__ =="__main__":
    App().run()
# # Display a formatted message with Rich
# console.print(
#     f"Hello, [bold {answers['title']}] {answers['description']}![/bold {answers['description']}]"
# )
