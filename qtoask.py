
class Questions:

    def question():
    # get user inputs
        return [
        {"type": "input", "name": "title", "message": "What is your project title?", "validate": lambda result: len(result) > 0,
            "invalid_message": "Input cannot be empty.",},
        {"type": "input", "name": "description", "message": "What is the description?", "validate": lambda result: len(result) > 0,
            "invalid_message": "Input cannot be empty.",},
        {"type": "input", "name": "installation", "message": "What is the instructions?", "validate": lambda result: len(result) > 0,
            "invalid_message": "Input cannot be empty.",},
        {"type": "input", "name": "usage", "message": "What is the Usage Information?", "validate": lambda result: len(result) > 0,
            "invalid_message": "Input cannot be empty.",},
        {"type": "list", "name": "licence", "message": "Choose Licenece?", "choices": 
         ["MIT", "Apache-2.0", "GPL-3.0", "None"],},
        {"type": "input", "name": "author", "message": "What is the author name?", "validate": lambda result: len(result) > 0,
            "invalid_message": "Input cannot be empty.",},
        {"type": "input", "name": "contact", "message": "What is the contact info?", "validate": lambda result: len(result) > 0,
            "invalid_message": "Input cannot be empty.",},
        
    ]
