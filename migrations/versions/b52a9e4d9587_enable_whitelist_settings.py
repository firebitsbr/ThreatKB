"""Enable Whitelist Settings

Revision ID: b52a9e4d9587
Revises: 808f4e517394
Create Date: 2018-12-09 22:42:26.427088

"""
import datetime

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
from app.models import cfg_settings

revision = 'b52a9e4d9587'
down_revision = '808f4e517394'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    date_created = datetime.datetime.now().isoformat()
    date_modified = datetime.datetime.now().isoformat()

    op.bulk_insert(
        cfg_settings.Cfg_settings.__table__,
        [
            {"key": "ENABLE_IP_WHITELIST_CHECK_ON_SAVE", "value": "1", "public": True, "date_created": date_created,
             "date_modified": date_modified,
             "description": "Whether Whitelist check for IP should be enabled on save or not."},
            {"key": "ENABLE_DNS_WHITELIST_CHECK_ON_SAVE", "value": "1", "public": True, "date_created": date_created,
             "date_modified": date_modified,
             "description": "Whether Whitelist check for DNS should be enabled on save or not."},
            {"key": "WHITELIST_STATES", "value": "is_release_state,is_staging_state", "public": True, "date_created": date_created,
             "date_modified": date_modified,
             "description": "List of states to perform Whitelist check on. Only applicable if ENABLE_IP_WHITELIST_CHECK_ON_SAVE or ENABLE_DNS_WHITELIST_CHECK_ON_SAVE enabled."}
        ]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    keys = ["ENABLE_IP_WHITELIST_CHECK_ON_SAVE", "ENABLE_DNS_WHITELIST_CHECK_ON_SAVE", "WHITELIST_STATES"]
    for key in keys:
        op.execute("""DELETE from cfg_settings where `key`='%s';""" % (key))
    # ### end Alembic commands ###
