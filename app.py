import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import time

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

# Set the target dates (in UK time)
interacted_date = datetime(2021, 2, 1, 0, 0, 0, tzinfo=uk_tz)  # Main countdown
target_date = datetime(2025, 3, 10, 18, 5, 0, tzinfo=uk_tz)  # Main countdown
first_met_date = datetime(2025, 2, 5, 12, 0, 0, tzinfo=uk_tz)  # First meeting at midday
dating_start_date = datetime(2025, 2, 14, 19, 0, 0, tzinfo=uk_tz)  # Started dating in evening

st.title("Our Story <3")
st.subheader("We've known each other for over 4 years...")
st.text("Our paths crossed multiple times, but it was only until February 2025 that we finally met.")
st.text("It almost feels like fate guided us to meet at the right time.")
st.image("images/Untitled - Frame 8.jpg", use_container_width=True)
st.image("images/Untitled - Frame 4 copy 2.jpg", use_container_width=True)


st.text("In the short time after we met, we started dating...")
st.text("On valentines day, we both confessed our feelings for each other. Within the same day we started dating.")
st.text("Everything seems to fall in place naturally with you, just like how I fell in love with you.")
st.image("images/Untitled - Frame 5.jpg", use_container_width=True)

st.text("You and I are connected in so many ways, each complex in its own right.")
st.text("Yet somehow, I beleive that we've only scratched the surface of our connection.")
st.text("I'm excited to discover more about us, and at the same time, I'm excited to create new connections with you.")
st.image("images/Untitled - Frame 7 copy.jpg", use_container_width=True)
# Create static headers
st.header("Till We Meet Again 👯‍♀️", divider="rainbow")

# Create empty containers for dynamic content
days_container = st.empty()
time_container = st.empty()

st.header("Our Milestones 🥰", divider="rainbow")
col_meet, col_date = st.columns(2)

# Create empty containers for metrics
meet_metric = col_meet.empty()
date_metric = col_date.empty()

# Stream the poem before the rest of the content

# Update the dynamic content in a loop
while True:
    days, hours, minutes, seconds = get_time_difference(target_date)
    days_since_meeting = get_days_since(first_met_date)
    days_since_dating = get_days_since(dating_start_date)
    
    # Update countdown
    days_container.header(f"{days} Days")
    time_container.text(f"{hours} hours, {minutes} minutes, and {seconds} seconds")
    
    # Update metrics
    meet_metric.metric("Days Since We First Met", 
                      days_since_meeting,
                      help=f"First met on {first_met_date.strftime('%B %d, %Y at %I:%M %p')} UK time")
    
    date_metric.metric("Days Since We Started Dating", 
                      days_since_dating,
                      help=f"Started dating on {dating_start_date.strftime('%B %d, %Y at %I:%M %p')} UK time")
    
    time.sleep(1)

