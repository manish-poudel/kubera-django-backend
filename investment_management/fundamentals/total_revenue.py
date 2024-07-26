from ..models import FinancialData
from .utilities import Utilities

class TotalRevenue:

    def __init__(self) -> None:
        pass

    def get_historical_totalrevenue(self, symbols):
        data = FinancialData.objects.filter(symbol__in = symbols, metric_type = 'total_revenue')
        return Utilities.transform_data_year(data=data)




