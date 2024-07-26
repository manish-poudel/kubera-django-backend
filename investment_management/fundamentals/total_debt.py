from ..models import FinancialData
from .utilities import Utilities

class TotalDebt:

    def __init__(self) -> None:
        pass

    def get_historical_totaldebt(self, symbols):
        data = FinancialData.objects.filter(symbol__in = symbols, metric_type = 'total_debt')
        return Utilities.transform_data_year(data=data)

