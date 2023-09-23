# from decimal import Decimal
# from django.conf import settings
# from django.core.exceptions import ImproperlyConfigured, ValidationError
# from django.core.validators import EMPTY_VALUES

from decimal import Decimal
# DEFAULT_CONTENT_TYPE_DEPRECATED_MSG, ENVIRONMENT_VARIABLE, global_settings, LazySettings
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.core.validators import EMPTY_VALUES


EU_COUNTRIES_RATES = {
    'AT': Decimal(20),  # Austria
    'BE': Decimal(21),  # Belgium
    'BG': Decimal(20),  # Bulgaria
    'CY': Decimal(19),  # Cyprus
    'CZ': Decimal(21),  # Czech Republic
    'DK': Decimal(25),  # Denmark
    'EE': Decimal(20),  # Estonia
    'FI': Decimal(24),  # Finland
    'FR': Decimal(20),  # France
    'DE': Decimal(19),  # Germany
    'GR': Decimal(24),  # Greece
    'HR': Decimal(25),  # Croatia
    'HU': Decimal(27),  # Hungary
    'IE': Decimal(21),  # Ireland
    'IT': Decimal(22),  # Italy
    'LV': Decimal(21),  # Latvia
    'LT': Decimal(21),  # Lithuania
    'LU': Decimal(17),  # Luxembourg
    'MT': Decimal(18),  # Malta
    'NL': Decimal(21),  # Netherlands
    'PL': Decimal(23),  # Poland
    'PT': Decimal(23),  # Portugal
    'RO': Decimal(19),  # Romania
    'SK': Decimal(20),  # Slovakia
    'SI': Decimal(22),  # Slovenia
    'ES': Decimal(21),  # Spain
    'SE': Decimal(25),  # Sweden
}

AFRICAN_COUNTRIES = {
    'ET': Decimal(20),  # ETHIOPIA
    'EG': Decimal(20),  # Egypt
    'GH': Decimal(20),  # Ghana
    'KE': Decimal(20),  # Kenya
    'NG': Decimal(20),  # Nigeria
    'TZ': Decimal(20),  # Tanzania
    'UG': Decimal(20),  # Uganda
    'SA': Decimal(20),  # South Africa
}

SOUTH_AMERICAN_COUNTRIES = {
    'BR': Decimal(20),  # Brazil
}

NORTH_AMERICAN_COUNTRIES = {
    'CN': Decimal(19),  # Canada
    'MX': Decimal(19),  # Mexico
    'US': Decimal(19),  # USA
}

OTHER_COUNTRIES = {
    'AU': Decimal(20),  # Australia
    'IN': Decimal(20),  # India
    'JP': Decimal(20),  # Japan
    'QT': Decimal(20),  # Qatar
    'UAE': Decimal(20),  # UAE
}


class EUTaxationPolicy():

    @classmethod
    def is_in_EU(cls, country_code):
        if country_code == 'GB':
            return False

        return country_code.upper() in EU_COUNTRIES_RATES.keys()


class JapanTaxationPolicy():
    pass


class IndiaTaxationPolicy():
    pass


class QatarTaxationPolicy():
    pass


class UAETaxationPolicy():
    pass


class AustraliaTaxationPolicy():
    pass
