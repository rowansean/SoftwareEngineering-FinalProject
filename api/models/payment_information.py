from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class PaymentInformation(Base):
    __tablename__ = "payment_information"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    card_information = Column(String(16))
    payment_type = Column(String(10))

    promotion_id = Column(Integer, ForeignKey('promotions.id'))
    promotion = relationship("Promotion", back_populates="payment_information")