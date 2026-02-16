LOGO_HTML = """
<div style="display: flex; justify-content: center; margin-bottom: 20px;">
    <svg width="300" height="80" viewBox="0 0 300 80" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="textGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#d0d0d0"/>
                <stop offset="50%" stop-color="#ffffff"/>
                <stop offset="100%" stop-color="#d0d0d0"/>
            </linearGradient>
        </defs>
        <text x="150" y="50" 
              font-family="SF Pro Display, Helvetica Neue, Arial, sans-serif" 
              font-size="42" 
              font-weight="300" 
              fill="url(#textGradient)" 
              text-anchor="middle" 
              letter-spacing="3">
            MyLexicon
        </text>
    </svg>
</div>
"""

MENU_STYLES = {
    "container": {
        "padding": "6px 8px",
        "background": "transparent",
        "border-radius": "20px",
    },
    "icon": {
        "color": "#d0d0d0", 
        "font-size": "16px",
    }, 
    "nav-link": {
        "font-size": "12px", 
        "text-align": "center",
        "padding": "10px 22px",
        "background": "transparent",
        "backdrop-filter": "blur(10px)",
        "-webkit-backdrop-filter": "blur(10px)",
        "border": "1px solid rgba(255, 255, 255, 0.1)",
        "border-radius": "14px",
        "color": "#ffffff",
        "font-weight": "500",
        "transition": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
        "box-shadow": "0 4px 15px rgba(0, 0, 0, 0.1)",
    },
    "nav-link:hover": {
        "background": "rgba(255, 255, 255, 0.1)",
        "border-color": "rgba(208, 208, 208, 0.3)",
    },
    "nav-link-selected": {
        "background": "linear-gradient(150deg, transparent, transparent)",
        "backdrop-filter": "blur(15px)",
        "-webkit-backdrop-filter": "blur(15px)",
        "border": "1px solid rgba(208, 208, 208, 0.5)",
        "color": "#ffffff",
        "font-weight": "600",
    },
}

GLASS_DIVIDER_HTML = """
    <div style='
        height: 1px;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(208, 208, 208, 0.3), 
            transparent
        );
        margin: 15px 0;
    '></div>
"""
