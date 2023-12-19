# brodota-bot

pip install -r .\requirements.txt
pyinstaller --onedir --add-data "data/image/*.png:data/image" --add-data "data/image/hero/*.png:data/image/hero" --add-data "data/image/hero/item/*.png:data/image/item" main.py 