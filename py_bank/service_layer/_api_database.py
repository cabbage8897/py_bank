"""Code for database access (also creates some dummy data)."""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker

from ._orm import metadata, start_mappers


def create_db_session(bank_name: str) -> Session:
    """Create db session for a bank.

    Args:
        bank_name (str): Bank name
    """

    engine = create_engine(f"sqlite:///{bank_name}.db", convert_unicode=True)
    metadata.create_all(engine)
    start_mappers()
    db_session = scoped_session(sessionmaker(bind=engine))
    return db_session


def add_data_bank_1(db_session: Session):
    """Add data for bank 1.

    Args:
        db_session (Session): Database sql alchemy session.
    """

    # Adding data
    db_session.execute(
        "INSERT INTO Accounts (account_owner, account_id, balance)" " VALUES ('Luke', 1, 1230.30)"
    )
    db_session.execute(
        "INSERT INTO Accounts (account_owner, account_id, balance)" " VALUES ('Jimmy', 2, 40102.28)"
    )

    db_session.execute(
        "INSERT INTO Transfers (transfer_id, amount, transfer_type, src_account_id, dest_account_id, info)"
        ' VALUES (1, 1203.23, "IntraBank", 2, 1, "Rent money")'
    )
    db_session.execute(
        "INSERT INTO transfers (transfer_id, amount, transfer_type, src_account_id, dest_account_id, info)"
        ' VALUES (2, 320.13, "IntraBank", 10, 1, "Vacation rental")'
    )
    db_session.commit()


def add_data_bank_2(db_session: Session):
    """Add data for bank 1.

    Args:
        db_session (Session): Database sql alchemy session.
    """
    # Adding data
    db_session.execute(
        "INSERT INTO Accounts (account_owner, account_id, balance)" " VALUES ('Leia', 1, 1230.30)"
    )
    db_session.execute(
        "INSERT INTO Accounts (account_owner, account_id,  balance)" " VALUES ('Emma',2, 40102.28)"
    )

    db_session.execute(
        "INSERT INTO Transfers (transfer_id, amount, transfer_type, src_account_id, dest_account_id, info)"
        ' VALUES (1, 1203.23, "IntraBank", 2, 1, "Rent money")'
    )
    db_session.execute(
        "INSERT INTO transfers (transfer_id, amount, transfer_type, src_account_id, dest_account_id, info)"
        ' VALUES (2, 320.13, "IntraBank", 10, 1, "Vacation rental")'
    )
    db_session.commit()
