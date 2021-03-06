import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, nullable=True)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, nullable=True)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')

    def __repr__(self):
        return ' '.join([str(self.team_leader), self.job, str(self.work_size), self.collaborators,
                         str(self.start_date), str(self.end_date), str(self.is_finished)])
