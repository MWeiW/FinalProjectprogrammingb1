Wei Wong - HTW Berlin - 15.02.2026.

Hello, this is a RESTful API built using FastAPI.

It allows users to:
- Create tasks
- View all tasks
- View a single task
- Update tasks
- Delete tasks
- Filter tasks by completion status
- View task statistics
- Delete all tasks

## The program uses:

- Python
- FastAPI
- Uvicorn
- JSON Lines file storage

## How to store data?:

Tasks are stored in a text file (`tasks.txt`) using JSON Lines format.
Each line represents one task as a JSON object.

Example:
{"id":1,"title":"get groceries","description":"milk","completed":false}

## How to run the project?

1. Create virtual environment:
   python -m venv venv

2. Activate environment:
   venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run server:
   uvicorn main:app --reload

5. Open Swagger:
   http://127.0.0.1:8000/docs
