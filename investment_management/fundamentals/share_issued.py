from ..models import FinancialData
from .utilities import Utilities

class SharedIssued:

    def __init__(self) -> None:
        pass

    def get_historical_shareissued(self, symbols):
        data = FinancialData.objects.filter(symbol__in = symbols, metric_type = 'share_issued')
        return Utilities.transform_data_year(data=data)

