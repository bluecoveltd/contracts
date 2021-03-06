import traceback

from contracts.main import parse_contract_string
from .utils import check_contracts_ok, syntax_fail, check_contracts_fail

from contracts.library import *  # @UnusedWildImport @UnresolvedImport

def check_good_repr(c):
    """ Checks that we can eval() the __repr__() value and we get
        an equivalent object. """
    parsed = parse_contract_string(c)
    # Check that it compares true with itself
    assert parsed.__eq__(parsed), 'Repr does not know itself: %r' % parsed

    reprc = parsed.__repr__()

    try:
        reeval = eval(reprc)
    except Exception as e:
        traceback.print_exc()
        raise Exception('Could not evaluate expression %r: %s' % (reprc, e))

    assert reeval == parsed, \
            'Repr gives different object:\n  %r !=\n  %r' % (parsed, reeval)


def check_reconversion(s, exact):
    """ Checks that we can eval() the __repr__() value and we get
        an equivalent object. """
    parsed = parse_contract_string(s)

    s2 = parsed.__str__()
    reconv = parse_contract_string(s2)

    msg = 'Reparsing gives different objects:\n'
    msg += '  Original string: %r\n' % s
    msg += '           parsed: %r\n' % parsed
    msg += '      Regenerated: %r\n' % s2
    msg += '         reparsed: %r' % reconv

    assert reconv == parsed, msg

    if exact:
        # Warn if the string is not exactly the same.
        if s2 != s:
            msg = ('Slight different regenerated strings:\n')
            msg += ('   original: %s\n' % s)
            msg += ('  generated: %s\n' % s2)
            msg += ('   parsed the first time as: %r\n' % parsed)
            msg += ('                and then as: %r' % reconv)
            assert s2 == s, msg
