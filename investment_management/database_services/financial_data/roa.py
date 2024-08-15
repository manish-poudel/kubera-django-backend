from ...models import FinancialData
from .utilities import Utilities

class ROA:

    def __init__(self) -> None:
        pass


    def calculate_roa(self, f_data):
        try:
            net_income = f_data['net_income']
            total_assets = f_data['total_assets']
            return net_income / total_assets
        except:
            return None 

    def get_historical_roa(self, symbols):
        data = FinancialData.objects.filter(symbol__in = symbols, metric_type__in = ['net_income', 'total_assets'])
        metrics = Utilities.transform_data_year(data=data)                    
        for symbol in metrics:
            company_data = metrics[symbol]
            for year in company_data:
                metrics[symbol][year]['roa'] = self.calculate_roa(metrics[symbol][year])  

        return metrics    





