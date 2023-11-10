# Шаблон приложения на Python

```bash
clear
echo -n "App name: python-" && read APP_NAME && APP_NAME="python-"$APP_NAME && 
git clone https://github.com/eldar-safin/python-app-template.git $APP_NAME && cd $_ ; unset APP_NAME && 
python3 -m venv .venv --upgrade-deps && source .venv/bin/activate && 
pip install -r requirements.txt && echo && pip list && echo
```