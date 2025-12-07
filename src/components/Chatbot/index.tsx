import React, { useState, useEffect } from 'react';
import "@chatscope/chat-ui-kit-styles/dist/default/styles.min.css";
import {
    MainContainer,
    ChatContainer,
    MessageList,
    Message,
    MessageInput,
    ConversationHeader,
    Avatar
} from "@chatscope/chat-ui-kit-react";

const Chatbot = () => {
    const [messages, setMessages] = useState([]);
    const [selectedText, setSelectedText] = useState('');
    const [askButtonPosition, setAskButtonPosition] = useState({ top: 0, left: 0, display: 'none' });

    const handleSend = async (message) => {
        const newMessage = {
            message,
            direction: 'outgoing',
            sender: "user"
        };
        setMessages([...messages, newMessage]);
        
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query: message, context_text: selectedText })
        });
        const data = await response.json();

        const botMessage = {
            message: `${data.answer}\n\nSources: ${data.sources.join(', ')}`,
            direction: 'incoming',
            sender: "bot"
        };
        setMessages([...messages, newMessage, botMessage]);
        setSelectedText('');
    };

    const handleMouseUp = () => {
        const selection = window.getSelection();
        if (selection.toString().length > 0) {
            const range = selection.getRangeAt(0);
            const rect = range.getBoundingClientRect();
            setSelectedText(selection.toString());
            setAskButtonPosition({
                top: rect.bottom + window.scrollY,
                left: rect.left + window.scrollX,
                display: 'block'
            });
        } else {
            setAskButtonPosition({ top: 0, left: 0, display: 'none' });
        }
    };

    useEffect(() => {
        document.addEventListener('mouseup', handleMouseUp);
        return () => {
            document.removeEventListener('mouseup', handleMouseUp);
        };
    }, []);

    const handleAskAboutSelection = () => {
        handleSend(selectedText);
        setAskButtonPosition({ top: 0, left: 0, display: 'none' });
    }

    return (
        <div style={{ position: 'fixed', bottom: '20px', right: '20px', height: '500px', width: '350px', zIndex: 1000 }}>
            <MainContainer>
                <ChatContainer>
                    <ConversationHeader>
                        <Avatar src="/img/logo.svg" name="Bot" />
                        <ConversationHeader.Content userName="Book Assistant" info="Ask me anything about the book" />
                    </ConversationHeader>
                    <MessageList>
                        {messages.map((msg, i) => (
                            <Message key={i} model={msg} />
                        ))}
                    </MessageList>
                    <MessageInput placeholder="Type message here" onSend={handleSend} />
                </ChatContainer>
            </MainContainer>
            <button
                style={{
                    position: 'absolute',
                    top: askButtonPosition.top,
                    left: askButtonPosition.left,
                    display: askButtonPosition.display,
                    zIndex: 1001
                }}
                onClick={handleAskAboutSelection}
            >
                Ask about this
            </button>
        </div>
    );
};

export default Chatbot;