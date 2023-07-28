"""
This file defines variables for the modelled legislation.

A variable is a property of an Entity such as a Commune, a Etat…

See https://openfisca.org/doc/key-concepts/variables.html
"""

# Import from openfisca-core the Python objects used to code the legislation in OpenFisca
from openfisca_core.periods import MONTH
from openfisca_core.variables import Variable

# Import the Entities specifically defined for this tax and benefit system
from openfisca_france_territoires.entities import Etat


class total_benefits(Variable):
    value_type = float
    entity = Etat
    definition_period = MONTH
    label = "Sum of the benefits perceived by a etat"
    reference = "https://stats.gov.example/benefits"

    def formula(etat, period, _parameters):
        """Total benefits."""
        basic_income_i = etat.members("basic_income", period)  # Calculates the value of basic_income for each member of the etat

        return (
            + etat.sum(basic_income_i)  # Sum the etat members basic incomes
            + etat("housing_allowance", period)
            )


class total_taxes(Variable):
    value_type = float
    entity = Etat
    definition_period = MONTH
    label = "Sum of the taxes paid by a etat"
    reference = "https://stats.gov.example/taxes"

    def formula(etat, period, _parameters):
        """Total taxes."""
        income_tax_i = etat.members("income_tax", period)
        social_security_contribution_i = etat.members("social_security_contribution", period)

        return (
            + etat.sum(income_tax_i)
            + etat.sum(social_security_contribution_i)
            + etat("housing_tax", period.this_year) / 12
            )
