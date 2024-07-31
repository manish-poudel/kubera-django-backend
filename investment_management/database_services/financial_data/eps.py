from ...models import FinancialData
from .utilities import Utilities

class EPS:

    def __init__(self) -> None:
        pass


    def calculate_eps(self, f_data):
        try:
            net_income = f_data['net_income']
            share_issued = f_data['share_issued']
            return net_income / share_issued
        except:
            return None 


    def get_historical_eps(self, symbols):
        data = FinancialData.objects.filter(symbol__in = symbols, metric_type__in = ['net_income', 'share_issued'])
        data = Utilities.transform_data_year(data=data)

        for symbol in data:
            company_data = data[symbol]
            for year in company_data:
                data[symbol][year]['eps'] = self.calculate_eps(data[symbol][year])  

        return data        

