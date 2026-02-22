import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import time
from pathlib import Path
import base64
import pandas as pd
from streamlit_autorefresh import st_autorefresh
st.set_page_config(page_title="Prachin Lipi Abhyas", layout="wide", initial_sidebar_state="auto")
# Top banner
st.markdown("""
<style>
.top-banner {
    width: 100%;
    height: 80px;            /* 2–3 cm approx */
    background: linear-gradient(90deg, #8b6f47, #c9a66b);
    display: flex;
    align-items:center ;
    justify-content: center;
    font-size: 34px;
    font-weight: bold;
    color: white;
    letter-spacing: 2px;
    border-radius: 0 0 10px 10px;
    margin-bottom: 10px;
}
</style>

<div class="top-banner">
    Prachin Lipi Abhyas (प्राचीन लिपि अभ्यास)
</div>
""", unsafe_allow_html=True)
brahmi_flashcards = [
    {
        "front": "ब्राह्मी लिपि",
        "back": "प्राचीन भारत की अत्यंत महत्वपूर्ण लिपि, जिससे अनेक एशियाई लिपियों का विकास हुआ।"
    },
    {
        "front": "खोज",
        "back": "1837 ई. में जेम्स प्रिंसेप ने ब्राह्मी लिपि को पढ़ा।"
    },
    {
        "front": "अशोक अभिलेख",
        "back": "तीसरी शताब्दी ईसा पूर्व के शिलालेखों में ब्राह्मी का श्रेष्ठ प्रयोग।"
    },
    {
        "front": "लेखन दिशा",
        "back": "बाएँ से दाएँ लिखी जाने वाली लिपि।"
    }
]

