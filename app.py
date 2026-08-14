%%writefile app.py

import streamlit as st
import base64
from datetime import datetime

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="PashuRakshak AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# SESSION STATE
# ============================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "language" not in st.session_state:
    st.session_state.language = "English"

if "animal" not in st.session_state:
    st.session_state.animal = None

if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None


# ============================================================
# TRANSLATIONS
# ============================================================

TEXT = {

    "English": {
        "dashboard": "Dashboard",
        "screening": "New Screening",
        "history": "Screening History",
        "analytics": "Analytics",
        "veterinary": "Veterinary Help",
        "notifications": "Notifications",
        "settings": "Settings",
        "profile": "Profile",
        "logout": "Logout",

        "welcome": "Welcome to PashuRakshak AI",
        "subtitle": "AI-powered livestock health screening",

        "start": "Start New Screening",
        "recent": "Recent Screenings",
        "animals": "Animals Checked",
        "total": "Total Screenings",
        "accuracy": "AI Model",

        "upload": "Upload Animal Image",
        "select_animal": "Select Animal",
        "symptoms": "Symptom Verification",
        "additional": "Additional Symptoms",
        "analyze": "Analyze Animal",

        "cow": "Cow",
        "buffalo": "Buffalo",
        "goat": "Goat",
        "sheep": "Sheep",

        "login": "Login",
        "email": "Email Address",
        "password": "Password",
        "remember": "Remember me",
        "forgot": "Forgot password?",
        "signin": "Sign In",
        "signup": "Create Account",

        "language": "Language",
        "offline": "Offline AI Ready",

        "help": "Need help?",
        "save": "Save Changes"
    },

    "हिन्दी": {
        "dashboard": "डैशबोर्ड",
        "screening": "नई जाँच",
        "history": "जाँच इतिहास",
        "analytics": "विश्लेषण",
        "veterinary": "पशु चिकित्सा सहायता",
        "notifications": "सूचनाएँ",
        "settings": "सेटिंग्स",
        "profile": "प्रोफ़ाइल",
        "logout": "लॉग आउट",

        "welcome": "PashuRakshak AI में आपका स्वागत है",
        "subtitle": "AI आधारित पशु स्वास्थ्य जाँच",

        "start": "नई जाँच शुरू करें",
        "recent": "हाल की जाँच",
        "animals": "जाँचे गए पशु",
        "total": "कुल जाँच",
        "accuracy": "AI मॉडल",

        "upload": "पशु की तस्वीर अपलोड करें",
        "select_animal": "पशु चुनें",
        "symptoms": "लक्षणों की जाँच",
        "additional": "अन्य लक्षण",
        "analyze": "पशु का विश्लेषण करें",

        "cow": "गाय",
        "buffalo": "भैंस",
        "goat": "बकरी",
        "sheep": "भेड़",

        "login": "लॉगिन",
        "email": "ईमेल पता",
        "password": "पासवर्ड",
        "remember": "मुझे याद रखें",
        "forgot": "पासवर्ड भूल गए?",
        "signin": "साइन इन",
        "signup": "खाता बनाएँ",

        "language": "भाषा",
        "offline": "ऑफलाइन AI तैयार",

        "help": "मदद चाहिए?",
        "save": "बदलाव सेव करें"
    },

    "मराठी": {
        "dashboard": "डॅशबोर्ड",
        "screening": "नवीन तपासणी",
        "history": "तपासणी इतिहास",
        "analytics": "विश्लेषण",
        "veterinary": "पशुवैद्यकीय मदत",
        "notifications": "सूचना",
        "settings": "सेटिंग्ज",
        "profile": "प्रोफाइल",
        "logout": "लॉग आउट",

        "welcome": "PashuRakshak AI मध्ये आपले स्वागत आहे",
        "subtitle": "AI आधारित पशुधन आरोग्य तपासणी",

        "start": "नवीन तपासणी सुरू करा",
        "recent": "अलीकडील तपासण्या",
        "animals": "तपासलेले प्राणी",
        "total": "एकूण तपासण्या",
        "accuracy": "AI मॉडेल",

        "upload": "प्राण्याचा फोटो अपलोड करा",
        "select_animal": "प्राणी निवडा",
        "symptoms": "लक्षणांची तपासणी",
        "additional": "इतर लक्षणे",
        "analyze": "प्राण्याचे विश्लेषण करा",

        "cow": "गाय",
        "buffalo": "म्हैस",
        "goat": "शेळी",
        "sheep": "मेंढी",

        "login": "लॉगिन",
        "email": "ईमेल पत्ता",
        "password": "पासवर्ड",
        "remember": "मला लक्षात ठेवा",
        "forgot": "पासवर्ड विसरलात?",
        "signin": "साइन इन",
        "signup": "खाते तयार करा",

        "language": "भाषा",
        "offline": "ऑफलाइन AI तयार",

        "help": "मदत हवी आहे?",
        "save": "बदल सेव्ह करा"
    }
}


