from sqlalchemy.exc import SQLAlchemyError


class UnitOfWork:
    def __init__(self, session_factory):
        self.session_factory = session_factory
        self.session = None

    def __enter__(self):
        self.session = self.session_factory()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            try:
                if exc_type is not None:
                    self.session.rollback()
                else:
                    try:
                        self.session.commit()
                    except SQLAlchemyError:
                        self.session.rollback()
                        raise
            finally:
                self.session.close()

    def commit(self):
        try:
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def rollback(self):
        self.session.rollback()

    @property
    def db(self):
        return self.session
