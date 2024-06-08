import React, { useState } from "react";
import axios from 'axios';

const ChatBox = () => {
  const [pdfFile, setPdfFile] = useState(null);
  const [textPrompt, setTextPrompt] = useState('');
  const [prompts, setPrompts] = useState([]);

  const handleFileChange = (e) => {
    setPdfFile(e.target.files[0]);
  };

  const handlePromptChange = (e) => {
    setTextPrompt(e.target.value);
  };

  const handleUpload = () => {
    const formData = new FormData();
    formData.append('pdf', pdfFile);
    formData.append('prompt', textPrompt);

    axios.post('http://127.0.0.1:5003/get_prompts', formData)
      .then(response => {
        setPrompts(response.data.prompts);
      })
      .catch(error => console.error(error));
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <div className="max-w-2xl mx-auto bg-white shadow-md rounded-md p-6 space-y-6">
        <h1 className="text-2xl font-bold text-center">Automatic Prompt Generation</h1>
        <div className="form-control">
          <label className="label">
            <span className="label-text">Upload PDF File</span>
          </label>
          <input type="file" className="file-input file-input-bordered w-full" onChange={handleFileChange} />
        </div>
        <div className="form-control">
          <label className="label">
            <span className="label-text">Enter Text Prompt</span>
          </label>
          <textarea className="textarea textarea-bordered h-24" value={textPrompt} onChange={handlePromptChange}></textarea>
        </div>
        <button className="btn btn-primary w-full" onClick={handleUpload}>Generate Prompts</button>
        <div>
          <h2 className="text-xl font-bold mt-4">Generated Prompts</h2>
          <div className="space-y-2 mt-2">
            {prompts.map((prompt, index) => (
              <div key={index} className="p-4 bg-gray-200 rounded-md">
                {prompt}
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};



export default ChatBox;