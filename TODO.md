# TODO List for Renaming Column in Student Model

- [x] Edit lib/models.py to rename 'name' column to 'full_name' and update __repr__ method
- [x] Generate new Alembic migration with message "Renaming name to full_name"
- [x] Edit the new migration file to add op.rename_column in upgrade() and downgrade()
- [x] Run alembic upgrade head to apply the migration
- [x] Run alembic downgrade to the previous revision (791279dd0760_create_table_students.py) to revert
- [ ] Commit and push changes using git
