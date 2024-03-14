import '../static/App.css';

import { useState, useEffect } from 'react';
import axios from 'axios';
import { Route, Routes, Link } from 'react-router-dom'

function JoinConversation() {
    const [roomId, setRoomId] = useState(0);
    const [roomPassword, setRoomPassword] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault()
        const data = {
            password: roomPassword
        }
        axios.post(`http://localhost:8000/api/join-conversation/${roomId}`, data)
        .then((res) => {
            console.log(res)
        })
    };

    return (
    <form onSubmit={handleSubmit}>
        <label>
            Room ID:
        <input
            type="number"
            value={roomId}
            onChange={(e) => setRoomId(e.target.value)}
        />
        </label>
        <br />
        <label>
            Room Password:
        <input
            type="password"
            value={roomPassword}
            onChange={(e) => setRoomPassword(e.target.value)}
        />
        </label>
        <br />
        <button type="submit">Submit</button>
    </form>
  );
};

export default JoinConversation;
