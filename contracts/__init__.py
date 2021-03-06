__version__ = '2019.1b5'

import logging

#logging.basicConfig()
logger = logging.getLogger(__name__)

from .interface import (Contract, ContractNotRespected,
                        CannotDecorateClassmethods,
                        ContractSyntaxError, ContractException)

from .main import (check, fail, check_multiple, contract_decorator,
                   contracts_decorate as decorate,
                   parse_flexible_spec as parse)


# Just make them appear as belonging to the "contracts" Module
# So that Eclipse and other IDEs will not get confused.
def contract(
    *args,
    _evaluate_docstring=True,
    _evaluate_annotations=True,
    **kwargs
):
    return contract_decorator(
        *args,
        _evaluate_docstring=_evaluate_docstring,
        _evaluate_annotations=_evaluate_annotations,
        **kwargs
    )


contract.__doc__ = contract_decorator.__doc__

from .main import new_contract as new_contract_main


def new_contract(*args):
    return new_contract_main(*args)


new_contract.__doc__ = new_contract_main.__doc__

from .enabling import disable_all, enable_all, all_disabled

# A couple of useful functions
from .interface import describe_value, describe_type, describe_value_multiline
from .utils import *

from .metaclass import ContractsMeta, with_metaclass

ContractsMeta.__module__ = 'contracts'

# And after everything else is loaded, load the  utils
from .useful_contracts import *
# After everything is loaded, load aliases
# from .library import miscellaneous_aliases  # @UnusedImport