def t(key):
    return TEXT[st.session_state.language].get(key, key)


# ============================================================
# SVG ICON SYSTEM
# ============================================================

ICONS = {

    "home": """
    <svg viewBox="0 0 24 24">
    <path d="M3 10.5 12 3l9 7.5v9a1.5 1.5 0 0 1-1.5 1.5h-5v-6h-5v6h-5A1.5 1.5 0 0 1 3 19.5z"/>
    </svg>
    """,

    "scan": """
    <svg viewBox="0 0 24 24">
    <path d="M4 7V5a1 1 0 0 1 1-1h2M17 4h2a1 1 0 0 1 1 1v2M20 17v2a1 1 0 0 1-1 1h-2M7 20H5a1 1 0 0 1-1-1v-2"/>
    <circle cx="12" cy="12" r="3"/>
    </svg>
    """,

    "history": """
    <svg viewBox="0 0 24 24">
    <path d="M3 12a9 9 0 1 0 3-6.7"/>
    <path d="M3 4v6h6"/>
    <path d="M12 7v5l3 2"/>
    </svg>
    """,

    "chart": """
    <svg viewBox="0 0 24 24">
    <path d="M4 19V5M4 19h16"/>
    <rect x="7" y="11" width="2.5" height="5"/>
    <rect x="11" y="8" width="2.5" height="8"/>
    <rect x="15" y="5" width="2.5" height="11"/>
    </svg>
    """,

    "vet": """
    <svg viewBox="0 0 24 24">
    <path d="M12 21s8-4 8-10V5l-8-3-8 3v6c0 6 8 10 8 10z"/>
    <path d="M9 12h6M12 9v6"/>
    </svg>
    """,

    "bell": """
    <svg viewBox="0 0 24 24">
    <path d="M18 8a6 6 0 0 0-12 0c0 7-3 7-3 9h18c0-2-3-2-3-9"/>
    <path d="M10 21h4"/>
    </svg>
    """,

    "settings": """
    <svg viewBox="0 0 24 24">
    <circle cx="12" cy="12" r="3"/>
    <path d="M19.4 15a1.7 1.7 0 0 0 .3 1.9l.1.1-2 2-.1-.1a1.7 1.7 0 0 0-1.9-.3 1.7 1.7 0 0 0-1 1.5V20h-3v-.1a1.7 1.7 0 0 0-1-1.5 1.7 1.7 0 0 0-1.9.3l-.1.1-2-2 .1-.1A1.7 1.7 0 0 0 7.2 15a1.7 1.7 0 0 0-1.5-1H5v-3h.7a1.7 1.7 0 0 0 1.5-1 1.7 1.7 0 0 0-.3-1.9l-.1-.1 2-2 .1.1a1.7 1.7 0 0 0 1.9.3 1.7 1.7 0 0 0 1-1.5V5h3v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.9-.3l.1-.1 2 2-.1.1a1.7 1.7 0 0 0-.3 1.9 1.7 1.7 0 0 0 1.5 1h.1v3h-.1a1.7 1.7 0 0 0-1.5 1z"/>
    </svg>
    """,

    "user": """
    <svg viewBox="0 0 24 24">
    <circle cx="12" cy="8" r="4"/>
    <path d="M4 21c.8-4 3.5-6 8-6s7.2 2 8 6"/>
    </svg>
    """,

    "upload": """
    <svg viewBox="0 0 24 24">
    <path d="M12 16V4"/>
    <path d="m7 9 5-5 5 5"/>
    <path d="M5 20h14"/>
    </svg>
    """,

    "shield": """
    <svg viewBox="0 0 24 24">
    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
    <path d="m9 12 2 2 4-5"/>
    </svg>
    """,

    "arrow": """
    <svg viewBox="0 0 24 24">
    <path d="M5 12h14"/>
    <path d="m13 6 6 6-6 6"/>
    </svg>
    """
}


