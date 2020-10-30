# invenio-server
Basic invenio server without UI.

## Usage
Server for testing oarepo repositories. It is only minimalistic version, so you can access only data model related URLs (api/records)

## Instalation
1) install poetry (https://python-poetry.org/)
2) inside invenio-server/inv run command `poetry install`
  this will create .venv folder inside invenio-server folder, if not:
    2,25) run `poetry config --list` and delete venv which was created, path to this .venv folder is in virtualenvs.path variable listed by `poetry config --list` command
    2,5) run `poetry config virtualenvs.path --unset`
    2,75) run `poetry install` again
3) inside invenio-server/inv/.venv create folder `var`
4) inside invenio-server/inv/.venv/var create folder `instance`
5) inside invenio-server/inv/.venv/var/instance create file `invenio.cfg`
6) put this inside invenio.cfg :
  `SERVER_NAME='127.0.0.1:5000'
  PREFERRED_URL_SCHEME='https'

  SQLALCHEMY_DATABASE_URI='sqlite:///test.db'

  RATELIMIT_ENABLED=False

  SEARCH_ELASTIC_HOSTS = [
      dict(host='127.0.0.1', port=9200),
  ]`
7) run command `./run.sh` (inside invenio-server/inv)
8) from another terminal, run command ./bootstrap.sh (inside invenio-server/inv), this will also add some records to your repository
9) you now have access to the server on https://127.0.0.1:5000. Basic data model api is on https://127.0.0.1:5000/api/records/
