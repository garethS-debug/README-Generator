def question():
    # get user inputs
    return [
        {"type": "input", "name": "title", "message": "What is your project title?"},
        {"type": "input", "name": "description", "message": "What is the description?"},
        {"type": "input", "name": "installation", "message": "What is the instructions?"},
        {"type": "input", "name": "usage", "message": "What is the Usage Information?"},
        {"type": "list", "name": "licence", "message": "Choose Licenece?", "choices": 
         ["MIT", "Apache-2.0", "GPL-3.0", "None"],}
    ]
