"""add first/last name

Revision ID: e3cd81869541
Revises: 80d1cd94f959
Create Date: 2025-09-23 02:20:11.072210

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers
revision = "add_first_last_name"
down_revision = "80d1cd94f959"

def upgrade():
    op.add_column("users", sa.Column("first_name", sa.String(), nullable=True))
    op.add_column("users", sa.Column("last_name", sa.String(), nullable=True))

    # naive split: first token -> first_name, rest -> last_name
    op.execute("""
        UPDATE users
        SET first_name = split_part(name, ' ', 1),
            last_name  = NULLIF(btrim(substr(name, length(split_part(name, ' ', 1)) + 1)), '')
    """)


    op.alter_column("users", "first_name", nullable=False)


    op.drop_column("users", "name")

def downgrade():
    op.add_column("users", sa.Column("name", sa.String(), nullable=False, server_default=""))
    op.execute("UPDATE users SET name = CONCAT(first_name, CASE WHEN last_name <> '' THEN ' ' || last_name ELSE '' END)")
    op.alter_column("users", "name", server_default=None)
    op.drop_column("users", "last_name")
    op.drop_column("users", "first_name")