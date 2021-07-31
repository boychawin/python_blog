# python_blog



pip3 install virtualenv 
python3 -m virtualenv venv


source ./venv/bin/activate
pip3 list

pip install django
django-admin startproject whoisuncle
cd whoisuncle

python3 manage.py runserver 
//สร้าง page
python3 manage.py startapp home
python3 manage.py migrate    

python3 manage.py createsuperuser

UserName : Admin
Password : Admin


./ngrok http 8000


คำสั่งสร้างฐานข้อมูล
python3 manage.py makemigrations
python3 manage.py migrate   
