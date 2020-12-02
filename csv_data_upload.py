from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User
import csv
import pandas as pd
import numpy as np

engine = create_engine('sqlite:///catalogs.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

User1 = User(name=" GOD", email="god@gmail.com")
session.add(User1)
session.commit()

category_df = pd.read_csv('categories.csv')
item_df = pd.read_csv('items.csv', error_bad_lines=False)


categories = category_df[['name', 'ID']]
items = item_df[['name', 'description', 'Category ID']]


for index, category in categories.iterrows():
    category_input = Categories(user_id=1, name=category['name'])
    session.add(category_input)
    session.commit()

    for index, item in items.iterrows():
        if(category['ID'] == item['Category ID']):
            item_input = CategoryItem(
                user_id=1,
                name=item['name'],
                description=item['description'],
                categories=category_input)
            session.add(item_input)
            session.commit()
'''
for index, item in items.iterrows():
    for index, category in categories.iterrows():
        if(category['ID'] == item['Category ID']):
            category_input = Categories(user_id=1, name=category['name'])
            item_input = CategoryItem(
                user_id=1,
                name=item['name'],
                description=item['description'],
                categories=category_input)
            session.add(category_input)
            session.commit()
            session.add(item__input)
            session.commit()'''
