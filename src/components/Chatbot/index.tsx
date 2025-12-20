import React, { useState, useEffect, useRef } from 'react';
import './Chatbot.css';

const ASSISTANT_AVATAR = "A";
const USER_AVATAR = "U";

interface Message {
    sender: 'user' | 'assistant';
    text: string;
    timestamp: string;
}

const Chatbot: React.FC = () => {
    const [isOpen, setIsOpen] = useState<boolean>(false);
    const [messages, setMessages] = useState<Message[]>([]);
    const [inputValue, setInputValue] = useState<string>('');
    const [isLoading, setIsLoading] = useState<boolean>(false);
    const [selectedText, setSelectedText] = useState<string>('');
    const [askButtonPosition, setAskButtonPosition] = useState({ top: 0, left: 0, display: 'none' });
    const messageListRef = useRef<HTMLDivElement | null>(null);

    // Scroll to bottom of message list
    useEffect(() => {
        if (messageListRef.current) {
            messageListRef.current.scrollTop = messageListRef.current.scrollHeight;
        }
    }, [messages]);
    
    const handleSendMessage = async () => {
        if (inputValue.trim() === '') return;

        const userMessage: Message = {
            sender: 'user',
            text: inputValue,
            timestamp: new Date().toLocaleTimeString(),
        };
        setMessages(prev => [...prev, userMessage]);
        setInputValue('');
        setIsLoading(true);

        try {
            const response = await fetch('/api/rag/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query: inputValue }),
            });

            if (!response.ok) {
                throw new Error('Failed to get a response from the chatbot.');
            }

            const data = await response.json();
            
            const assistantMessage: Message = {
                sender: 'assistant',
                text: data.answer, // Assuming the backend returns an 'answer' field
                timestamp: new Date().toLocaleTimeString(),
            };
            setMessages(prev => [...prev, assistantMessage]);

        } catch (error) {
            console.error('Chatbot API error:', error);
            const errorMessage: Message = {
                sender: 'assistant',
                text: "Sorry, I'm having trouble connecting. Please try again later.",
                timestamp: new Date().toLocaleTimeString(),
            };
            setMessages(prev => [...prev, errorMessage]);
        } finally {
            setIsLoading(false);
        }
    };
    
    // Handle text selection for "Ask about this"
    const handleMouseUp = () => {
        const selection = window.getSelection();
        const text = selection?.toString().trim();
        if (text && text.length > 10) {
            const range = selection.getRangeAt(0);
            const rect = range.getBoundingClientRect();
            setSelectedText(text);
            setAskButtonPosition({
                top: rect.bottom + window.scrollY + 5,
                left: rect.left + window.scrollX,
                display: 'block',
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
        const query = `Based on the following text, can you explain it further?\n\n---\n${selectedText}\n---`;
        setInputValue(query);
        setIsOpen(true);
        setAskButtonPosition({ top: 0, left: 0, display: 'none' });
    };

    return (
        <>
            <div className="chatbot-fab" onClick={() => setIsOpen(!isOpen)}>
                {isOpen ? 'X' : '💬'}
            </div>
            
            {askButtonPosition.display === 'block' && (
                <button
                    className="ask-button"
                    style={{ top: `${askButtonPosition.top}px`, left: `${askButtonPosition.left}px` }}
                    onClick={handleAskAboutSelection}
                >
                    Ask about this
                </button>
            )}

            {isOpen && (
                <div className="chatbot-window">
                    <div className="chatbot-header">
                        <h3>Book Assistant</h3>
                        <button className="close-button" onClick={() => setIsOpen(false)}>✕</button>
                    </div>
                    <div className="message-list" ref={messageListRef}>
                        {messages.map((msg, index) => (
                            <div key={index} className={`message ${msg.sender}`}>
                                <div className="message-avatar">
                                    {msg.sender === 'user' ? USER_AVATAR : ASSISTANT_AVATAR}
                                </div>
                                <div className="message-content">
                                    {msg.text}
                                    <div className="message-timestamp">{msg.timestamp}</div>
                                </div>
                            </div>
                        ))}
                        {isLoading && (
                            <div className="message assistant">
                                <div className="message-avatar">{ASSISTANT_AVATAR}</div>
                                <div className="message-content">
                                    <div className="loading-indicator">
                                        <span></span><span></span><span></span>
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>
                    <div className="chatbot-composer">
                        <input
                            type="text"
                            value={inputValue}
                            onChange={(e) => setInputValue(e.target.value)}
                            onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
                            placeholder="Ask a question..."
                        />
                        <button onClick={handleSendMessage}>➤</button>
                    </div>
                </div>
            )}
        </>
    );
};

export default Chatbot;