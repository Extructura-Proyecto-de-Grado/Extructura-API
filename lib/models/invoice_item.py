class Item:
    def __init__(
        self,
        cod,
        title,
        amount,
        measure,
        unit_price,
        discount_perc,
        subtotal,
        subtotal_inc_fees=None,
        vat_fee=None,
        discounted_subtotal=None,
    ):
        self.cod = cod
        self.title = title
        self.amount = amount
        self.measure = measure
        self.unit_price = unit_price
        self.discount_perc = discount_perc
        self.subtotal = subtotal
        self.vat_fee = vat_fee
        self.subtotal_inc_fees = subtotal_inc_fees
        self.discounted_subtotal = discounted_subtotal
