from ..models import FinancialData
from .utilities import Utilities

class TotalCash:

    def __init__(self) -> None:
        pass

    def get_historical_totalcash(self, symbols):
        data = FinancialData.objects.filter(symbol__in = symbols, metric_type = 'total_cash')
        return Utilities.transform_data_year(data=data)
