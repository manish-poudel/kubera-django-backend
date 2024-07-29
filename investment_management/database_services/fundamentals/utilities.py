class Utilities:
    
    def __init__(self) -> None:
        pass

    @staticmethod    
    def transform_data_year(data):
        metrics = {}
        for entry in data:
            symbol = entry.symbol
            if symbol not in metrics:
                metrics[symbol] = {}    
            year = entry.year.year
            if year not in metrics[symbol]:
                metrics[symbol][year] = {}
            metrics[symbol][year][entry.metric_type] = entry.metric_value
        return metrics       

