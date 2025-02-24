import streamlit as st
from datetime import datetime
import pytz
import time
from app_utils import get_time_difference, get_days_since

# Set timezone to UK
uk_tz = pytz.timezone('Europe/London')

# Set the target dates (in UK time)
target_date = datetime(2025, 3, 10, 18, 5, 0, tzinfo=uk_tz)  # Main countdown
first_met_date = datetime(2025, 2, 5, 12, 0, 0, tzinfo=uk_tz)  # First meeting at midday
dating_start_date = datetime(2025, 2, 14, 19, 0, 0, tzinfo=uk_tz)  # Started dating in evening

st.title("Andie and Kee 💖")

# Add containers for the different counters
main_countdown_container = st.container()
milestones_container = st.container()

# Update the counters every second
while True:
    days, hours, minutes, seconds = get_time_difference(target_date)
    days_since_meeting = get_days_since(first_met_date)
    days_since_dating = get_days_since(dating_start_date)
    
    with main_countdown_container:
        st.header("Till We Meet Again 👯‍♀️", divider="rainbow")
        # Main counter (Days)
        st.header(f"{days} Days")
        
        # Remaining time breakdown
        st.text(f"{hours} hours, {minutes} minutes, and {seconds} seconds")
    
    with milestones_container:
        st.header("Our Milestones 🥰", divider="rainbow")
        
        # Display days since first meeting and starting to date
        col_meet, col_date = st.columns(2)
        
        with col_meet:
            st.metric("Days Since We First Met", 
                     days_since_meeting,
                     help=f"First met on {first_met_date.strftime('%B %d, %Y at %I:%M %p')} UK time")
            
        with col_date:
            st.metric("Days Since We Started Dating", 
                     days_since_dating,
                     help=f"Started dating on {dating_start_date.strftime('%B %d, %Y at %I:%M %p')} UK time")
    
    time.sleep(1)
    st.rerun()

