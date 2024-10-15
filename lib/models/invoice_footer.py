class Footer:
    def __init__(
        self,
        currency,
        exchange_rate,
        other_taxes_ammout,
        total,
        net_amount_untaxed=None,
        net_amount_taxed=None,
        vat_27=None,
        vat_21=None,
        vat_10_5=None,
        vat_5=None,
        vat_2_5=None,
        vat_0=None,
        sub_total=None,
    ):
        self.currency = currency
        self.net_amount_taxed = net_amount_taxed
        self.net_amount_untaxed = net_amount_untaxed
        self.vat_27 = vat_27
        self.vat_21 = vat_21
        self.vat_10_5 = vat_10_5
        self.vat_5 = vat_5
        self.vat_2_5 = vat_2_5
        self.vat_0 = vat_0
        self.other_taxes_ammout = other_taxes_ammout
        self.total = total
        self.exchange_rate = exchange_rate
        self.currency = currency
        self.sub_total = sub_total
