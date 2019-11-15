# colander_mtgjson

Collection of Colander Schemas for validating MTGJSON4

# Usage

Schemas are written to be composable:

```python
from colander_mtgjson import BaseCardSchema, CreatureSchema, RenameMixin

class CardSchema(RenameMixin, CreatureSchema, BaseCardSchema):
  """Deserialize and serialize only:
      * Base info (card name, etc...)
      * Creature info (power, toughness, etc...)
  """
  pass
```

For a complete list of schema partials, see `src/colander_mtgjson/card_schemas.py`.
