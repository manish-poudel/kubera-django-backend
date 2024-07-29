
from django.http import JsonResponse
from django.shortcuts import render
from collections import defaultdict
from django.db.models.functions import Lower
from django.db.models import Count, Case, When, Value, CharField
from .database_services.fundamentals.roa import ROA
from .database_services.fundamentals.cashflow import CashFlow
from .database_services.fundamentals.roe import ROE
from .database_services.fundamentals.total_revenue import TotalRevenue
from .database_services.fundamentals.total_cash import TotalCash
from .database_services.fundamentals.share_issued import SharedIssued
from .database_services.fundamentals.total_debt import TotalDebt

from investment_management.models import Stock



def home(request):
    stocks = Stock.objects.all()
    return render(request, 'home.html', {'stocks':stocks})





def get_fundamental_data(request, exchange, ftype):
    try:     
        fundamental_data = None
        status = 200
        symbols = request.GET.get('symbols', None)
        symbols = symbols.split(',')

        if ftype == "roa":
            roa = ROA()
            fundamental_data = roa.get_historical_roa(symbols) 

        elif ftype == "cashflow":
            cashflow = CashFlow()
            fundamental_data = cashflow.get_historical_cashflow(symbols=symbols)

        elif ftype == "roe":
            roe = ROE()
            fundamental_data = roe.get_historical_roe(symbols=symbols)      

        elif ftype == "totalrevenue":
            total_revenue = TotalRevenue()
            fundamental_data = total_revenue.get_historical_totalrevenue(symbols=symbols)      

        elif ftype == "totalcash":
            total_cash = TotalCash()
            fundamental_data = total_cash.get_historical_totalcash(symbols=symbols)  
        
        elif ftype == "shareissued":
            share_issued = SharedIssued()
            fundamental_data = share_issued.get_historical_shareissued(symbols=symbols)   

        elif ftype == "totaldebt":
            total_debt = TotalDebt()
            fundamental_data = total_debt.get_historical_totaldebt(symbols=symbols)  
                  
        else:
            fundamental_data = {
                    "result": "no such fundamental type" } 
            status = 404   
        return JsonResponse(fundamental_data, status = status)
    except Exception as e:
        print(e)
        return JsonResponse({
            "msg": "Something went wrong"
        }, status = 500)

def sector_stock(request):
    exchange = request.GET.get('exchange', None)

    # Fetch stocks filtered by symbol if provided, otherwise fetch all stocks
    if exchange:
        stocks = Stock.objects.filter(exchange=exchange)
    else:
        stocks = Stock.objects.all()

    # Initialize a defaultdict for grouping by sector_display
    grouped_stocks = defaultdict(lambda: {'stocks': [], 'count': 0})

    # Group stocks by sector_display and count them
    for stock in stocks:
        sector = stock.sector_display.strip() if stock.sector_display else 'Other'
        if sector.lower() in ['n/a', 'unknown', 'not applicable']:
            sector = 'Other'
        grouped_stocks[sector]['stocks'].append({
            'id': stock.id,
            'symbol': stock.symbol,
            'company_name': stock.company_name
        })
        grouped_stocks[sector]['count'] += 1

    # Convert defaultdict to regular dict
    grouped_stocks = {sector: {
        'count': data['count'],
        'stocks': data['stocks']
    } for sector, data in grouped_stocks.items()}

    # Sort the grouped stocks by sector_display in alphabetical order
    sorted_grouped_stocks = dict(sorted(grouped_stocks.items(), key=lambda item: item[0]))

    # Return JSON response with minimal data
    return JsonResponse(sorted_grouped_stocks)


def stock_detail(request, stock_id):
    try:
        stock = Stock.objects.get(id=stock_id)
        stock_data = {
            'id': stock.id,
            'symbol': stock.symbol,
            'company_name': stock.company_name,
            'description': stock.description,
            'exchange': stock.exchange,
            'country': stock.country,
            'address1': stock.address1,
            'address2': stock.address2,
            'city': stock.city,
            'zip': stock.zip,
            'phone': stock.phone,
            'website': stock.website,
            'sector_key': stock.sector_key,
            'sector_display': stock.sector_display,
            'industry_key': stock.industry_key,
            'industry_display': stock.industry_display,
            'fulltime_employees': stock.fulltime_employees,
            'last_updated': stock.last_updated.isoformat()
        }
        return JsonResponse(stock_data)
    except Stock.DoesNotExist:
        return JsonResponse({'error': 'Stock not found'}, status=404)

def group_companies_by_alphabet(request, exchange):
    # Fetch companies based on the exchange (assuming there's a field in Stock for exchange)
    companies = Stock.objects.filter(exchange=exchange.upper())

    # Group companies by the first letter of their name
    grouped_companies = {}
    for company in companies:
        name = company.company_name
        if name:
            first_letter = name[0].upper()  # Group by the first letter (case-insensitive)
            if first_letter not in grouped_companies:
                grouped_companies[first_letter] = []
            grouped_companies[first_letter].append({
                'id': company.id,
                'symbol': company.symbol,
                'name': name
            })

    # Convert the dictionary to a sorted list of tuples
    sorted_grouped_companies = dict(sorted(grouped_companies.items()))

    return JsonResponse(sorted_grouped_companies)

def company_stats(request, exchange):
    # Annotate sector_display to convert 'n/a' to 'Others'
    adjusted_sector_counts = Stock.objects.filter(exchange=exchange.upper()).annotate(
        adjusted_sector_display=Case(
            When(sector_display__iexact='n/a', then=Value('Others')),
            default=Lower('sector_display'),
            output_field=CharField()
        )
    ).values('adjusted_sector_display').annotate(
        total_count=Count('id')  # Count occurrences of each sector
    ).order_by('adjusted_sector_display')

    # Format the data for response
    data = {
        'stats': [
            {
                'sector_display': entry['adjusted_sector_display'],
                'total_count': entry['total_count']
            }
            for entry in adjusted_sector_counts
        ]
    }

    return JsonResponse(data)





def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    result = val1 + val2
    return render(request, 'result.html', {'result': result})
