import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import time
from pathlib import Path
import base64
import pandas as pd
from streamlit_autorefresh import st_autorefresh
st.set_page_config(page_title="Prachin Lipi Abhyas", layout="wide", initial_sidebar_state="auto")
st.markdown("""
<style>

/* Target radio option container */
div[data-testid="stRadio"] label {
    font-size: 20px !important;
    font-weight: 600 !important;
}

/* Increase spacing between options */
div[data-testid="stRadio"] > div {
    gap: 12px;
}

/* Make radio circle slightly bigger */
div[data-testid="stRadio"] input[type="radio"] {
    transform: scale(1.3);
    margin-right: 10px;
}

</style>
""", unsafe_allow_html=True)

def set_background(image_url):
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }}
    </style>
    """, unsafe_allow_html=True)


# Top banner

st.markdown("""
<div style="
    text-align:center;
    padding:25px;
    background: linear-gradient(90deg, #8B6F3D, #C2A36B);
    color:white;
    border-radius:15px;
    font-size:38px;
    font-weight:700;">
    📜 PRACHIN LIPI ABHYAS (प्राचीन लिपि अभ्यास)
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
#st.markdown('<div class="section-heading">ब्राह्मी लिपि का परिचय</div>', unsafe_allow_html=True)



# ---------------------------
# Sidebar Menu
# ---------------------------
#st.sidebar.title("Navigation Bar")
#st.sidebar.markdown("<br><br>", unsafe_allow_html=True)
st.sidebar.image("logo.png", width=200)

with st.sidebar:
 main_option = st.sidebar.radio(
    "",
    ("🏠 Home", "📜 Brahmi", "📖 Sharada", "🎮 Game Zone", "🔗 Important Links", "🔁 Transliteration")
)

#main_option = st.radio(
   # "",
   # ["🏠 Home", "📜 Brahmi", "📖 Sharada", "🎮 Game Zone", "🔗 Important Links"], horizontal=True
#)
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

def show_home():

    st.markdown("""
    <div style="
        background: #FBF6ED;
        padding: 40px;
        border-radius: 18px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        border-left: 8px solid #8B6F3D;
    ">

    <h1 style="
        text-align:center;
        color:#5C4326;
        font-weight:700;
        letter-spacing:1px;">
        📜 भारतीय लिपि-विकास की गौरवगाथा
    </h1>

    <hr style="border:1px solid #C2A36B;">

    <p style="text-align:justify; font-size:19px; line-height:1.8;">
    भारतवर्ष की ज्ञान-परंपरा अत्यंत समृद्ध एवं बहुआयामी रही है। 
    वैदिक ऋचाओं से लेकर दार्शनिक ग्रंथों, अभिलेखों तथा पांडुलिपियों तक 
    विचारों के संरक्षण एवं प्रसार के लिए लिपि ने महत्वपूर्ण भूमिका निभाई। 
    लिपि केवल लेखन का माध्यम नहीं, बल्कि सांस्कृतिक निरंतरता का सेतु है।
    </p>

    <h3 style="color:#6F5630;"> ब्राह्मी : प्राचीन आधारशिला</h3>
    <p style="text-align:justify; font-size:18px; line-height:1.8;">
    ब्राह्मी लिपि भारतीय उपमहाद्वीप की प्राचीनतम लिपियों में से एक मानी जाती है। 
    सम्राट अशोक के शिलालेखों में इसका व्यवस्थित एवं व्यापक प्रयोग दृष्टिगोचर होता है। 
    उत्तर एवं दक्षिण भारत की अधिकांश लिपियाँ ब्राह्मी की उत्तराधिकारी मानी जाती हैं।
    </p>

    <h3 style="color:#6F5630;">क्षेत्रीय विकास एवं विविधता</h3>
    <p style="text-align:justify; font-size:18px; line-height:1.8;">
    कालांतर में ब्राह्मी से विविध क्षेत्रीय लिपियों का विकास हुआ। 
    उत्तर भारत में शारदा एवं नागरी, 
    जबकि दक्षिण भारत में ग्रन्थ, कन्नड़, तेलुगु एवं तमिल लिपियों का स्वरूप विकसित हुआ। 
    प्रत्येक लिपि अपने क्षेत्र की सांस्कृतिक पहचान का प्रतीक बनी।
    </p>

    <h3 style="color:#6F5630;"> सांस्कृतिक एवं दार्शनिक आयाम</h3>
    <p style="text-align:justify; font-size:18px; line-height:1.8;">
    भारतीय लिपियों का अध्ययन केवल भाषिक अनुसंधान तक सीमित नहीं है। 
    यह हमारी दार्शनिक दृष्टि, सामाजिक संरचना, धार्मिक परंपराओं 
    तथा ज्ञान-संरक्षण की प्रणाली को समझने का महत्वपूर्ण माध्यम है। 
    पांडुलिपि-विज्ञान, अभिलेख-विज्ञान तथा भाषावैज्ञानिक अध्ययन में 
    लिपि का विशिष्ट स्थान है।
    </p>

    <blockquote style="
        font-size:20px;
        font-style:italic;
        color:#5C4326;
        border-left:4px solid #8B6F3D;
        padding-left:15px;
        margin-top:25px;">
        ‘लिपिः संस्कृतेः आधारः, परंपरायाः वाहिका च।’ 
    </blockquote>

    </div>
    """, unsafe_allow_html=True)

st.divider()
if main_option == "🏠 Home":
    show_home()

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
            vowels =["अ (𑀅)", "आ (𑀆)", "इ (𑀇)", "ई (::)", 
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

# ---------------------------
# Function for Quiz
# ---------------------------


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
               }]
    
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

    st.markdown(f"""
<div style="
    background-color: #F5E9D6;
    padding: 20px;
    border-radius: 12px;
    border: 2px solid #8B6F3D;
    font-size: 28px;
    font-weight: 600;
">
    {current_q["question"]}
</div>
""", unsafe_allow_html=True)

    answer = st.radio(
    "",
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
<style>
.justify-text {
    text-align: justify;
    font-size: 18px;
    line-height: 1.8;
}
.section-heading {
    font-size: 28px;
    font-weight: bold;
    margin-top: 30px;
    color: #4b2e1e;
}
.sub-heading {
    font-size: 22px;
    font-weight: 600;
    margin-top: 20px;
    color: #6b4226;
}
</style>
""", unsafe_allow_html=True)



# ---------------------------
# Brahmi Section
# ---------------------------
if main_option == "📜 Brahmi":
   st.markdown("""
<style>
.justify-text {
    text-align: justify;
    font-size: 18px;
    line-height: 1.9;
    margin-bottom: 15px;
}
.section-heading {
    font-size: 32px;
    font-weight: bold;
    margin-top: 10px;
    margin-bottom: 10px;
    color: #4b2e1e;
    text-align: center;
}
.sub-heading {
    font-size: 22px;
    font-weight: 600;
    margin-top: 25px;
    margin-bottom: 10px;
    color: #6b4226;
}
.divider {
    border-top: 2px solid #c2a477;
    margin: 25px 0;
}
</style>
""", unsafe_allow_html=True)

   st.markdown('<div class="section-heading">ब्राह्मी लिपि</div>', unsafe_allow_html=True)
   st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

   st.markdown("""
<div class="justify-text">
ब्राह्मी लिपि भारतीय उपमहाद्वीप की प्राचीनतम और अत्यंत महत्वपूर्ण लिपियों में से एक है। 
इसी से आगे चलकर देवनागरी, बंगला, गुजराती, कन्नड़, तमिल आदि अनेक भारतीय लिपियों का विकास हुआ। 
इस प्रकार इसे भारतीय लिपि परंपरा की जननी कहा जाता है।
</div>
""", unsafe_allow_html=True)

   st.markdown('<div class="sub-heading">ऐतिहासिक पृष्ठभूमि</div>', unsafe_allow_html=True)

   st.markdown("""
<div class="justify-text">
मौर्यकाल, विशेषकर सम्राट अशोक (तीसरी शताब्दी ईसा पूर्व) के शिलालेखों में ब्राह्मी का व्यापक उपयोग मिलता है। 
इन अभिलेखों के माध्यम से न केवल प्रशासनिक घोषणाएँ की गईं, बल्कि नैतिक और धार्मिक संदेश भी जनसामान्य तक पहुँचाए गए।
</div>
""", unsafe_allow_html=True)

   st.markdown('<div class="sub-heading">लिपि की संरचना</div>', unsafe_allow_html=True)

   st.markdown("""
<div class="justify-text">
ब्राह्मी एक ध्वन्यात्मक लिपि है जिसमें स्वर और व्यंजन दोनों का व्यवस्थित रूप मिलता है। 
इसकी संरचना वैज्ञानिक एवं सुव्यवस्थित है, जो आगे चलकर भारतीय वर्णमालाओं की आधारशिला बनी।
</div>
""", unsafe_allow_html=True)

   st.markdown('<div class="sub-heading">सांस्कृतिक महत्व</div>', unsafe_allow_html=True)

   st.markdown("""
<div class="justify-text">
ब्राह्मी लिपि केवल लेखन की पद्धति नहीं, बल्कि भारतीय सांस्कृतिक विरासत का जीवंत प्रतीक है। 
यह भारत की ज्ञान-परंपरा, शिलालेखीय इतिहास और भाषिक विकास की निरंतरता को दर्शाती है।
</div>
""", unsafe_allow_html=True)

   st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

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
    st.markdown("""
<style>
.justify-text {
    text-align: justify;
    font-size: 18px;
    line-height: 1.9;
    margin-bottom: 15px;
}
.section-heading {
    font-size: 32px;
    font-weight: bold;
    margin-top: 10px;
    margin-bottom: 10px;
    color: #4b2e1e;
    text-align: center;
}
.sub-heading {
    font-size: 22px;
    font-weight: 600;
    margin-top: 25px;
    margin-bottom: 10px;
    color: #6b4226;
}
.divider {
    border-top: 2px solid #c2a477;
    margin: 25px 0;
}
</style>
""", unsafe_allow_html=True)

    st.markdown('<div class="section-heading">शारदा लिपि</div>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown("""
<div class="justify-text">
शारदा लिपि उत्तर-पश्चिम भारत, विशेषतः कश्मीर क्षेत्र में प्रचलित एक महत्वपूर्ण प्राचीन लिपि है। 
इसका विकास ब्राह्मी लिपि से हुआ और मध्यकाल में यह संस्कृत तथा क्षेत्रीय भाषाओं के लेखन में व्यापक रूप से प्रयुक्त हुई।
</div>
""", unsafe_allow_html=True)

    st.markdown('<div class="sub-heading">ऐतिहासिक विकास</div>', unsafe_allow_html=True)

    st.markdown("""
<div class="justify-text">
आठवीं से बारहवीं शताब्दी के मध्य शारदा लिपि का व्यापक उपयोग हुआ। 
कश्मीर के अभिलेखों, ताम्रपत्रों और धार्मिक ग्रंथों में इस लिपि के प्रमाण मिलते हैं। 
यह लिपि कश्मीरी सांस्कृतिक परंपरा का एक महत्वपूर्ण अंग रही है।
</div>
""", unsafe_allow_html=True)

    st.markdown('<div class="sub-heading">संरचना और विशेषताएँ</div>', unsafe_allow_html=True)

    st.markdown("""
<div class="justify-text">
शारदा लिपि की आकृतियाँ कोणीय (angular) एवं स्पष्ट रेखाओं वाली हैं। 
इसमें स्वर और व्यंजन दोनों का सुव्यवस्थित रूप मिलता है। 
बाद में इससे टाकरी और गुरुमुखी जैसी लिपियों का विकास हुआ।
</div>
""", unsafe_allow_html=True)

    st.markdown('<div class="sub-heading">सांस्कृतिक महत्व</div>', unsafe_allow_html=True)

    st.markdown("""
<div class="justify-text">
शारदा लिपि केवल लेखन की पद्धति नहीं, बल्कि कश्मीर की दार्शनिक, धार्मिक और साहित्यिक परंपरा की संवाहिका रही है। 
यह भारतीय ज्ञान-परंपरा की निरंतरता और क्षेत्रीय सांस्कृतिक वैभव का प्रतीक है।
</div>
""", unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

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
    

    st.markdown(
        "<h1 style='text-align:center;'>🔗 Important Government Links</h1>",
        unsafe_allow_html=True
    )

    links_data = [
        {"Name": "National Mission for Manuscripts",
         "Description": "The NMM was established in February 2003, by the Ministry of Tourism and Culture, Government of India.",
         "Link": "https://www.namami.gov.in/"},
        
        {"Name": "Gyan Bharatam",
         "Description": "Indian knowledge systems initiative.",
         "Link": "https://gyanbharatam.com/"}  
       
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


    st.markdown(
        "<h1 style='text-align:center;'><br><br>🔗 Important Catalogs Links</h1>",
        unsafe_allow_html=True
    )
    links_data1 = [
        {"Name": "Vande Mataram Library",
         "Description": "The Vande Mataram Library Trust (VMLT), launched in April 2016 by Dr. Sampadananda Mishra. The library is a significant digital resource for studying Sanskrit literature, offering easy access to ancient texts.",
         "Link": "https://vmlt.in/ncc/1?page=1"},

         {"Name": "Indira Gandhi National Centre of the Arts",
         "Description": "It acts as a major repository for thousands of rare manuscripts, offering digitization services, microfilm resources, and training in manuscriptology.",
         "Link": "https://ignca.gov.in/divisionss/kalanidhi/reference-library/print-material/a-descriptive-catalogue-of-microfilmed-manuscripts/"},

         {"Name": "Sandarbha",
         "Description": "It allows you to search a phrase in a digital corpus of Sanskrit text and see it's context.",
         "Link": "https://sandarbha.sangrah.org/"},
    ]
    df1 = pd.DataFrame(links_data1)

    # Make full link clickable
    df1["Link"] = df1["Link"].apply(
        lambda x: f'<a href="{x}" target="_blank">{x}</a>'
    )

    table_html = df1.to_html(escape=False, index=False)

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
    set_background("your_quiz_background_image_url")
    show_game()

#remove arrow ...
st.markdown("""
<style>

/* Hide collapse arrow */
button[kind="header"] {
    display: none !important;
}

/* Hide top sidebar collapse control */
[data-testid="collapsedControl"] {
    display: none !important;
}

</style>
""", unsafe_allow_html=True)


#Transliteration --- 
def conversion_module():

    st.title("🔁 Script Conversion Practice")

    # =====================================
    # 📜 BRAHMI SECTION
    # =====================================

    st.markdown("## 📜 Brahmi → Devanagari")

    brahmi_text = "𑀓𑀼𑀮𑀓𑁆𑀱𑀬𑁂 𑀧𑁆𑀭𑀡𑀰𑁆𑀬𑀦𑁆𑀢𑀺 𑀓𑀼𑀮𑀥𑀭𑁆𑀫𑀸𑀂 𑀲𑀦𑀸𑀢𑀦𑀸𑀂"
    brahmi_correct = "कुलक्षये प्रणश्यन्ति कुलधर्माः सनातनाः"

    st.markdown(f"""
    <div style="font-size:26px; padding:15px;
                background:#F5E9D6;
                border-radius:10px;
                border:2px solid #8B6F3D;">
    {brahmi_text}
    </div>
    """, unsafe_allow_html=True)

    user_brahmi = st.text_area("Type Brahmi conversion here:", key="brahmi_input")

    if st.button("Submit Brahmi", key="brahmi_btn"):
        score = calculate_partial_score(user_brahmi, brahmi_correct)
        st.write(f"Correct Answer: {brahmi_correct}")
        st.success(f"Your Score: {score}%")

    st.markdown("---")

    # =====================================
    # 📖 SHARADA SECTION
    # =====================================

    st.markdown("## 📖 Sharada → Devanagari")

    sharada_text = "𑆃𑆲𑆾 𑆧𑆠 𑆩𑆲𑆠𑇀𑆥𑆳𑆥𑆁 𑆑𑆫𑇀𑆠𑆶𑆁 𑆮𑇀𑆪𑆮𑆱𑆴𑆠𑆳 𑆮𑆪𑆩𑇀 𑇅"
    sharada_correct = "अहो बत महत्पापं कर्तुं व्यवसिता वयम्"

    st.markdown(f"""
    <div style="font-size:26px; padding:15px;
                background:#F5E9D6;
                border-radius:10px;
                border:2px solid #8B6F3D;">
    {sharada_text}
    </div>
    """, unsafe_allow_html=True)

    user_sharada = st.text_area("Type Sharada conversion here:", key="sharada_input")

    if st.button("Submit Sharada", key="sharada_btn"):
        score = calculate_partial_score(user_sharada, sharada_correct)
        st.write(f"Correct Answer: {sharada_correct}")
        st.success(f"Your Score: {score}%")
def calculate_partial_score(user, correct):

    user = user.strip()
    correct = correct.strip()

    total_chars = len(correct)
    match_count = 0

    for u, c in zip(user, correct):
        if u == c:
            match_count += 1

    percentage = int((match_count / total_chars) * 100)

    return percentage       

if main_option == "🔁 Transliteration":
    conversion_module()