import pytz
from datetime import datetime

# Set timezone to UK
uk_tz = pytz.timezone('Europe/London')

def get_time_difference(target):
    now = datetime.now(uk_tz)
    difference = target - now
    
    # Calculate all time components
    days = difference.days
    hours = difference.seconds // 3600
    minutes = (difference.seconds % 3600) // 60
    seconds = difference.seconds % 60
    
    return days, hours, minutes, seconds

def get_days_since(start_date):
    now = datetime.now(uk_tz)
    difference = now - start_date
    return difference.days