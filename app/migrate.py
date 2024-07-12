import os

from dotenv import load_dotenv


def main():
    # Load environment variables from .env
    load_dotenv()

    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("DATABASE_URL is not set in environment variables")

    # Set the environment variable for Alembic
    os.environ['DATABASE_URL'] = database_url

    # Run Alembic migrations
    from alembic.config import Config
    from alembic import command

    alembic_cfg = Config(os.path.join(os.path.dirname(__file__), '../alembic.ini'))
    alembic_cfg.set_main_option('sqlalchemy.url', database_url)

    command.upgrade(alembic_cfg, "head")


if __name__ == "__main__":
    main()
