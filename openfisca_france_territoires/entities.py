"""
This file defines the entities needed by our legislation.

Taxes and benefits can be calculated for different entities: communes, etat, companies, etc.

See https://openfisca.org/doc/key-concepts/commune,_entities,_role.html
"""

from openfisca_core.entities import build_entity

Commune = build_entity(
    key = "commune",
    plural = "communes",
    label = "Une commune. L'entité légale la plus réduite à laquelle s'applique la législation de ce moteur de calcul.",
    doc = """
    Une commune est l'entité légale la plus réduite percevant des dotations de l'État.
    """,
    is_person = True,  # entité pivot
    )


Etat = build_entity(
    key = "etat",
    plural = "etats",
    label = "État",
    roles = [
        {
            "key": "commune",
            "plural": "communes",
            "label": "Communes",
            },
        ],
    )

entities = [Etat, Commune]
