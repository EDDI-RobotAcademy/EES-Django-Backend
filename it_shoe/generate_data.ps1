Get-ChildItem -Path "./*/migrations/*.py" -Exclude "__init__.py" | Remove-Item -Force
Get-ChildItem -Path "./*/migrations/*/*.pyc" | Remove-Item -Force

python manage.py makemigrations
python manage.py migrate

python manage.py runscript scripts.create_sample.create_accounts
python manage.py runscript scripts.create_sample.withdraw_accounts
python manage.py runscript scripts.create_sample.create_login_histories
python manage.py runscript scripts.create_sample.create_products
python manage.py runscript scripts.create_sample.create_orders
python manage.py runscript scripts.extract_sample.extract_orders
python manage.py runscript scripts.extract_sample.extract_user_info 
python manage.py runscript scripts.extract_sample.extract_date_info

