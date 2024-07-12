from contextlib import contextmanager

from sqlalchemy.exc import SQLAlchemyError

from app import SessionLocal


@contextmanager
def transactional(func):
    def wrapper(*args, **kwargs):
        db = SessionLocal()
        try:
            result = func(db, *args, **kwargs)
            db.flush()
            db.refresh(result)
            db.commit()
            return result
        except SQLAlchemyError as e:
            db.rollback()
            raise e
        finally:
            db.close()

    return wrapper
