import '../static/App.css';

import { useState, useEffect } from 'react';
import axios from 'axios';
import { Route, Routes, Link } from 'react-router-dom'

function StartConversation()
{
    const[roomName, setRoomName] = useState('')
    const [roomPassword, setRoomPassword] = useState('');
    const [confidential, setConfidential] = useState(false)

    const handleSubmit = (event) => {
        event.preventDefault()
        const data = {
            name: roomName,
            password: roomPassword,
            confidential: confidential
        }
        axios.post('http://localhost:8000/api/start-conversation', data)
        .then(res => console.log(res))
    };

  return (
    <form onSubmit={handleSubmit}>
        <label>
            Room Name:
        </label>
        <input
          type="text"
          value={roomName}
          onChange={(e) => setRoomName(e.target.value)}
        />
      <br />
        <label>
            Room Password:
        </label>
        <input
          type="password"
          value={roomPassword}
          onChange={(e) => setRoomPassword(e.target.value)}
        />
      <br />
      <label>
            Confidential:
        </label>
        <input
          type="checkbox"
          value={confidential}
          onChange={(e) => e.target.checked ? setConfidential(true) : setConfidential(false)}
        />
      <button type="submit">Submit</button>
    </form>
  );
};

export default StartConversation;
