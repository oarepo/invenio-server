invenio db destroy --yes-i-know
invenio db init create

invenio index destroy --force --yes-i-know
invenio index init --force
invenio index queue init purge

invenio testrepo records
