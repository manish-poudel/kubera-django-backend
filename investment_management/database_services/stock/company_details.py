

from django.http import JsonResponse
from investment_management.models import CompanyOfficer, Stock


class CompanyDetails:

    def get_company_details(self, stock_id):
        stock = Stock.objects.get(id = stock_id)

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
        employees = CompanyOfficer.objects.filter(stock_id = stock_id)
        employees_list = []
        for employee in employees:
            employees_list.append({
                "name": employee.name,
                "title": employee.title
            })

        stock_data['employees'] = employees_list
        return JsonResponse(stock_data)
