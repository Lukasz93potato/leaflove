import React, { useState } from 'react';
import '../css/style.css';
// Pamiętaj, żeby zaimportować obrazki, które chcesz używać
import backgroundImg from '../img/background_img.png';
import logInImg from '../img/log_in.svg';
import signUpImg from '../img/sign_up.svg';

function Login() {
    const [messages, setMessages] = useState([]); // Zakładam, że będziesz chciał tu przechować jakieś komunikaty

    // Tutaj można dodać logikę komunikacji z serwerem lub inne funkcje

    return (
        <div className="container">
            <div className="leaflove-container">
                <img src={backgroundImg} alt="Background" />
                {/* Jeżeli chcesz użyć obrazka leaf_love.svg, musisz go zaimportować podobnie jak powyżej */}
                {/* <img src={leafLoveImg} alt="Leaf Love" /> */}
            </div>

            <form action="login" method="POST">
                <div className="messages">
                    {messages.map((message, index) => <div key={index}>{message}</div>)}
                </div>
                <input className="login" name="email" type="text" placeholder="Login" />
                <input className="login" name="password" type="password" placeholder="Password" />

                <button className="button" type="submit">
                    <img src={logInImg} alt="Log In" />
                </button>
            </form>

            <a href="http://localhost/web/register">
                <img src={signUpImg} alt="Sign Up" />
            </a>
        </div>
    );
}

export default Login;