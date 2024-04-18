from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base 

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    note = Column(String(255), nullable=False)  
    score = Column(String(255), nullable=False) 
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)  
    created_at = Column(DateTime, default=datetime.utcnow)  # Added a datetime column 

    # Relationship to the Order model
    order = relationship("Order", back_populates="reviews")

    def __repr__(self):
        return f"<Review(id={self.id}, note='{self.note}', score='{self.score}', order_id={self.order_id})>"
