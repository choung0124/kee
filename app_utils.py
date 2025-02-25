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
            time.sleep(0.05)

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
    
stream_poem()

