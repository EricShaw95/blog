# models.py
import datetime

# 导入 SQLAlchemy 中的 Model 类
from app import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.now(datetime.UTC),  # 正确调用 utcnow
    )
    updated_at = db.Column(
        db.DateTime,
        default=datetime.datetime.now(datetime.UTC),
        onupdate=datetime.datetime.now(datetime.UTC),  # 同上
    )

    def __repr__(self):
        return "<Article %r>" % self.content
