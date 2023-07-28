from openfisca_core.periods import YEAR
from openfisca_core.variables import Variable
from openfisca_france_territoires.entities import Commune


# TODO règle de la variation proportionnelle des taux
# quatre taxes (ou des trois taxes pour les communes membres d’EPCI à fiscalité professionnelle unique)
# TFB, la TFNB, la TH et la CFE

class taxe_fonciere_proprietes_baties(Variable):
    value_type = float
    entity = Commune
    definition_period = YEAR
    label = "Taxe foncière sur les propriétés bâties (TFB)"
    reference = "https://www.collectivites-locales.gouv.fr/finances-locales/taxes-foncieres"


class taxe_fonciere_proprietes_non_baties(Variable):
    value_type = float
    entity = Commune
    definition_period = YEAR
    label = "Taxe foncière sur les propriétés non bâties (TFNB)"
    reference = "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000028419445"
    # même article pour les communes et les foyers fiscaux ?


class taxe_habitation(Variable):
    value_type = float
    entity = Commune
    definition_period = YEAR
    label = "Taxe d'habitation (TH)"
    reference = "https://www.service-public.fr/particuliers/vosdroits/F42"


class cotisation_fonciere_entreprises(Variable):
    value_type = float
    entity = Commune
    definition_period = YEAR
    label = "Cotisation foncière des entreprises (CFE)"
    reference = "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000023380872"
