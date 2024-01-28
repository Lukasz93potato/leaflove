import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../css/Folders.css';
import nice_plant from '../img/nice_plant.jpg';
import water_button from '../img/water_button.svg';
import fertilizer_button from '../img/fertilizer_button.svg';
import add_plant_button from '../img/addPlantButton.svg';

const Folders = () => {
  const [plants, setPlants] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedFolder, setSelectedFolder] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/app/plants/')
      .then(response => {
        setPlants(response.data);
      })
      .catch(error => {
        console.error('Error loading plants', error);
      });
  }, []);

  const handleDelete = async (plantId) => {
    try {
      await fetch(`http://localhost:8000/app/delete-plant/${plantId}/`, {
        method: 'DELETE',
      });
      setPlants(prevPlants => prevPlants.filter(plant => plant.id !== plantId));
      console.log('Plant deleted successfully');
    } catch (error) {
      console.error('Error deleting plant', error);
    }
  };

  const handleWaterButtonClick = async () => {
    if (selectedFolder) {
      // Update the state locally
      var currentDate = new Date();

      var year = currentDate.getFullYear();
      var month = String(currentDate.getMonth() + 1).padStart(2, '0'); // Months are zero-based, so we add 1
      var day = String(currentDate.getDate()).padStart(2, '0');

      var formattedDate = year + '-' + month + '-' + day;

      const updatedSelectedFolder = { ...selectedFolder, water_last: formattedDate}; //new Date().toISOString()
      setSelectedFolder(updatedSelectedFolder);
      console.log(updatedSelectedFolder.water_last);
      // Make a request to update the server data
      try {
        await axios.patch(`http://localhost:8000/app/update-plant-water-last/${selectedFolder.id}/`, {
          water_last: updatedSelectedFolder.water_last,
        });
        console.log('Watering date updated successfully on the server');
      } catch (error) {
        console.error('Error updating watering date on the server', error);
      }
    }
  };

  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleFolderSelect = (plantId) => {
    const selectedPlant = plants.find(plant => plant.id === plantId);
    setSelectedFolder(selectedPlant);
  };

  const filteredPlants = plants.filter(plant =>
    plant.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="base-container">
      <main>
        <section className = "folders_page_layout">
        <section className="plant_card">
            {selectedFolder ? (
              <>
                <img src={selectedFolder.image} alt={selectedFolder.name}></img>
                <div className="plantcard-name">{selectedFolder.name}</div>
                <div className="plantcard-water">Last time watered: {selectedFolder.water_last}</div>
                <div className="plantcard-fertilizer">Last time fertilized: {selectedFolder.fertilizer_last}</div>
                <div className="plantcard-buttons">
                  <button className="water-button" data-plant-id={selectedFolder.id} onClick={handleWaterButtonClick}>
                    <img src={water_button} alt="water_the_plant"></img>
                  </button>
                  <button className="fertilizer-button" data-plant-id={selectedFolder.id}>
                    <img src={fertilizer_button} alt="fertilize_the_plant"></img>
                  </button>
                </div>
              </>
            ) : (
              <div>
                {/* Default content when no folder is selected */}
              </div>
            )}
        </section>
        <section className="search_bar_and_folders">
        <section className="search_bar">
        <input
            type="searchbar"
            placeholder="Search by name"
            value={searchTerm}
            onChange={handleSearchChange}
          />
        </section>
        <section className="folders">
          {filteredPlants.map(plant => (
            <div
                 className={`folder-container ${selectedFolder && selectedFolder.id === plant.id ? 'selected' : ''}`}
                 data-plant-id={plant.id}
                 data-water-last={plant.water_last}
                 data-fertilizer-last={plant.fertilizer_last}
                 onClick={() => handleFolderSelect(plant.id)}
            >
              <img src={plant.image} alt={plant.name} />
              <div className="name-container">
                <h2>{plant.name}</h2>
                <div>
                  {plant.tags && plant.tags.map((tag, index) => (
                    <span key={index} className="tag">{tag}</span>
                  ))}
                </div>
                <div className="notification">
                  <button onClick={() => handleDelete(plant.id)}>Usuń</button>
                </div>
              </div>
            </div>
          ))}
          <div className="folder-container">
            <a href="/AddPlant">
              <img src={add_plant_button} alt="Add new plant" />
            </a>
            <div className="name-container">
              <h2>add new</h2>
              <div className="notification"></div>
            </div>
          </div>
        </section>
        </section>
        </section>
      </main>
    </div>
  );
};

export default Folders;