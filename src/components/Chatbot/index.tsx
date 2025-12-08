import React, { useState, useEffect, useRef } from 'react';
import {
    ChatKit,
    ChatKitAvatar,
    ChatKitComposer,
    ChatKitMessage,
    ChatKitMessageList,
    ChatKitWindow,
} from '@openai/chatkit-react';

const ASSISTANT_ID = "book-rag-assistant"; // Must match the assistant ID in the backend

const Chatbot: React.FC = () => {
    const [clientSecret, setClientSecret] = useState<string | null>(null);
    const [selectedText, setSelectedText] = useState<string>('');
    const [askButtonPosition, setAskButtonPosition] = useState({ top: 0, left: 0, display: 'none' });
    const [isOpen, setIsOpen] = useState<boolean>(false);
    
    const composerRef = useRef<{ setText: (text: string) => void } | null>(null);

    // T074: Fetch ChatKit session client secret
    useEffect(() => {
        const fetchSession = async () => {
            try {
                const response = await fetch('/api/chatkit/session', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ user_id: 'anonymous-user' }), // Example user ID
                });
                if (!response.ok) {
                    throw new Error('Failed to fetch ChatKit session');
                }
                const data = await response.json();
                setClientSecret(data.client_secret);
            } catch (error) {
                console.error('ChatKit session error:', error);
            }
        };

        fetchSession();
    }, []);

    // T076 & T077: Handle text selection
    const handleMouseUp = () => {
        const selection = window.getSelection();
        const text = selection?.toString().trim();
        if (text && text.length > 10) { // Only show for reasonably long selections
            const range = selection.getRangeAt(0);
            const rect = range.getBoundingClientRect();
            setSelectedText(text);
            setAskButtonPosition({
                top: rect.bottom + window.scrollY + 5, // Position below selection
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
    
    // T078: Handle "Ask about this" button click
    const handleAskAboutSelection = () => {
        if (composerRef.current) {
            const query = `Based on the following text, can you explain it further?

---
${selectedText}
---`;
            composerRef.current.setText(query);
        }
        setIsOpen(true); // Open the chat window
        setAskButtonPosition({ top: 0, left: 0, display: 'none' }); // Hide the button
    };

    if (!clientSecret) {
        return null; // Or a loading indicator
    }

    return (
        <>
            {/* T075: Floating chatbot window */}
            <div style={{ position: 'fixed', bottom: '20px', right: '20px', zIndex: 1000 }}>
                <ChatKit
                    clientSecret={clientSecret}
                    assistantId={ASSISTANT_ID}
                    isOpen={isOpen}
                    onClose={() => setIsOpen(false)}
                    onOpen={() => setIsOpen(true)}
                >
                        {/* T073: ChatKit UI Components */}
                    <ChatKitWindow>
                        <header>
                            <ChatKitAvatar name="Book Assistant" />
                            <h3>Book Assistant</h3>
                        </header>
                        <ChatKitMessageList />
                        <ChatKitComposer ref={composerRef} />
                    </ChatKitWindow>
                </ChatKit>
            </div>
            {/* "Ask about this" button */}
            <button
                style={{
                    position: 'absolute',
                    top: `${askButtonPosition.top}px`,
                    left: `${askButtonPosition.left}px`,
                    display: askButtonPosition.display,
                    zIndex: 1001,
                    padding: '5px 10px',
                    borderRadius: '5px',
                    border: '1px solid #ccc',
                    background: '#fff',
                    cursor: 'pointer',
                    boxShadow: '0 2px 5px rgba(0,0,0,0.1)',
                }}
                onClick={handleAskAboutSelection}
            >
                Ask about this
            </button>
        </>
    );
};

export default Chatbot;
