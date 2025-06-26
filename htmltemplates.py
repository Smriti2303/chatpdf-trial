css = '''
<style>
.chat-message {
    padding: 1.2rem;
    border-radius: 1.2rem;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: flex-start;
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(8px);
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}
.chat-message.user {
    background: rgba(47, 53, 66, 0.9);
}
.chat-message.bot {
    background: rgba(87, 96, 111, 0.9);
}
.chat-message .avatar {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    overflow: hidden;
    flex-shrink: 0;
    border: 2px solid white;
}
.chat-message .avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.chat-message .message {
    flex: 1;
    padding: 0 1.2rem;
    color: #fff;
    font-size: 1rem;
    white-space: pre-wrap;
}
button:hover {
    background-color: #3742fa !important;
    color: white !important;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn.openart.ai/uploads/image_wRzOL9xa_1718069239214_raw.jpg" alt="Bot Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://us-tuna-sounds-images.voicemod.net/a5d72ecb-cd20-4e09-8606-1e411df3b2e1-1713904553784.jpeg" alt="User Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
