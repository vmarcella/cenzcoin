from collections import OrderedDict

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_ordered_dict(self):
        '''
            Convert the transaction into an ordered dict

            Returns:
                An Ordered dict containing key transaction information
        '''
        return OrderedDict([('sender', self.sender), ('recipient', self.recipient), ('amount', self.amount)])