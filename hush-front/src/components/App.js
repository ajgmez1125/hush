import '../static/App.css';
import JoinConversation from './JoinConversation';
import StartConversation from './StartConversation';

import { useState, useEffect } from 'react';
import { Route, Routes, Link } from 'react-router-dom'

function App() {
  return (
    <div>
      <Routes>
        <Route path = '/' element = {<StartConversation />}/>
        <Route path = '/start-conversation' element = {<StartConversation />}/>
        <Route path = '/join-conversation' element = {<JoinConversation />}/>
      </Routes>
    </div>
  );
}

export default App;
