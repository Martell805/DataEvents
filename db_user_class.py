import datetime
import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
import sqlalchemy.orm as orm

from db_session import SqlAlchemyBase
from flask_login import UserMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    date_times = sqlalchemy.Column(sqlalchemy.String, default='0 ' * 372)
    '''january = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='0 ' * 31)
    february = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='0 ' * 29)
    march = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='0 ' * 31)
    april = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='0 ' * 30)
    may = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='0 ' * 31)
    june = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='0 ' * 30)
    july = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='0 ' * 31)
    august = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='0 ' * 30)
    september = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='0 ' * 30)
    october = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='0 ' * 31)
    november = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='0 ' * 30)
    december = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='0 ' * 31)'''

    def __init__(self, id):
        self.id = id
        self.date_times = '0 ' * 372

    def __repr__(self):
        return f'<User> {self.id} {self.date_times}'
