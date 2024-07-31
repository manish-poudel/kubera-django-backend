from ...models import FinancialData
from .utilities import Utilities

class ROE:

    def __init__(self) -> None:
        pass


    def calculate_roe(self, f_data):
        try:
            net_income = f_data['net_income']
            stockholder_equity = f_data['stockholder_equity']
            return net_income / stockholder_equity
        except:
            return None 

    def get_historical_roe(self, symbols):
        data = FinancialData.objects.filter(symbol__in = symbols, metric_type__in = ['net_income', 'stockholder_equity'])
        metrics = Utilities.transform_data_year(data=data)                
        for symbol in metrics:
            company_data = metrics[symbol]
            for year in company_data:
                metrics[symbol][year]['roe'] = self.calculate_roe(metrics[symbol][year])  

        return metrics    





