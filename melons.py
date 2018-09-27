"""Classes for melon orders."""


class AbstractMelonOrder():

    def __init__(self, species, qty, order_type, tax):
        """Initiliaze melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5

        if self.species == "Christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code

    def get_total(self):

        actual_total = super().get_total()

        if self.qty < 10:
            actual_total += 3

        return actual_total


class GovernmentMelonOrder(AbstractMelonOrder):
    """An order from the U.S. government."""

    def __init__(self, species, qty):
        """Initialize government melon order."""

        super().__init__(species, qty, "domestic", 0.0)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Marks an order as inspected or not."""

        self.passed_inspection = passed
