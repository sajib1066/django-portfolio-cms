# MakePortfolio
## Create Your Own Portfolio

## How To Setup On Linux
1. Clone This Project `git clone https://github.com/sajib1066/makeportfolio.git`
2. Go to Project Directory `cd makeportfolio`
3. Create a Virtual Environment `python3 -m venv env`
4. Activate Virtual Environment `source env/bin/activate`
5. Install Requirements Package `pip install -r requirements.txt`
6. Migrate Database `python manage.py migrate`
7. Create Super User `python manage.py createsuperuser`
8. Finally Run The Project `python manage.py runserver`

## Some Initial Setup Before Use
1. After Login Admin Panel Go To this url `http://127.0.0.1:8000/admin/theme/theme/add/` and add two theme like that.
Make sure data is same as image.
### Add Theme 1
![theme-1-add](https://user-images.githubusercontent.com/39632170/84584676-148e8c80-ae29-11ea-9b6b-4fb8cc88642b.png)
### Add Theme 2
![theme-2-add](https://user-images.githubusercontent.com/39632170/84584678-148e8c80-ae29-11ea-95f9-08a0f78c8626.png)

2. Add Portfolio Category
Go to this url `http://127.0.0.1:8000/admin/portfolio_item/portfoliocategory/add/` and some portfolio category.

After Setup You can use it easily.

If you found some issue to setup then feel free to contact me.
[Facebook](https://www.facebook.com/sajib1066/)
