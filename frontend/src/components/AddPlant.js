import React, { useState } from 'react';
import axios from 'axios';
import '../css/AddPlant.css';
import x_button from '../img/x_button.svg';

const AddPlant = () => {
  const [name, setName] = useState('');
  const [file, setFile] = useState(null);
  const [waterLast, setWaterLast] = useState('');
  const [waterCycle, setWaterCycle] = useState('');
  const [fertilizerLast, setFertilizerLast] = useState('');
  const [fertilizerCycle, setFertilizerCycle] = useState('');
  const [messages, setMessages] = useState([]);

  const handleSubmit = (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('name', name);
    formData.append('image', file);  // Nazwa 'image' powinna odpowiadać nazwie pola w modelu Django
    formData.append('water_last', waterLast);
    formData.append('water_cycle', waterCycle);
    formData.append('fertilizer_last', fertilizerLast);
    formData.append('fertilizer_cycle', fertilizerCycle);

    axios.post('http://localhost:8000/app/add-plant/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
    .then(response => {
      console.log(response);
      setMessages(['Plant added successfully']);
      // Możesz tutaj dodać dodatkowe działania po pomyślnym dodaniu
    })
    .catch(error => {
      console.error('Error submitting form', error);
      setMessages(['Error submitting form']);
    });
  };

  return (
    <main>

      <section className="folder-form">
        <a href="/folders">
          <img src={x_button} alt="Close" className="button" />
        </a>
        <h1>Add new plant</h1>
        <form onSubmit={handleSubmit} encType="multipart/form-data">
          {messages.map((message, index) => <div key={index}>{message}</div>)}
          <input name="name" type="name" placeholder="Plant name" onChange={e => setName(e.target.value)} />
          <input type="file" name="file" onChange={e => setFile(e.target.files[0])} />
          <label>Last time watered:</label>
          <input type="date" name="water_last" value={waterLast} onChange={e => setWaterLast(e.target.value)} />
          <label>Watering cycle:</label>
          <input name="water_cycle" type="number" placeholder="Water cycle" step="1" onChange={e => setWaterCycle(e.target.value)} />
          <label>Last time fertilized:</label>
          <input type="date" name="fertilizer_last" value={fertilizerLast} onChange={e => setFertilizerLast(e.target.value)} />
          <label>Fertilizer cycle:</label>
          <input name="fertilizer_cycle" type="number" placeholder="Fertilizer cycle" step="1" onChange={e => setFertilizerCycle(e.target.value)} />
          <button type="submit">Send</button>
        </form>
      </section>
    </main>
  );
};

export default AddPlant;