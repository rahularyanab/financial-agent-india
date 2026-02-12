from datetime import datetime, timedelta
import calendar

def get_next_expiry_date():
    """
    Returns the next expiry date for options.
    
    The expiry date is the last Thursday of the month. If today is 
    a Thursday, the expiry date for the current month is returned.
    """
    today = datetime.now()
    first_day_next_month = (today.replace(day=1) + timedelta(days=31)).replace(day=1)
    last_thursday_next_month = first_day_next_month + timedelta(days=(3 - first_day_next_month.weekday()) % 7 + 21)
    return last_thursday_next_month.date()

def fetch_option_chain():
    expiry_date = get_next_expiry_date()
    # Logic to fetch the option chain based on expiry_date
    pass

# Other functions remain unchanged below...