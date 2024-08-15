from ...models import FinancialData
from .utilities import Utilities

class CashFlow:

    def __init__(self) -> None:
        pass


    def get_historical_cashflow(self, symbols):
        data = FinancialData.objects.filter(symbol__in = symbols, metric_type = 'free_cashflow')
        return Utilities.transform_data_year(data=data)




