py -m venv eenv
REM Activate virtual environment
call eenv\Scripts\activate
py -m pip install --upgrade pip

REM Install requirements
pip install -r requirements.txt
