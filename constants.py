# Decimal number settings
DECIMAL_DIGITS = 6
DECIMAL_PLACES = 2


# Max length of a title
TITLE_MAX_LEN = 100

# Max len of typical overview string
MAX_STRING_LEN = 500


# Task related statuses.
RUNNING = 0
NOT_ASSIGNED = 1
FINISHED = 2
TASK_STATUSES = (
  (RUNNING, 'RUNNING'),
  (NOT_ASSIGNED, 'NOT ASSIGNED'),
  (FINISHED, 'FINISHED'))


# Category related item types.
# Category means a category node with children.
TYPE_CATEGORY = 0
# Task means task itself
TYPE_TASK = 1
# History means finished task
TYPE_HISTORY = 2

ITEM_TYPES = (
  (TYPE_CATEGORY, 'CATEGORY'),
  (TYPE_TASK, 'TASK'),
  (TYPE_HISTORY, 'HISTORY'))