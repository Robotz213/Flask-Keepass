from pathlib import Path

from flask import Flask

from flask_keepass import KeepassManager

app = Flask(__name__)
app.config["KEEPASS_FILENAME"] = str(
    Path.cwd().joinpath("tests", "data", "test_db.kdbx"),
)
app.config["KEEPASS_PASSWORD"] = "password123"


Path(app.config["KEEPASS_FILENAME"]).parent.mkdir(parents=True, exist_ok=True)


manager = KeepassManager()


manager.init_app(app)

entry = manager.find_entries(first=True, title="Sample Entry")


if not entry:
    manager.add_entry(
        destination_group=manager.root_group,
        title="Sample Entry",
        username="user1",
        password="pass1",
        url="https://example.com",
        notes="This is a sample entry.",
    )

manager.save()

Path(app.config["KEEPASS_FILENAME"]).unlink(missing_ok=True)
Path(app.config["KEEPASS_FILENAME"]).parent.rmdir()
