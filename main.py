from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from qtoask import question

# console = Console()
answers = prompt(question())
content = f"""
            #{answers['title']}
            # Description
            # {answers['description']}
            """



# # Display a formatted message with Rich
# console.print(
#     f"Hello, [bold {answers['title']}] {answers['description']}![/bold {answers['description']}]"
# )
