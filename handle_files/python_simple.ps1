New-item -Path 'app' -ItemType Directory
New-item -Path 'tests' -ItemType Directory
New-item -Path 'main.py' -ItemType File
New-item -Path '.gitignore' -ItemType File
python -m venv env
.\env\Scripts\Activate.ps1
git init
pip install telethon
# python -m pip freeze > requirements.txt
pip install requests
pip install python-telegram-bot