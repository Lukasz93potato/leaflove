import React, { useState } from 'react';
import axios from 'axios';
import '../css/Register.css'; // Zakładając, że CSS jest dostosowany do Reacta

const Register = () => {
  const [first_name, setName] = useState('');
  const [last_name, setSurname] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmedPassword, setConfirmedPassword] = useState('');
  const [messages, setMessages] = useState([]);

  const handleSubmit = (event) => {
    event.preventDefault();

    // Dane do wysłania na serwer
    const userData = { first_name, last_name, email, password, confirmedPassword };

    // Wysyłanie żądania POST na serwer
    axios.post('http://localhost:8000/register/', userData)
      .then(response => {
        // Obsługa odpowiedzi
        console.log(response);
        setMessages(['Registration successful']);
      })
      .catch(error => {
        // Obsługa błędów
        setMessages(['Error during registration', error.message]);
      });
  };

  return (
    <div className="folder-form">
      <h1>Welcome to LeafLove</h1>
      <form onSubmit={handleSubmit}>
        <div className="messages">
          {messages.map((message, index) => <div key={index}>{message}</div>)}
        </div>
        <input name="name" type="name" placeholder="name" value={first_name} onChange={e => setName(e.target.value)} />
        <input name="surname" type="name" placeholder="surname" value={last_name} onChange={e => setSurname(e.target.value)} />
        <input name="email" type="email" placeholder="email@email.com" value={email} onChange={e => setEmail(e.target.value)} />
        <input name="password" type="password" placeholder="password" value={password} onChange={e => setPassword(e.target.value)} />
        <input name="confirmedPassword" type="password" placeholder="confirm password" value={confirmedPassword} onChange={e => setConfirmedPassword(e.target.value)} />
        <button type="submit">Sign Up</button>
      </form>
    </div>
  );
};

export default Register;