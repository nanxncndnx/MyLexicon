CHAT_STYLES = """
<style>
.chat-container {
    display: flex;
    flex-direction: column;
    gap: 15px;
    margin-bottom: 20px;
    padding: 10px;
}

.user-message {
    display: flex;
    justify-content: flex-end;
    margin-left: 20%;
}

.assistant-message {
    display: flex;
    justify-content: flex-start;
    margin-right: 20%;
}

.message-bubble {
    padding: 12px 18px;
    border-radius: 18px;
    max-width: 100%;
    word-wrap: break-word;
}

.user-bubble {
    background: linear-gradient(135deg, #a8b8d8 0%, #c0c8d8 50%, #d8dce8 100%);
    color: #1a1a1a;
    border-bottom-right-radius: 4px;
    box-shadow: 0 4px 15px rgba(168, 184, 216, 0.3);
}

.assistant-bubble {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(208, 208, 208, 0.2);
    color: #d0d0d0;
    border-bottom-left-radius: 4px;
}
</style>
"""
