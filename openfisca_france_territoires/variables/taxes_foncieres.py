from openfisca_core.model_api import max_
from openfisca_core.periods import YEAR
from openfisca_core.variables import Variable
from openfisca_france_territoires.entities import Commune


# TODO règle de la variation proportionnelle des taux
# quatre taxes (ou des trois taxes pour les communes membres d’EPCI à fiscalité professionnelle unique)
# TFB, la TFNB, la TH et la CFE


class coefficient_variation_proportionnelle(Variable):
    value_type = float
    entity = Commune
    definition_period = YEAR
    label = "Coefficient de variation proportionnelle"
    reference = "todo"


class taxe_fonciere_proprietes_baties(Variable):
    value_type = float
    entity = Commune
    definition_period = YEAR
    label = "Taxe foncière sur les propriétés bâties (TFB)"
    reference = "https://www.collectivites-locales.gouv.fr/finances-locales/taxes-foncieres"

class taxe_fonciere_proprietes_baties_taux_plafond(Variable):
    value_type = float
    entity = Commune
    definition_period = YEAR
    label = "Taux plafond taxe foncière sur les propriétés bâties (TFB)"
    reference = "todo"

class taxe_fonciere_proprietes_baties_taux_maximal(Variable):
    value_type = float
    entity = Commune
    definition_period = YEAR
    label = "Taxe foncière sur les propriétés bâties (TFB)"
    reference = "https://www.collectivites-locales.gouv.fr/finances-locales/taxes-foncieres"
    documentation = """
    Le taux voté a l'obligation de correspondre au taux de l'année précédente 
    multiplié par un coefficient de variation proportionnelle et ne pas dépasser 
    un taux plafond de l'année courante.
    """

    def formula(commune, period, _parameters):
        # TODO rendre générique toute commune
        taux_annee_precedente = _parameters(period.last_year).taxe_fonciere_proprietes_baties.taux.chauffailles
        coefficient_variation_proportionnelle = commune("coefficient_variation_proportionnelle", period)
        taxe_fonciere_proprietes_baties_taux_plafond = commune("taxe_fonciere_proprietes_baties_taux_plafond", period)
        
        return max_(taux_annee_precedente * coefficient_variation_proportionnelle, taxe_fonciere_proprietes_baties_taux_plafond)


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