def icon(name, size=22):
    return f"""
    <span class="svg-icon" style="width:{size}px;height:{size}px;">
        {ICONS[name]}
    </span>
    """


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f5f8f6;
}

#MainMenu,
footer,
header {
    visibility: hidden;
}

.svg-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    vertical-align: middle;
}

.svg-icon svg {
    width: 100%;
    height: 100%;
    fill: none;
    stroke: currentColor;
    stroke-width: 1.8;
    stroke-linecap: round;
    stroke-linejoin: round;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e4ebe6;
}

.brand {
    text-align: center;
    padding: 12px 5px 20px;
}

.logo {
    width: 64px;
    height: 64px;
    border-radius: 19px;
    background: linear-gradient(135deg,#15803d,#0f766e);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: auto;
    box-shadow: 0 10px 25px rgba(21,128,61,.20);
}

.logo svg {
    width: 35px;
    height: 35px;
    fill: none;
    stroke: white;
    stroke-width: 1.6;
    stroke-linecap: round;
    stroke-linejoin: round;
}

.brand-name {
    margin-top: 10px;
    font-size: 19px;
    font-weight: 800;
    color: #17251c;
}

.brand-tag {
    font-size: 9px;
    color: #718078;
    letter-spacing: 1.5px;
    margin-top: 3px;
}

/* BUTTONS */

.stButton > button {
    border-radius: 11px;
    min-height: 42px;
    font-weight: 600;
    border: 1px solid #e2e9e4;
    background: white;
    color: #27352d;
    transition: .2s;
}

.stButton > button:hover {
    border-color: #15803d;
    color: #15803d;
}

/* PRIMARY BUTTON */

.primary-btn .stButton > button {
    background: #15803d;
    color: white;
    border: none;
}

/* PAGE */

.page-title {
    font-size: 31px;
    font-weight: 800;
    color: #17251c;
    margin-bottom: 3px;
}

.page-subtitle {
    color: #718078;
    font-size: 14px;
}

/* HERO */

.hero {
    margin-top: 25px;
    padding: 34px;
    border-radius: 24px;
    background: linear-gradient(120deg,#166534,#15803d,#0f766e);
    color: white;
    min-height: 230px;
    position: relative;
    overflow: hidden;
}

.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,.14);
    padding: 7px 12px;
    border-radius: 20px;
    font-size: 11px;
    letter-spacing: .4px;
}

.hero-title {
    font-size: 31px;
    font-weight: 800;
    margin-top: 17px;
}

.hero-text {
    max-width: 650px;
    margin-top: 9px;
    line-height: 1.6;
    color: rgba(255,255,255,.88);
}

/* CARDS */

.card {
    background: white;
    border: 1px solid #e4ebe6;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 18px;
}

.card-title {
    font-weight: 750;
    font-size: 16px;
    color: #17251c;
    margin-bottom: 12px;
}

/* STAT */

.stat-card {
    background: white;
    border: 1px solid #e4ebe6;
    border-radius: 17px;
    padding: 20px;
}

.stat-value {
    font-size: 27px;
    font-weight: 800;
    color: #17251c;
    margin-top: 4px;
}

.stat-label {
    color: #718078;
    font-size: 12px;
}

/* STATUS */

.status {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: #dcfce7;
    color: #15803d;
    padding: 7px 11px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 700;
}

