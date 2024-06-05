import React, { useState } from "react";
import axios from 'axios';

const ChatBox = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const handleSend = async () => {
    if (input.trim()) {
      const newMessages = [...messages, { sender: "user", text: input }];
      setMessages(newMessages);
      setInput("");

      try {
        const response = await axios.post('http://localhost:5000/generate_prompt', {
          topic: input,
        });

        const aiResponse = response.data.prediction;

        setMessages((prevMessages) => [
          ...prevMessages,
          { sender: "ai", text: aiResponse },
        ]);
      } catch (error) {
        console.error("Error on fetching generated prompts:", error);
        setMessages((prevMessages) => [
          ...prevMessages,
          { sender: "ai", text: "Error on fetching prompts." },
        ]);
      }
    }
  };

  return (
    <div className="flex flex-col items-center p-4 bg-white min-h-screen">
      <h1 className="text-3xl text-slate-800 mt-16 font-extrabold">Amharic News Classifier</h1>
      <div className="bg-slate-800 w-full max-w-lg rounded-lg shadow-lg p-4 mt-16">
        <div className="h-96 overflow-y-auto">
          {messages.map((msg, index) => (
            <div key={index} className={`chat ${msg.sender === "user" ? "chat-end" : "chat-start"}`}>
              <div className="chat-bubble bg-white text-black">
                {msg.text}
              </div>
            </div>
          ))}
        </div>
        <div className="flex mt-4">
          <input
            type="text"
            className="input input-bordered flex-grow bg-white text-black"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === "Enter" && handleSend()}
          />
          <button className="btn btn-primary ml-2 bg-white text-black" onClick={handleSend}>
            Send
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatBox;