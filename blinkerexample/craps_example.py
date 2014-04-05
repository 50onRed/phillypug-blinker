from blinker import Namespace
import random

_signals = Namespace()

dice_rolled = _signals.signal('dice-rolled')


def roll(cheat=None, player='Steve'):
    number = cheat or random.randint(2, 12)
    dice_rolled.send(number, player=player)
    return number

# Signalling even without any subscribers is not a problem
roll()

# Subscribing to signals is easy. Just decorate your function with {signal}.connect
@dice_rolled.connect
def log_roll(number, player=None, **kwargs):
    print '{} rolled a {}'.format(number, player)


# Subscribing to specific senders is also easy, even using decorators
@dice_rolled.connect_via(7)
@dice_rolled.connect_via(11)
def front_line_winner(number, player=None, **kwargs):
    print 'WINNER WINNER, FRONT-LINE WINNER!'


roll(6)
roll(11)


def crapped_out(number, player=None, **kwargs):
    print '{} craps {}. Sorry, you lose!'.format(number, number)


# You may also subscribe to signals by calling the connect method
dice_rolled.connect(crapped_out, sender=2)
dice_rolled.connect(crapped_out, sender=3)
dice_rolled.connect(crapped_out, sender=12)

roll(12)

# Unsubscribing to signals is also easy
dice_rolled.disconnect(crapped_out, sender=12)

roll(12)