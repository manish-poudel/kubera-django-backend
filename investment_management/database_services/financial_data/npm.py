from ...models import FinancialData
from .utilities import Utilities

class NPM:

    def __init__(self) -> None:
        pass


    def calculate_npm(self, f_data):
        try:
            net_income = f_data['net_income']
            total_revenue = f_data['total_revenue']
            return net_income / total_revenue
        except:
            return None 


    def get_historical_npm(self, symbols):
        data = FinancialData.objects.filter(symbol__in = symbols, metric_type__in = ['net_income', 'total_revenue'])
        data = Utilities.transform_data_year(data=data)

        for symbol in data:
            company_data = data[symbol]
            for year in company_data:
                data[symbol][year]['net_profit_margin'] = self.calculate_npm(data[symbol][year])  

        return data        

