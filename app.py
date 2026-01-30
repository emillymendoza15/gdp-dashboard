import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Which Madison Spot Are You?",
    page_icon="📍",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffffff;
    }

    h1 {
        color: #b30000;
        text-align: center;
        font-weight: 800;
    }

    html, body, p, span, label, div {
        color: black !important;
    }

    div[data-testid="stRadio"] > label {
        font-weight: 700;
        color: black !important;
    }

    div[data-testid="stRadio"] span {
        color: black !important;
    }

    .stButton > button {
        background-color: #b30000;
        color: white !important;
        border-radius: 12px;
        font-weight: bold;
        padding: 8px 22px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- STATE ----------------
if "question" not in st.session_state:
    st.session_state.question = 0

if "scores" not in st.session_state:
    st.session_state.scores = {
        "Memorial Union Terrace": 0,
        "State Street": 0,
        "Memorial Library": 0,
        "Monona Terrace": 0,
        "The Old Fashioned": 0,
        "Dotty Dumpling's Dowry": 0
    }

# ---------------- QUESTIONS (7) ----------------
questions = [
    {
        "question": "Your ideal study environment is:",
        "options": {
            "Social, people around": "Memorial Union Terrace",
            "Quiet and focused": "Memorial Library",
            "Scenic and calming": "Monona Terrace",
            "Anywhere with food nearby": "Dotty Dumpling's Dowry"
        }
    },
    {
        "question": "What’s your go-to weekend plan?",
        "options": {
            "Walking around and exploring": "State Street",
            "Catching up on work": "Memorial Library",
            "Relaxing somewhere peaceful": "Monona Terrace",
            "Dinner and long conversations": "The Old Fashioned"
        }
    },
    {
        "question": "Pick a vibe:",
        "options": {
            "Lively and social": "Memorial Union Terrace",
            "Busy and exciting": "State Street",
            "Calm and reflective": "Monona Terrace",
            "Focused and quiet": "Memorial Library"
        }
    },
    {
        "question": "Where would you take a friend visiting Madison?",
        "options": {
            "A classic Wisconsin restaurant": "The Old Fashioned",
            "A walk through downtown": "State Street",
            "A chill lakeside spot": "Monona Terrace",
            "Somewhere cozy with food": "Dotty Dumpling's Dowry"
        }
    },
    {
        "question": "How do you handle a long day?",
        "options": {
            "Hang out with friends": "Memorial Union Terrace",
            "Push through and get work done": "Memorial Library",
            "Step back and recharge": "Monona Terrace",
            "Food fixes everything": "Dotty Dumpling's Dowry"
        }
    },
    {
        "question": "Your personality is best described as:",
        "options": {
            "Outgoing and friendly": "Memorial Union Terrace",
            "Driven and disciplined": "Memorial Library",
            "Thoughtful and creative": "Monona Terrace",
            "Laid-back and reliable": "Dotty Dumpling's Dowry"
        }
    },
    {
        "question": "What matters most in a favorite spot?",
        "options": {
            "People and energy": "State Street",
            "Comfort and tradition": "The Old Fashioned",
            "Peace and space": "Monona Terrace",
            "Productivity": "Memorial Library"
        }
    }
]

# ---------------- IMAGES ----------------
images = {
    "Memorial Union Terrace": "https://www.joegarzaphotography.com/images/xl/OnWisconsin.jpg",
    "State Street": "https://onwisconsin.uwalumni.com/content/uploads/2021/10/BascHill_autumn16_2774.jpg",
    "Memorial Library": "https://news.wisc.edu/content/uploads/2017/11/Law_Library_autumn13_4363.jpg",
    "Monona Terrace": "https://wrightinwisconsin.org/sites/default/files/RGB_Monona_Terrace.jpg",
    "The Old Fashioned": "https://share.google/L8ZJr0BIQMt5BDpbh",
    "Dotty Dumpling's Dowry": "https://bloximages.newyork1.vip.townnews.com/channel3000.com/content/tncms/assets/v3/editorial/c/13/c138a8de-3d5a-11ef-ad8b-83bf20e66695/668c34a2f0a1c.image.jpg?resize=540%2C304"
}

# ---------------- TITLE ----------------
st.title("Which Madison Spot Are You?")

# ---------------- PROGRESS ----------------
st.progress(st.session_state.question / len(questions))

# ---------------- QUIZ FLOW ----------------
if st.session_state.question < len(questions):
    q = questions[st.session_state.question]

    choice = st.radio(
        q["question"],
        list(q["options"].keys()),
        key=st.session_state.question
    )

    if st.button("Next"):
        result = q["options"][choice]
        st.session_state.scores[result] += 1
        st.session_state.question += 1
        st.rerun()

# ---------------- RESULTS ----------------
else:
    final = max(st.session_state.scores, key=st.session_state.scores.get)
    st.balloons()
   
    explanations = {
        "Memorial Union Terrace": "You thrive on connection and balance. You’re the “let’s all sit together” friend and yes, you grabbed a Terrace chair first.",
        "State Street": "You’re energized by movement and variety. Standing still isn’t your thing, there’s always something happening where you belong.",
        "Memorial Library": "Focused, disciplined, and goal-oriented. You don’t romanticize all-nighters, but if one happens, you’re surviving it here.",
        "Monona Terrace": "Reflective and creative, you appreciate space to think. You’re not avoiding people, you’re just having a main-character moment.",
        "The Old Fashioned": "Classic, comfortable, and dependable. You value tradition, good food, and conversations that last.",
        "Dotty Dumpling's Dowry": "Chill and low-key, you care more about comfort than aesthetics. And yes — you’re ordering a burger at an unreasonable hour."
    }

    st.subheader(f"You got: **{final}**")
    st.image(images[final], use_container_width=True)
    st.write(explanations[final])
st.markdown("""
### Why UW–Madison Fits Me

I understand that my transcript does not fully reflect my potential as a student. Throughout high school, I balanced school with significant responsibilities outside the classroom, including working long hours to help support my family and taking on caregiving roles for my grandparents when they needed me. These experiences shaped my priorities and required a level of responsibility that challenged me in ways that extended beyond academics.
            
While my grades are part of my story, they do not define who I am or the kind of student I know I can be. I am motivated, resilient, and eager to challenge myself in an environment that holds high expectations while still offering support and community. That balance is exactly what draws me to UW–Madison.
            
I built this project because UW–Madison is a place I can genuinely see myself. As a student, I learn best in environments that push me to grow while also making me feel connected to the people around me. Working on this quiz allowed me to reflect on how much I value community, independence, and personal growth qualities that UW–Madison encourages through its campus culture and student life. I don’t just want to attend a university; I want to contribute to a community where students are motivated, curious, and proud of where they are.
            
This project represents how I think, create, and problem-solve as a student, as well as my genuine interest in UW–Madison. Given the opportunity, I am confident that UW–Madison would be the right environment for me to grow both academically and personally, and I am ready to fully commit to the challenges and opportunities it offers.

— Emily Mendoza Dominguez

""")

if st.button("Restart Quiz"):
        st.session_state.question = 0
        for k in st.session_state.scores:
            st.session_state.scores[k] = 0
        st.rerun()
