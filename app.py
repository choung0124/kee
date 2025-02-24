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

poem_parag_1 = [
    "생화"
]    

poem_parag_2 = [
    "생화를 불쌍해주는 그대,",
    "어떤 마음으로 새상을 맞이 할까요",
    "순간 순간 지나가는 생각들,",
    "뭐든지 들어 줄게요",
    "그대의 마음을 이해하고 싶어요.",
]

poem_parag_3 = [
    "공감을 어색하는 당신,",
    "누구보다 마음이 여린 것 같아요",
    "생화의 아름다움을 감사하며,",
    "생명의 현실을 바라 보는 당신",
    "나도 생화로 봐주면 안될 까요?",
]

poem_parag_4 = [
    "생화를 불쌍해주는 내 사랑 에게,",
    "함께 꽃밭을 키워 보고 싶어요"
]

def stream_paragraph(paragraph_lines):
    # Create a container for each line in the paragraph
    line_containers = [st.empty() for _ in paragraph_lines]
    
    # Stream each line in the paragraph
    for line_idx, line in enumerate(paragraph_lines):
        current_line = ""
        # Stream each character in the line
        for char in line:
            current_line += char
            # Center the text using markdown
            line_containers[line_idx].markdown(f"<div style='text-align: left'>{current_line}</div>", unsafe_allow_html=True)
            time.sleep(0.1)

def stream_poem():
    # Stream first paragraph
    stream_paragraph(poem_parag_1)
    # Double newline between paragraphs
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Stream second paragraph
    stream_paragraph(poem_parag_2)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Stream third paragraph
    stream_paragraph(poem_parag_3)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Stream fourth paragraph
    stream_paragraph(poem_parag_4)

# Stream the poem before the rest of the content
stream_poem()

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