sharada_flashcards = [
    {
        "front": "शारदा लिपि",
        "back": "शारदा लिपि उत्तर भारत में प्रचलित एक प्राचीन लिपि है, जिसका प्रयोग मुख्यतः कश्मीर क्षेत्र में हुआ।"
    },
    {
        "front": "उत्पत्ति",
        "back": "यह लिपि ब्राह्मी से विकसित हुई और संस्कृत ग्रंथों के लेखन में उपयोगी रही।"
    },
    {
        "front": "प्रयोग क्षेत्र",
        "back": "कश्मीर, हिमाचल प्रदेश तथा पंजाब के कुछ भागों में इसका प्रयोग हुआ।"
    },
    {
        "front": "काल",
        "back": "8वीं से 12वीं शताब्दी के बीच इसका व्यापक प्रयोग हुआ।"
    },
]
# ---------------------------
# Background Styling
# ---------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fdf6e3;
    }
    section[data-testid="stSidebar"] {
        background-color: #f5e6cc;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
<style>
header {visibility: hidden;}
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
.block-container {
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)


def show_flashcards(cards):
    # Initialize session state
    if "card_index" not in st.session_state:
        st.session_state.card_index = 0
    if "flipped" not in st.session_state:
        st.session_state.flipped = False

    card = cards[st.session_state.card_index]
    flip_class = "flipped" if st.session_state.flipped else ""

    # Card HTML
    st.markdown(f"""
<style>
.card-wrapper {{
    display: flex;
    justify-content: center;
    margin-top: 40px;
}}

.card-container {{
    perspective: 1000px;
    width: 420px;
    height: 260px;
}}

.card {{
    width: 100%;
    height: 100%;
    position: relative;
    transform-style: preserve-3d;
    transition: transform 0.6s;
}}

.card.flipped {{
    transform: rotateY(180deg);
}}

.card-face {{
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    backface-visibility: hidden;
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    padding: 25px;
    text-align: center;
    background: white;
    border: 2px solid #bbb;
    box-sizing: border-box;
}}

.card-back {{
    transform: rotateY(180deg);
    background: #f3e5c3;
}}
</style>

<div class="card-wrapper">
    <div class="card-container">
        <div class="card {flip_class}">
            <div class="card-face">
                {card['front']}
            </div>
            <div class="card-face card-back">
                {card['back']}
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    # Buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("⬅ Previous"):
            if st.session_state.card_index > 0:
                st.session_state.card_index -= 1
                st.session_state.flipped = False
                st.rerun()

    with col2:
        if st.button("🔄 Flip"):
            st.session_state.flipped = not st.session_state.flipped
            st.rerun()

    with col3:
        if st.button("Next ➡"):
            if st.session_state.card_index < len(cards) - 1:
                st.session_state.card_index += 1
                st.session_state.flipped = False
                st.rerun()


# ---------------------------
# Sidebar Menu
# ---------------------------
#st.sidebar.title("Navigation Bar")
#st.sidebar.markdown("<br><br>", unsafe_allow_html=True)
st.sidebar.image("logo.png", width=200)
main_option = st.radio(
    "",
    ["🏠 Home", "📜 Brahmi", "📖 Sharada", "🎮 Game Zone", "🔗 Important Links"], horizontal=True
)
st.markdown("""
<style>
section[data-testid="stSidebar"] .stRadio > div {
    gap: 20px;
}
</style>
""", unsafe_allow_html=True)
# ---------------------------
# Lipi Vikas Section
# ---------------------------
if main_option == "🏠 Home":
    

  st.markdown("## 📜 लिपि विकास (Evolution of Scripts)")

  st.write("""
सामान्य अर्थ में **लिपि विकास** मानव सभ्यता के संचार का सबसे क्रांतिकारी पड़ाव है।  
यह ध्वनि (Sound) को दृश्य रूप (Visual Form) देने की यात्रा है।
""")

  st.divider()

# -----------------------------
# 1️⃣ Evolution Stages Chart
# -----------------------------

  st.subheader("🔄 विकास के प्रमुख चरण")

  st.write("लिपियों का विकास एक क्रमिक प्रक्रिया रही है:")

  st.markdown("""
1. 🖼 **चित्र लिपि (Pictographic)**  
2. 💡 **भाव लिपि (Ideographic)**  
3. 🔤 **ध्वन्यात्मक लिपि (Phonetic/Alphabetic)**
 
""")



  st.divider()

# -----------------------------
# 2️⃣ Indian Script Tree
# -----------------------------

  st.subheader("भारतीय लिपियों का विकास")

  st.markdown("""
भारत में लगभग सभी लिपियों की जननी **ब्राह्मी लिपि** मानी जाती है।
""")

  st.markdown("""
📜 ब्राह्मी → गुप्त → कुटिल/सिद्धमात्रिका  
↙️ उत्तरी शाखा → देवनागरी, शारदा, गुरुमुखी, बंगाली  
↘️ दक्षिणी शाखा → तमिल, तेलुगु, कन्नड़, मलयालम
""")

  st.divider()

# -----------------------------
# 3️⃣ Influencing Factors
# -----------------------------

  st.subheader("⚙️ लिपि विकास को प्रभावित करने वाले कारक")

  col1, col2 = st.columns(2)

  with col1:
    st.markdown("### 🪨 लेखन सामग्री")
    st.write("""
    • पत्थर → कोणीय अक्षर  
    • भोजपत्र/कागज़ → गोलाकार अक्षर
    """)

  with col2:
    st.markdown("### 🗣 भाषा परिवर्तन")
    st.write("""
    • नई ध्वनियाँ  
    • नुक्ता का विकास  
    • लेखन गति
    """)

  st.divider()

# -----------------------------
# 4️⃣ Technical Features
# -----------------------------
  st.subheader("🔬 महत्वपूर्ण तकनीकी बदलाव")

  st.markdown("""
• **शिरोरेखा** – उत्तर भारतीय लिपियों में  
• **मात्रा व्यवस्था** – स्वर और व्यंजन का वैज्ञानिक वर्गीकरण  
""")

  st.divider()

  #st.success("📚 लिपि विकास जटिलता से सरलता की ओर एक ऐतिहासिक यात्रा है।")

  #st.info("👉 क्या आप किसी विशेष लिपि का कालक्रम विस्तार से देखना चाहेंगे?")

# ---------------------------
# Function for Alphabets
# ---------------------------
def show_alphabets(script_name):
    
    if script_name == "Sharada":
        #st.header(f"{script_name} Alphabets")

        st.subheader("Vowels")
        vowels =["अ (𑆃)", "आ (𑆄)", "इ (𑆅)", "ई (𑆆)", 
                 "उ (𑆇)", "ऊ (𑆈)", "ऋ (𑆉)", "ॠ(𑆊)", "ऌ (𑆋)","ॡ(𑆌)","ए (𑆍)", "ऐ (𑆎)", "ओ (𑆏)", "औ (𑆐)","अं(𑆃𑆁)", "अ:(𑆃:)"]  
       
        st.markdown(
    "<div style='font-size:28px; letter-spacing:10px;'>"
    + " ".join(vowels) +
    "</div>",
    unsafe_allow_html=True)
        st.divider()
        st.subheader("Consonants")



        st.markdown(
    """
    <div style='font-size:28px; line-height:2.2;'>
    क वर्ग:&nbsp;&nbsp;  𑆑 (क), 𑆒 (ख), 𑆓 (ग), 𑆔 (घ), 𑆕 (ङ)<br>
    च वर्ग:&nbsp;&nbsp;  𑆖 (च), 𑆗 (छ), 𑆘 (ज), 𑆙 (झ), 𑆚 (ञ)<br>
    ट वर्ग:&nbsp;&nbsp;  𑆛 (ट), 𑆜 (ठ), 𑆝 (ड), 𑆞 (ढ), 𑆟 (ण)<br>
    त वर्ग:&nbsp;&nbsp;  𑆠 (त), 𑆡 (थ), 𑆢 (द), 𑆣 (ध), 𑆤 (न)<br>
    प वर्ग:&nbsp;&nbsp;  𑆥 (प), 𑆦 (फ), 𑆧 (ब), 𑆨 (भ), 𑆩 (म)<br>
    अन्य:&nbsp;&nbsp;   𑆪 (य), 𑆫 (र), 𑆬 (ल), 𑆭 (व), 𑆮 (श), 𑆯 (ष), 𑆰 (स), 𑆱 (ह)
    </div>
    """,
    unsafe_allow_html=True
)

        st.divider()
        st.subheader("Matras")
        st.markdown(
    """
    <div style='font-size:28px; line-height:2.2;'>
    का — 𑆑𑆳,&nbsp;&nbsp  कि — 𑆑𑆴,&nbsp;&nbsp  की — 𑆑𑆵,&nbsp;&nbsp  कु — 𑆑𑆶 ,&nbsp;&nbsp कू — 𑆑𑆷 ,&nbsp;&nbsp कृ — 𑆑𑆸  ,&nbsp;&nbsp के — 𑆑𑆼 ,&nbsp;&nbsp कै — 𑆑𑆽,&nbsp;&nbsp  को — 𑆑𑆾,&nbsp;&nbsp  कौ — 𑆑𑆿 ,&nbsp;&nbsp कं — 𑆑𑆁 ,&nbsp;&nbsp कः — 𑆑𑆂   </div>
    """,
    unsafe_allow_html=True
)

    else:
            st.subheader("Vowels")
            vowels =["अ (𑆃)", "आ (𑀆)", "इ (𑀇)", "ई (::)", 
                 "उ (𑀉)", "ऊ (𑀊)", "ए (𑀏)", "ऐ (𑀐)", "ओ (𑀑)", "औ (𑀒)", "अं (𑀅𑀁)", "अः(𑀅:)" ]  
       
            st.markdown(
            "<div style='font-size:28px; letter-spacing:10px;'>"
          + " ".join(vowels) +
          "</div>",
            unsafe_allow_html=True)
            st.divider()
            st.subheader("Consonants")



            st.markdown(
    """
    <div style='font-size:28px; line-height:2.2;'>
    क वर्ग:&nbsp;&nbsp;  क (𑀓), ख (𑀔), ग (𑀕), घ (𑀖), ङ (𑀗)<br>
    च वर्ग:&nbsp;&nbsp;  च (𑀘), छ (𑀙), ज (𑀚), झ (𑀛), ञ (𑀜)<br>
    ट वर्ग:&nbsp;&nbsp;  ट (𑀝), ठ (𑀞), ड (𑀟), ढ (𑀠), ण (𑀡)<br>
    त वर्ग:&nbsp;&nbsp;  त (𑀢), थ (𑀣), द (𑀤), ध (𑀥), न (𑀦)<br>
    प वर्ग:&nbsp;&nbsp;  प (𑀧), फ (𑀨), ब (𑀩), भ (𑀪), म (𑀫)<br>
    अन्य:&nbsp;&nbsp;   य (𑀬), र (𑀭), ल (𑀮), व (𑀯), श (𑀰), ष (𑀱), स (𑀲), ह (𑀳)
    </div>
    """,
            unsafe_allow_html=True)

            st.divider()
            st.subheader("Matras")
            st.markdown(
    """
    <div style='font-size:28px; line-height:2.2;'>
 क — 𑀓,&nbsp;&nbsp  का — 𑀓𑀸,&nbsp;&nbsp  कि — 𑀓𑀹,&nbsp;&nbsp  की — 𑀓𑀺,&nbsp;&nbsp  कु — 𑀓𑀼 ,&nbsp;&nbsp कू — 𑀓𑀽  ,&nbsp;&nbsp के — 𑀓𑁂 ,&nbsp;&nbsp कै — 𑀓𑁃,&nbsp;&nbsp  को — 𑀓𑁄,&nbsp;&nbsp  कौ — 𑀓𑁅 ,&nbsp;&nbsp कं — 𑀓𑀁 ,&nbsp;&nbsp कः — 𑀓𑀂   </div>
    """,
            unsafe_allow_html=True
        )

    #cols = st.columns(6)
    #for i, char in enumerate(alphabets):
     #   cols[i % 6].markdown(
     ##       f"<h2 style='text-align:center'>{char}</h2>",
       #     unsafe_allow_html=True
     #   )

# ---------------------------
# Function for Quiz
# ---------------------------
import streamlit as st
import time

def run_quiz(script_name):

    # -------------------------
    # Script-Specific Keys
    # -------------------------
    start_key = f"{script_name}_start"
    q_index_key = f"{script_name}_q_index"
    score_key = f"{script_name}_score"
    finished_key = f"{script_name}_finished"
    timer_key = f"{script_name}_timer"
    show_score_key = f"{script_name}_show_score"

    # -------------------------
    # Question Bank
    # -------------------------
    if script_name == "📜 Brahmi":
        quiz_questions = [
            {
                "question": "ब्राह्मी लिपि के संबंध में 'ललित विस्तर' में क्या उल्लेख मिलता है?",
                "options": [
                    "केवल खरोष्ठी का उल्लेख",
                    "विदेशी लिपियों का वर्णन",
                    "लिपियों की सूची में ब्राह्मी का प्रथम स्थान",
                    "लिपि को पढ़ने की मनाही"
                ],
                "answer": "लिपियों की सूची में ब्राह्मी का प्रथम स्थान"
            },
            {
                "question": "ब्राह्मी लिपि में 'अ' वर्ण की आकृति किससे मिलती-जुलती है?",
                "options": [
                    "अंग्रेजी के 'K' अक्षर से",
                    "अंग्रेजी के 'O' अक्षर से",
                    "गणित के '+' चिह्न से",
                    "हिंदी के 'न' अक्षर से"
                ],
                "answer": "अंग्रेजी के 'K' अक्षर से"
            },
            {
                "question": "सम्राट अशोक ने ब्राह्मी लिपि को किस नाम से पुकारा?",
                "options": ["प्राकृत लिपि", "अशोक लिपि", "धम्मलिपि", "देवनागरी"],
                "answer": "धम्मलिपि"
            },
            { 
            "question": "ब्राह्मी लिपि में 'ब' वर्ण को किस ज्यामितीय आकृति द्वारा पहचाना जा सकता है?", 
             "options": ["वर्ग (Square)", "बिंदु (Dot)", "त्रिभुज (Triangle)", "वृत्त (Circle)"], 
             "answer": "वर्ग (Square)"
            },
            { 
                "question": "ब्राह्मी लिपि में स्वर 'इ' (I) को दर्शाने के लिए किसका प्रयोग किया जाता था?", 
             "options": ["एक बड़े शून्य का", "दो खड़ी रेखाओं का", "तीन बिंदुओं का (त्रिभुज के आकार में)", "एक सीधी रेखा का"], 
             "answer": "तीन बिंदुओं का (त्रिभुज के आकार में)"
               },
        ]
    else:
        quiz_questions = [
            {
                "question": "शारदा लिपि का मुख्य काल कौन सा है?",
                "options": [
                    "ईसा पूर्व तीसरी शताब्दी",
                    "8वीं से 12वीं शताब्दी",
                    "15वीं से 18वीं शताब्दी",
                    "आधुनिक काल"
                ],
                "answer": "8वीं से 12वीं शताब्दी"
            },
            {
                "question": "शारदा पीठ कहाँ स्थित था?",
                "options": ["काँजीपुरम", "कश्मीर", "नालंदा", "तमिलनाडु"],
                "answer": "कश्मीर"
            },
            {
                "question": "टाकरी लिपि किससे विकसित हुई?",
                "options": ["तमिल", "शारदा", "तेलुगु", "ब्राह्मी"],
                "answer": "शारदा"
            },
            { "question": "शारदा लिपि में लिखी गई पांडुलिपियाँ (Manuscripts) अधिकांशतः किस सामग्री पर पाई जाती हैं?", 
             "options": ["कागज ", "ताड़पात्र", "भूर्जपात्र", "वस्त्र"], "answer": "भूर्जपात्र" },
             { "question": "शारदा लिपि में 'उ' (U) की मात्रा व्यंजन के साथ कहाँ जुड़ती है?",
               "options": ["अक्षर के नीचे ", "अक्षर के ऊपर ", "अक्षर के बराबर में ", "इनमें से कोई नहीं "], 
               "answer": "अक्षर के नीचे" }

        ]

    total_questions = len(quiz_questions)

    # -------------------------
    # Initialize State
    # -------------------------
    if start_key not in st.session_state:
        st.session_state[start_key] = False
    if q_index_key not in st.session_state:
        st.session_state[q_index_key] = 0
    if score_key not in st.session_state:
        st.session_state[score_key] = 0
    if finished_key not in st.session_state:
        st.session_state[finished_key] = False
    if show_score_key not in st.session_state:
        st.session_state[show_score_key] = False

    # -------------------------
    # Instruction Screen
    # -------------------------
    if not st.session_state[start_key]:
        st.info("• Each question has 10 seconds.\n\n• Select one correct answer.\n\n• Quiz has multiple questions.")

        if st.button("Start Quiz"):
            st.session_state[start_key] = True
            st.session_state[q_index_key] = 0
            st.session_state[score_key] = 0
            st.session_state[finished_key] = False
            st.session_state[show_score_key] = False
            st.session_state[timer_key] = time.time()
            st.rerun()
        return

    # -------------------------
    # After Quiz Finished
    # -------------------------
    if st.session_state[finished_key]:

        score = st.session_state[score_key]
        percentage = int((score / total_questions) * 100)

        st.success(f"🎯 Your Score: {score} / {total_questions}")
        st.write(f"📊 Percentage: {percentage}%")

        # Badge System
        if percentage >= 80:
            st.markdown("🥇 **Gold Badge – Excellent!**")
        elif percentage >= 50:
            st.markdown("🥈 **Silver Badge – Good Job!**")
        else:
            st.markdown("🥉 **Bronze Badge – Keep Practicing!**")

        if st.button("Restart Quiz"):
            st.session_state[start_key] = False
            st.session_state[q_index_key] = 0
            st.session_state[score_key] = 0
            st.session_state[finished_key] = False
            st.session_state[show_score_key] = False
            st.rerun()

        return

    # -------------------------
    # Quiz Running
    # -------------------------
    q_index = st.session_state[q_index_key]
    current_q = quiz_questions[q_index]

    # Timer
    time_elapsed = int(time.time() - st.session_state[timer_key])
    time_left = max(0, 10 - time_elapsed)

    st.write(f"⏱ Time left: {time_left} seconds")
    st.write(f"Question {q_index + 1} of {total_questions}")

    answer = st.radio(
        current_q["question"],
        current_q["options"],
        key=f"{script_name}_answer_{q_index}"
    )

    # Submit or Timeout
    if st.button("Submit") or time_left == 0:

        selected = st.session_state.get(
            f"{script_name}_answer_{q_index}", None
        )

        if selected == current_q["answer"]:
            st.session_state[score_key] += 1

        st.session_state[q_index_key] += 1

        if st.session_state[q_index_key] >= total_questions:
            st.session_state[finished_key] = True
        else:
            st.session_state[timer_key] = time.time()

        st.rerun()

    # Auto refresh for timer
    if time_left > 0:
        time.sleep(1)
        st.rerun()




# ---------------------------
# Practice Area
# ---------------------------
def practice_area(script_name):
    st.header(f"{script_name} Practice Area")
    st.write("Draw inside the grid to practice the script.")

    # Controls
    stroke_width = st.slider("Stroke width", 1, 10, 3)
    stroke_color = st.color_picker("Stroke color", "#000000")

    # Canvas
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.0)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color="#ffffff",
        height=400,
        width=1050,
        drawing_mode="freedraw",
        key=f"canvas_{script_name}",
        display_toolbar=True
    )

def show_brahmi_introduction():
    st.subheader("Brahmi Lipi Introduction")

    # Flashcards
    show_flashcards(brahmi_flashcards)

    st.markdown("---")

    # Main intro
    st.markdown("""
    <div style="background:#fff8e1; padding:20px; border-radius:12px;">
    <h3>ब्राह्मी लिपि का परिचय</h3>
    ब्राह्मी लिपि प्राचीन भारत की एक अत्यंत महत्वपूर्ण लिपि है,
    जिसने कई एशियाई लिपियों के विकास की आधारशिला रखी।
    </div>
    """, unsafe_allow_html=True)

    # Historical background
    st.markdown("""
    <div style="background:#e3f2fd; padding:20px; border-radius:12px; margin-top:10px;">
    <h4>ऐतिहासिक पृष्ठभूमि और खोज</h4>
    <ul>
        <li><b>पुनरुद्धार:</b> 1837 ई. में जेम्स प्रिंसेप ने ब्राह्मी को पढ़ा।</li>
        <li><b>प्रथम शब्द:</b> साँची स्तूप पर 'दानं' शब्द पहचाना।</li>
        <li><b>अशोक शिलालेख:</b> तीसरी शताब्दी ईसा पूर्व के अभिलेख।</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    

# ---------------------------
# Brahmi Section
# ---------------------------
if main_option == "📜 Brahmi":
    sub_option = st.sidebar.radio(
        "Brahmi Options",
        ("Introduction","Alphabets", "Quiz", "Practice Area")
    )

    st.title("Brahmi Lipi")
    if sub_option == "Introduction":
        show_brahmi_introduction()
    elif sub_option == "Alphabets":
        show_alphabets("Brahmi")
    elif sub_option == "Quiz":
        run_quiz("📜 Brahmi")
    elif sub_option == "Practice Area":
        practice_area("Brahmi")

# ---------------------------
# Sharada Section
# ---------------------------
if main_option == "📖 Sharada":
    sub_option = st.sidebar.radio(
        "Sharada Options",
        ("Introduction", "Alphabets", "Quiz", "Practice Area")
    )

    st.title("Sharada Lipi")

    if sub_option == "Introduction":
        show_flashcards(sharada_flashcards)
    elif sub_option == "Alphabets":
        show_alphabets("Sharada")
    elif sub_option == "Quiz":
        run_quiz("📖 Sharada")
    elif sub_option == "Practice Area":
        practice_area("Sharada")


# ---------------------------
# Floating Rotating Image
# ---------------------------
def floating_rotating_image(image_path, width=30):
    with open(image_path, "rb") as img_file:
        img_bytes = img_file.read()
        encoded = base64.b64encode(img_bytes).decode()

    html = f"""
    <style>
    .float-rotate {{
        animation: floatRotate 4s ease-in-out infinite;
    }}
    @keyframes floatRotate {{
        0%   {{ transform: translateY(0px) rotate(0deg); }}
        100%  {{ transform: translateY(-12px) rotate(0deg); }}
        50%  {{ transform: translateY(0px) rotate(0deg); }}
        75%  {{ transform: translateY(-12px) rotate(-4deg); }}
        100% {{ transform: translateY(0px) rotate(0deg); }}
    }}
    </style>
    <div style="text-align:center;">
        <img src="data:image/png;base64,{encoded}" 
             class="float-rotate" width="{width}">
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# ---------------------------
# Game Module
# ---------------------------


def show_game():

    st.markdown("<h1 style='text-align:center;'>🎮 Brahmi/Sharada Word Challenge</h1>", unsafe_allow_html=True)

    # ---- Game Data ----
    game_data = [
        {"image": "1.png", "answer": "कमल"},
        {"image": "2.png", "answer": "लिपिकार"},
        {"image": "3.png", "answer": "लिपिकार"},
        {"image": "4.png", "answer": "शीतल"},
        {"image": "5.png", "answer": "मूलपाठ "},
        {"image": "6.png", "answer": "नीति "},
        {"image": "7.png", "answer": "खिलौना "},
        {"image": "8.png", "answer": "सुविधि "},
        {"image": "9.png", "answer": "शिलालेख "},
    ]

    # ---- Session State ----
    total_questions = len(game_data)

    # ---------------- SESSION STATE ----------------
    defaults = {
        "game_started": False,
        "level": 1,
        "score": 0,
        "index": 0,
        "start_time": None
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

    # ---------------- INSTRUCTIONS PAGE ----------------
    if not st.session_state.game_started:

        st.markdown("""
        <div style="background:#fff3e0;padding:20px;border-radius:12px;">
        <h3>📜 Instructions</h3>
        <ul>
            <li>Identify the word shown in Brahmi/Sharada script.</li>
            <li>Type answer in <b>Devanagari only</b>.</li>
            <li>You have maximum <b>20 seconds</b> per question.</li>
            <li>This game has <b>3 levels</b>.</li>
            <li>Rotation speed increases at each level.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚀 Start Game"):
            st.session_state.game_started = True
            st.session_state.start_time = time.time()
            st.rerun()

        return

    # ---------------- GAME OVER ----------------
    if st.session_state.index >= total_questions:

        score = st.session_state.score
        percentage = round((score / total_questions) * 100)

        # Badge Logic
        if percentage >= 90:
            badge = "🏆 Lipi Master"
            message = "Outstanding! You have mastered the script!"
            st.balloons()
        elif percentage >= 70:
            badge = "🥇 Lipi Scholar"
            message = "Excellent performance!"
        elif percentage >= 50:
            badge = "🥈 Script Learner"
            message = "Good effort! Keep practicing!"
        else:
            badge = "📘 Beginner"
            message = "Keep learning. Practice makes perfect!"

        st.markdown("""
        <div style="background:#f0f9ff;padding:30px;border-radius:20px;text-align:center;">
        """, unsafe_allow_html=True)

        st.markdown(f"## 🎯 Final Score: {score}/{total_questions}")
        st.markdown(f"### 📊 Percentage: {percentage}%")
        st.markdown(f"## {badge}")
        st.markdown(f"### {message}")

        st.markdown("</div>", unsafe_allow_html=True)

        if st.button("🔄 Restart Game"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

        return

    # ---------------- LEVEL CONTROL ----------------
    if st.session_state.index == 3:
        st.session_state.level = 2
    elif st.session_state.index == 6:
        st.session_state.level = 3

    rotation_speed = {
        1: "8s",
        2: "4s",
        3: "2s"
    }

    st.subheader(f"Level {st.session_state.level}")

    # ---------------- IMAGE DISPLAY ----------------
    def get_base64_image(path):
        with open(path, "rb") as img:
            return base64.b64encode(img.read()).decode()

    current = game_data[st.session_state.index]
    image_base64 = get_base64_image(current["image"])

    st.markdown(f"""
        <style>
        .rotate {{
            animation: rotation {rotation_speed[st.session_state.level]} infinite linear;
        }}
        @keyframes rotation {{
            from {{ transform: rotate(0deg); }}
            to {{ transform: rotate(360deg); }}
        }}
        </style>
        <div style="text-align:center;">
            <img src="data:image/png;base64,{image_base64}" class="rotate" width="350">
        </div>
    """, unsafe_allow_html=True)

    # ---------------- TIMER ----------------
    st_autorefresh(interval=1000, key="timer_refresh")

    if st.session_state.start_time is None:
        st.session_state.start_time = time.time()

    remaining = 20  - int(time.time() - st.session_state.start_time)

    if remaining <= 0:
        st.warning("⏰ Time Up!")
        st.session_state.index += 1
        st.session_state.start_time = time.time()
        st.rerun()

    st.info(f"⏳ Time Remaining: {remaining} seconds")

    # ---------------- INPUT ----------------
    user_answer = st.text_input(
        "Type answer in Devanagari:",
        key=f"answer_{st.session_state.index}"
    )

    # ---------------- SUBMIT ----------------
    if st.button("Submit"):

        correct = current["answer"]

        if user_answer.strip() == correct.strip():
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Wrong! Correct answer: {correct}")

        st.session_state.index += 1
        st.session_state.start_time = time.time()

        st.rerun()

#------------------------
# Important Links
#----------------------=

def show_important_links():
    import streamlit as st
    import pandas as pd

    st.markdown(
        "<h1 style='text-align:center;'>🔗 Important Government Links</h1>",
        unsafe_allow_html=True
    )

    links_data = [
        {"Name": "Dharohar Portal",
         "Description": "Indian cultural heritage documentation portal.",
         "Link": "https://dharohar.gov.in"},
        
        {"Name": "Gyan Bharatam",
         "Description": "Indian knowledge systems initiative.",
         "Link": "https://gyanbharatam.gov.in"},
        {"Name": "Ministry of Culture",
         "Description": "Official website of Ministry of Culture, India.",
         "Link": "https://indiaculture.gov.in"},
       
    ]

    df = pd.DataFrame(links_data)

    # Make full link clickable
    df["Link"] = df["Link"].apply(
        lambda x: f'<a href="{x}" target="_blank">{x}</a>'
    )

    table_html = df.to_html(escape=False, index=False)

    # Center headers
    table_html = table_html.replace(
        "<th>",
        "<th style='text-align:center; background-color:#d7ccc8; padding:10px;'>"
    )

    centered_table = f"""
    <div style="display:flex; justify-content:center; margin-top:30px;">
        <div style="width:85%;">
            {table_html}
        </div>
    </div>
    """

    st.markdown(centered_table, unsafe_allow_html=True)
   
if main_option == "🔗 Important Links":
    show_important_links()

if main_option == "🎮 Game Zone":
    show_game()




