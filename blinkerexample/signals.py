from blinker import Namespace

# Create namespaces to prevent potential collisions with the global Namespace
_signals = Namespace()

# Signals accept a doc string for pydoc help text
user_saved = _signals.signal('user-saved', doc='Signal for user saved. :param user: the user saved')
account_funded = _signals.signal('account-funded')
payment_method_added = _signals.signal('payment_method_added')
card_payment_created = _signals.signal('card_payment_created')
card_payment_processed = _signals.signal('card_payment_processed')
