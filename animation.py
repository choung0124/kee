import streamlit as st
import streamlit.components.v1 as components

# You can set page layout if you want, e.g.:
# st.set_page_config(layout="centered")

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Swirl Animation</title>
  <style>
    /* Basic reset */
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      background: #F3F1FA; /* Light lavender background */
      display: flex;
      justify-content: center;
      align-items: center;
      /* Fill parent container (Streamlit component) */
      height: 100%;
      width: 100%;
      margin: 0 auto;
    }

    /* Container for the SVG */
    #timeline {
      width: 300px;   /* Adjust as needed */
      height: 1000px; /* Adjust as needed */
      overflow: visible;
      display: block;
    }

    /* Common line/path styles */
    .swirl {
      fill: none;
      stroke-width: 4;
      stroke-linecap: round;
      stroke-linejoin: round;
    }
    .blue {
      stroke: #BCE6F3; /* Light blue */
    }
    .pink {
      stroke: #F9C4DD; /* Light pink */
    }

    .center-line {
      stroke: #fff;     /* White center line */
      stroke-width: 6;  /* Thicker line if you want */
    }

    /* Circle styles */
    .circle {
      fill: #fff;       /* White fill */
      stroke: none;
    }

    /* Text styling (years/months) */
    .year-text {
      font-family: sans-serif;
      font-size: 16px;
      fill: #000;       /* Black text */
    }
  </style>
</head>
<body>

<svg id="timeline" viewBox="0 0 300 1000" xmlns="http://www.w3.org/2000/svg">
  <!-- Text near top -->
  <text class="year-text" x="150" y="60" text-anchor="middle">
    2021 February
  </text>

  <!-- Vertical center line -->
  <line class="center-line" x1="150" y1="100" x2="150" y2="900" />

  <!-- Blue swirl (left swirl) -->
  <path
    id="blueSwirl"
    class="swirl blue"
    d="M 150,100
       C 100,150  200,250  150,300
       C 100,350  200,450  150,500
       C 100,550  200,650  150,700
       C 100,750  200,850  150,900"
  />

  <!-- Pink swirl (right swirl) -->
  <path
    id="pinkSwirl"
    class="swirl pink"
    d="M 150,100
       C 200,150  100,250  150,300
       C 200,350  100,450  150,500
       C 200,550  100,650  150,700
       C 200,750  100,850  150,900"
  />

  <!-- Top circle (center) -->
  <circle class="circle" cx="150" cy="100" r="12" />
  <!-- Bottom circle (center) -->
  <circle class="circle" cx="150" cy="900" r="12" />

  <!-- Text near bottom -->
  <text class="year-text" x="150" y="940" text-anchor="middle">
    2025 February
  </text>
</svg>

<script>
  /**
   * Animate an SVG path by “drawing” it from start to finish
   * using strokeDasharray and strokeDashoffset.
   */
  function animatePath(pathId, duration = 4) {
    const path = document.getElementById(pathId);
    const length = path.getTotalLength();

    // Clear any previous transition
    path.style.transition = path.style.WebkitTransition = 'none';
    // Set up the starting positions
    path.style.strokeDasharray = length;
    path.style.strokeDashoffset = length;

    // Force a reflow to ensure the styles are applied
    path.getBoundingClientRect();

    // Define our transition
    path.style.transition = path.style.WebkitTransition =
      'stroke-dashoffset ' + duration + 's ease-in-out';
    // Animate to strokeDashoffset = 0 (fully drawn)
    path.style.strokeDashoffset = '0';
  }

  window.addEventListener('load', () => {
    // Animate both swirls on page load
    animatePath('blueSwirl', 4);
    animatePath('pinkSwirl', 4);
  });
</script>

</body>
</html>
"""

# Render the HTML in Streamlit
components.html(html_code, height=1100, width=400)
