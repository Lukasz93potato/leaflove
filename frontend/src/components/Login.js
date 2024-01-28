import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import '../css/style.css';
import backgroundImg from '../img/background_img.png';
import logInImg from '../img/log_in.svg';
import signUpImg from '../img/sign_up.svg';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [messages, setMessages] = useState([]);
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const response = await axios.post('http://localhost:8000/token/', { username, password });

            if (response.data.access) {
                localStorage.setItem('access_token', response.data.access);
                localStorage.setItem('refresh_token', response.data.refresh);
                axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
                navigate('/Folders'); // Przekierowanie do odpowiedniej strony po zalogowaniu
            } else {
                setMessages(["Nie udało się zalogować. Spróbuj ponownie."]);
            }
        } catch (error) {
            setMessages(["Błąd podczas logowania. Spróbuj ponownie."]);
        }
    };

    return (
        <div className="container">
            <div className="leaflove-container">
                <img src={backgroundImg} alt="Background" />
            </div>

            <form onSubmit={handleSubmit}>
                <div className="messages">
                    {messages.map((message, index) => <div key={index}>{message}</div>)}
                </div>
                <input
                    className="login"
                    name="username"
                    type="text"
                    placeholder="Login"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <input
                    className="login"
                    name="password"
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <button className="button" type="submit">
                    <img src={logInImg} alt="Log In" />
                </button>
            </form>

            <a href="/register">
                <img src={signUpImg} alt="Sign Up" />
            </a>
        </div>
    );
}

export default Login;