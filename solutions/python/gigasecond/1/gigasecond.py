def add(moment):
    from datetime import datetime, timedelta
    return moment + timedelta(seconds=1e9)
