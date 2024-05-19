import os

from dotenv import load_dotenv
from flask import Flask, render_template, request

from extension import db
from models import Article

load_dotenv()


def create_app():
    app = Flask(__name__)
    # MySQL数据库配置
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv(
        "SQLALCHEMY_TRACK_MODIFICATIONS"
    )

    db.init_app(app)

    @app.route("/", methods=["GET", "POST"])
    def home_page():
        if request.method == "POST":
            entry_content = request.form.get("content")
            article = Article(content=entry_content)
            db.session.add(article)
            db.session.commit()

        articles = Article.query.all()
        return render_template("home.html", articles=articles)

    return app
