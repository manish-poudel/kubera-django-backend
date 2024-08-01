

from django.http import Http404, JsonResponse
from investment_management.models import CompanyOfficer, Stock


class CompanyDetails:


    def get_stock_data(self,searchvalue):
        try:
            # Try to convert searchvalue to an integer
            search_id = int(searchvalue)
            # If conversion is successful, search by id
            return Stock.objects.get(id=search_id)
        except:
            print("")
            return Stock.objects.get(symbol=searchvalue)

            
    def get_company_details(self, value):
        print("Getting company details..." + value)
        stock = self.get_stock_data(value)
        print(stock)
        # Get stock data
        stock_data = {
            'id': stock.id,
            'symbol': stock.symbol,
            'name': stock.company_name,
            'description': stock.description,
            'exchange': stock.exchange,
            'country': stock.country,
            'address1': stock.address1,
            'address2': stock.address2,
            'city': stock.city,
            'zip': stock.zip,
            'phone': stock.phone,
            'website': stock.website,
            'sector_display': stock.sector_display,
            'industry_display': stock.industry_display,
        }

        # Get employee data
        employees = CompanyOfficer.objects.filter(stock_id = stock.id)
        employees_list = []
        for employee in employees:
            employees_list.append({
                "name": employee.name,
                "title": employee.title
            })

        stock_data['employees'] = employees_list
        return JsonResponse(stock_data)
      

