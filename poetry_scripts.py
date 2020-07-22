import shutil

from src.poetry_test.app import app


def clean():
    shutil.rmtree("build", ignore_errors=True)


def flask():
    app.run(host="0.0.0.0", port=8080)