/* LOGIN */

.login-wrapper {
    max-width: 440px;
    margin: 50px auto;
}

.login-logo {
    width: 76px;
    height: 76px;
    margin: auto;
    border-radius: 23px;
    background: linear-gradient(135deg,#15803d,#0f766e);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
}

.login-title {
    text-align: center;
    font-size: 29px;
    font-weight: 800;
    color: #17251c;
    margin-top: 14px;
}

.login-subtitle {
    text-align: center;
    color: #718078;
    font-size: 13px;
    margin-bottom: 25px;
}

/* ANIMAL CARD */

.animal-card {
    background: white;
    border: 1px solid #e4ebe6;
    border-radius: 17px;
    padding: 19px;
    text-align: center;
}

.animal-icon {
    font-size: 36px;
}

.animal-name {
    font-weight: 700;
    margin-top: 6px;
}

/* RESULT */

.result {
    background: white;
    border: 1px solid #e4ebe6;
    border-radius: 20px;
    padding: 28px;
}

.result-good {
    color: #15803d;
    font-size: 27px;
    font-weight: 800;
}

/* FOOTER */

.app-footer {
    text-align: center;
    color: #8a968f;
    font-size: 11px;
    padding: 25px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOGIN PAGE
# ============================================================

if not st.session_state.logged_in:

    st.markdown("""
    <div class="login-wrapper">

        <div class="login-logo">
            <svg width="42" height="42" viewBox="0 0 24 24"
                 fill="none" stroke="white" stroke-width="1.6"
                 stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                <path d="m9 12 2 2 4-5"/>
            </svg>
        </div>

        <div class="login-title">
            PashuRakshak AI
        </div>

        <div class="login-subtitle">
            AI-powered livestock health screening
        </div>

    </div>
    """, unsafe_allow_html=True)

    # Language

    lang = st.selectbox(
        "🌐 Language",
        ["English", "हिन्दी", "मराठी"],
        index=["English", "हिन्दी", "मराठी"].index(
            st.session_state.language
        )
    )

    st.session_state.language = lang

    st.write("")

    email = st.text_input(
        t("email"),
        placeholder="example@email.com"
    )

    password = st.text_input(
        t("password"),
        type="password"
    )

    remember = st.checkbox(t("remember"))

    c1, c2 = st.columns(2)

    with c1:
        if st.button(
            t("signin"),
            type="primary",
            use_container_width=True
        ):
            if email and password:
                st.session_state.logged_in = True
                st.session_state.page = "Dashboard"
                st.rerun()
            else:
                st.warning("Please enter email and password.")

    with c2:
        if st.button(
            t("signup"),
            use_container_width=True
        ):
            st.info(
                "Account creation will be connected to the backend later."
            )

    st.write("")

    st.markdown(
        f"<div style='text-align:center;color:#718078;font-size:12px;'>"
        f"{t('forgot')}"
        f"</div>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="app-footer">
        PashuRakshak AI • Demo Prototype<br>
        AI-assisted screening is not a veterinary diagnosis.
    </div>
    """, unsafe_allow_html=True)

    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <div class="brand">

        <div class="logo">
            <svg viewBox="0 0 24 24">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                <path d="m9 12 2 2 4-5"/>
            </svg>
        </div>

        <div class="brand-name">
            PashuRakshak AI
        </div>

        <div class="brand-tag">
            AI LIVESTOCK HEALTH
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Navigation

    nav_items = [
        ("Dashboard", "home", t("dashboard")),
        ("Screening", "scan", t("screening")),
        ("History", "history", t("history")),
        ("Analytics", "chart", t("analytics")),
        ("Veterinary", "vet", t("veterinary")),
        ("Notifications", "bell", t("notifications")),
        ("Settings", "settings", t("settings"))
    ]

    for page, icon_name, label in nav_items:

        if st.button(
            label,
            key=f"nav_{page}",
            use_container_width=True,
            icon=f":material/{icon_name}:"
        ):
            st.session_state.page = page
            st.rerun()

    st.divider()

    st.markdown("""
    <div class="status">
        ● Offline AI Ready
    </div>

    <p style="
        font-size:11px;
        color:#718078;
        line-height:1.5;
        margin-top:10px;">
        Basic screening can continue even when
        internet connectivity is unavailable.
    </p>
    """, unsafe_allow_html=True)

    st.divider()

    if st.button(
        t("profile"),
        use_container_width=True,
        icon=":material/person:"
    ):
        st.session_state.page = "Profile"
        st.rerun()

    if st.button(
        t("logout"),
        use_container_width=True,
        icon=":material/logout:"
    ):
        st.session_state.logged_in = False
        st.rerun()


# ============================================================
# TOP LANGUAGE SELECTOR
# ============================================================

top1, top2 = st.columns([5, 1])

with top2:

    language = st.selectbox(
        "Language",
        ["English", "हिन्दी", "मराठी"],
        index=["English", "हिन्दी", "मराठी"].index(
            st.session_state.language
        ),
        label_visibility="collapsed"
    )

    if language != st.session_state.language:
        st.session_state.language = language
        st.rerun()


# ============================================================
# DASHBOARD
# ============================================================

if st.session_state.page == "Dashboard":

    st.markdown(
        f'<div class="page-title">{t("welcome")} 👋</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="page-subtitle">{t("subtitle")}</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="hero">

        <div class="hero-badge">
            ✦ AI-POWERED LIVESTOCK HEALTH
        </div>

        <div class="hero-title">
            Early detection can save livestock.
        </div>

        <div class="hero-text">
            Upload an animal image, answer simple symptom
            questions and receive AI-assisted preliminary
            screening insights.
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button(
        t("start"),
        type="primary",
        icon=":material/search:",
        use_container_width=False
    ):
        st.session_state.page = "Screening"
        st.rerun()

    st.write("")

    # Stats

    c1, c2, c3, c4 = st.columns(4)

    stats = [
        ("24", t("total"), "search"),
        ("18", t("animals"), "pets"),
        ("94%", t("accuracy"), "psychology"),
        ("98%", "Offline Ready", "wifi_off")
    ]

    for col, (value, label, icon_name) in zip(
        [c1, c2, c3, c4],
        stats
    ):

        with col:

            st.markdown(
                f"""
                <div class="stat-card">
                    <div style="color:#15803d;">
                        {icon(icon_name if icon_name in ICONS else "shield", 24)}
                    </div>
                    <div class="stat-value">{value}</div>
                    <div class="stat-label">{label}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.write("")

    left, right = st.columns([1.5, 1])

    with left:

        st.markdown(
            f'<div class="card-title">{t("recent")}</div>',
            unsafe_allow_html=True
        )

        recent = [
            ("🐄", "Cow", "Today • 09:20 AM", "Healthy"),
            ("🐐", "Goat", "Today • 08:10 AM", "Attention"),
            ("🐃", "Buffalo", "Yesterday", "Healthy"),
            ("🐑", "Sheep", "Yesterday", "Healthy")
        ]

        for animal_icon, animal, date, result in recent:

            col1, col2 = st.columns([4, 1])

            with col1:
                st.markdown(
                    f"""
                    <div class="card">
                        <span style="font-size:25px;">
                            {animal_icon}
                        </span>
                        <b style="margin-left:10px;">
                            {animal}
                        </b>
                        <span style="
                            margin-left:12px;
                            color:#718078;
                            font-size:11px;">
                            {date}
                        </span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:
                if result == "Healthy":
                    st.success(result)
                else:
                    st.warning(result)

    with right:

        st.markdown("""
        <div class="card">

            <div class="card-title">
                How PashuRakshak Works
            </div>

            <p>01 &nbsp; Select animal</p>
            <p>02 &nbsp; Upload image</p>
            <p>03 &nbsp; Verify symptoms</p>
            <p>04 &nbsp; AI screening</p>
            <p>05 &nbsp; Get result</p>

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# SCREENING
# ============================================================

elif st.session_state.page == "Screening":

    st.markdown(
        f'<div class="page-title">{t("screening")} 🔍</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Begin a new livestock health screening.'
        '</div>',
        unsafe_allow_html=True
    )

    st.progress(0.25)

    st.caption("Step 1 of 4 • Animal & Image")

    st.write("")

    st.markdown(
        f'<div class="card-title">{t("select_animal")}</div>',
        unsafe_allow_html=True
    )

    animals = [
        ("🐄", "Cow"),
        ("🐃", "Buffalo"),
        ("🐐", "Goat"),
        ("🐑", "Sheep")
    ]

    cols = st.columns(4)

    for i, (animal_icon, animal) in enumerate(animals):

        with cols[i]:

            if st.button(
                f"{animal_icon}  {animal}",
                key=f"animal_{animal}",
                use_container_width=True
            ):
                st.session_state.animal = animal

    if st.session_state.animal:
        st.success(
            f"Selected: {st.session_state.animal}"
        )

    st.write("")

    st.markdown(
        f'<div class="card-title">{t("upload")}</div>',
        unsafe_allow_html=True
    )

    uploaded = st.file_uploader(
        "Choose a clear animal image",
        type=["jpg", "jpeg", "png", "webp"]
    )

    if uploaded:

        st.session_state.uploaded_image = uploaded

        st.image(
            uploaded,
            caption="Uploaded Animal",
            width=400
        )

    st.write("")

    if st.button(
        "Continue to Symptoms",
        type="primary",
        icon=":material/arrow_forward:",
        use_container_width=True
    ):

        if not st.session_state.animal:
            st.warning("Please select an animal.")

        elif not uploaded:
            st.warning("Please upload an image.")

        else:
            st.session_state.page = "Symptoms"
            st.rerun()


# ============================================================
# SYMPTOMS
# ============================================================

elif st.session_state.page == "Symptoms":

    st.markdown(
        f'<div class="page-title">{t("symptoms")} 🩺</div>',
        unsafe_allow_html=True
    )

    st.progress(0.50)

    st.caption("Step 2 of 4 • Symptoms")

    questions = [
        "Does the animal have a fever?",
        "Is the animal eating less than usual?",
        "Does the animal appear unusually weak?",
        "Is there abnormal discharge?",
        "Does the animal have difficulty walking?",
        "Is there swelling?",
        "Is the animal coughing or breathing unusually?",
        "Has milk production decreased?"
    ]

    for i, question in enumerate(questions):

        st.markdown(
            f"""
            <div class="card">
                <b>{i+1}. {question}</b>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.radio(
            "Answer",
            ["Yes", "No"],
            horizontal=True,
            key=f"symptom_{i}",
            label_visibility="collapsed"
        )

    st.markdown(
        f'<div class="card-title">{t("additional")}</div>',
        unsafe_allow_html=True
    )

    st.text_area(
        "Describe other symptoms you have noticed",
        placeholder="Example: animal has been less active since yesterday..."
    )

    if st.button(
        t("analyze"),
        type="primary",
        icon=":material/psychology:",
        use_container_width=True
    ):

        st.session_state.page = "Analysis"
        st.rerun()


# ============================================================
# ANALYSIS
# ============================================================

elif st.session_state.page == "Analysis":

    st.markdown(
        '<div class="page-title">AI Analysis 🧠</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Analyzing the available screening information...'
        '</div>',
        unsafe_allow_html=True
    )

    import time

    with st.spinner("Running AI screening..."):

        progress = st.progress(0)

        for i in range(0, 101, 10):
            time.sleep(0.08)
            progress.progress(i)

    st.success("Analysis completed.")

    if st.button(
        "View Result",
        type="primary",
        icon=":material/arrow_forward:"
    ):

        st.session_state.page = "Result"
        st.rerun()


# ============================================================
# RESULT
# ============================================================

elif st.session_state.page == "Result":

    st.markdown(
        '<div class="page-title">Screening Result</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="result">

        <div style="
            color:#15803d;
            font-size:13px;
            font-weight:700;">
            PRELIMINARY SCREENING
        </div>

        <div class="result-good">
            Low Risk / Healthy
        </div>

        <p>
            AI Confidence: <b>94%</b>
        </p>

        <hr>

        <b>Screening Summary</b>

        <p style="color:#718078;">
            No major high-risk indicators were detected
            in this demo screening.
        </p>

        <div style="
            background:#fff7ed;
            padding:14px;
            border-radius:10px;
            margin-top:15px;">
            ⚠️ This is an AI-assisted screening result,
            not a veterinary diagnosis.
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button(
        "Start New Screening",
        type="primary",
        icon=":material/search:"
    ):

        st.session_state.page = "Screening"
        st.rerun()


# ============================================================
# HISTORY
# ============================================================

elif st.session_state.page == "History":

    st.markdown(
        f'<div class="page-title">{t("history")}</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        [
            ["Cow", "Healthy", "94%", "14 Aug 2026"],
            ["Goat", "Attention", "87%", "14 Aug 2026"],
            ["Buffalo", "Healthy", "92%", "13 Aug 2026"],
            ["Sheep", "Healthy", "91%", "13 Aug 2026"]
        ],
        column_config={
            0: "Animal",
            1: "Result",
            2: "Confidence",
            3: "Date"
        },
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# ANALYTICS
# ============================================================

elif st.session_state.page == "Analytics":

    st.markdown(
        f'<div class="page-title">{t("analytics")}</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Screenings", "24", "+6")
    c2.metric("Healthy", "16", "+4")
    c3.metric("Attention Required", "8", "+2")

    st.info(
        "Detailed analytics will be connected to the screening database later."
    )


# ============================================================
# VETERINARY HELP
# ============================================================

elif st.session_state.page == "Veterinary":

    st.markdown(
        f'<div class="page-title">{t("veterinary")} 🩺</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

        <div class="card-title">
            Veterinary Assistance
        </div>

        <p>
            Find nearby veterinary support when a screening
            indicates that professional attention may be needed.
        </p>

        <p style="color:#718078;">
            Location-based veterinary services will be
            connected in the next development stage.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.button(
        "Find Nearby Veterinary Support",
        type="primary",
        icon=":material/location_on:"
    )


# ============================================================
# NOTIFICATIONS
# ============================================================

elif st.session_state.page == "Notifications":

    st.markdown(
        f'<div class="page-title">{t("notifications")}</div>',
        unsafe_allow_html=True
    )

    st.info("No new notifications.")

    st.warning(
        "Remember: AI screening should not replace professional veterinary care."
    )


# ============================================================
# PROFILE
# ============================================================

elif st.session_state.page == "Profile":

    st.markdown(
        f'<div class="page-title">{t("profile")}</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

        <div style="
            width:70px;
            height:70px;
            border-radius:50%;
            background:#dcfce7;
            display:flex;
            align-items:center;
            justify-content:center;
            margin-bottom:15px;">

            <svg width="35" height="35"
                 viewBox="0 0 24 24"
                 fill="none"
                 stroke="#15803d"
                 stroke-width="1.8">
                <circle cx="12" cy="8" r="4"/>
                <path d="M4 21c.8-4 3.5-6 8-6s7.2 2 8 6"/>
            </svg>

        </div>

        <b>Demo User</b>

        <p style="color:#718078;">
            Farmer / Livestock Owner
        </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# SETTINGS
# ============================================================

elif st.session_state.page == "Settings":

    st.markdown(
        f'<div class="page-title">{t("settings")} ⚙️</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="card-title">{t("language")}</div>',
        unsafe_allow_html=True
    )

    new_language = st.selectbox(
        "Choose your preferred language",
        ["English", "हिन्दी", "मराठी"],
        index=["English", "हिन्दी", "मराठी"].index(
            st.session_state.language
        )
    )

    if st.button(t("save"), type="primary"):

        st.session_state.language = new_language

        st.success("Settings saved successfully.")


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="app-footer">
    PashuRakshak AI • AI-assisted livestock health screening
    <br>
    Demo UI • TensorFlow model and backend will be integrated later
</div>
""", unsafe_allow_html=True)