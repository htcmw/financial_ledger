from sqlalchemy import Column, Integer, Text, Float

from app.model.base import Base


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, index=True)  # 아이디
    date = Column(Text)  # 날짜
    exchange_name = Column(Text)  # 거래소 이름
    account_email = Column(Text)  # 계정 아이디
    ticker = Column(Text)  # 증권 이름
    ticker_symbol = Column(Text)  # 증권 고유 코드
    financial_instruments = Column(Text)  # 현물, 선물, 옵션 등..
    key_currency = Column(Text)  # 거래시 기축통화
    type = Column(Text)  # 진입, 종료, 입금, 출금, 청산, 이벤트 입금
    position = Column(Text)  # 롱, 숏, null
    leverage = Column(Float)  # 1 to n, null
    quantity = Column(Float)  # 수량
    price = Column(Float)  # 거래단가
    fee = Column(Float)  # 수수료
    total_amount = Column(Float)  # 거래금액
    net_profit = Column(Float)  # 정산금액(거래금액 - 수수료)
    sender = Column(Text)  # 송신인
    recipient = Column(Text)  # 수취인
    withdrawal_address = Column(Text)  # 출금 주소
    created_at = Column(Text)
    updated_at = Column(Text)
