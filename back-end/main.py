from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, Float, Date, Text
from datetime import date
from sqlalchemy import func

engine = create_engine("sqlite:///tally.db", echo=True)
Base = declarative_base()


class Transactions(Base):

    __tablename__ = "table1"

    id = Column(Integer, primary_key=True)
    date = Column('date', Text)
    type = Column('type', Text)
    amount = Column('amount', Float, default=0.0)
    detail = Column('detail', Text)

    @classmethod
    def write_to_db(self, date, type, amount, detail):
        Session = sessionmaker(bind=engine)
        session = Session()

        session.add(self(date=date, type=type, amount=amount, detail=detail))

        session.commit()
        session.close()

    @classmethod
    def read_from_db(self, column_name=None):
        Session = sessionmaker(bind=engine)
        session = Session()

        if column_name:
            values = session.query(getattr(self, column_name)).all()
        else:
            values = session.query(self).all()

        session.close()
        return values

    @classmethod
    def sum_of_amount(self):
        Session = sessionmaker(bind=engine)
        session = Session()

        amounts = session.query(func.sum(self.amount)).scalar()
        session.close()
        if not amounts:
            return 0
        return amounts

    @classmethod
    def sum_of_amount_by_type(self, type=None):
        Session = sessionmaker(bind=engine)
        session = Session()

        if type == None:
            amounts = session.query(func.sum(self.amount)).scalar()
        elif type == "expense":
            amounts = session.query(func.sum(self.amount)
                                    ).filter(self.amount < 0).scalar()
        elif type == "income":
            amounts = session.query(func.sum(self.amount)
                                    ).filter(self.amount > 0).scalar()

        session.close()
        return amounts

    @classmethod
    def delete_from_db(self, id):
        Session = sessionmaker(bind=engine)
        session = Session()

        session.query(self).filter_by(id=id).delete()
        session.commit()
        session.close()

    @classmethod
    def update_db(self, id, date, type, amount, detail):  # modify any transactions
        Session = sessionmaker(bind=engine)
        session = Session()

        session.query(self).filter_by(id=id).update(
            {self.date: date, self.type: type, self.amount: amount, self.detail: detail})

        session.commit()
        session.close()

    @classmethod
    def clear_all(self):
        Session = sessionmaker(bind=engine)
        session = Session()

        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        session.commit()
        session.close()


Base.metadata.create_all(engine)
