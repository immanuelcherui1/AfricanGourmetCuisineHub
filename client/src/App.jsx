import { useEffect, useState } from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import RecipeForm from './components/RecipeForm';
// import RecipeList from './components/RecipeList';
// import NotFoundPage from './components/NotFoundPage';


const App = () => {
  const [data, setData] = useState(''); // State to store the fetched data

  useEffect(() => {
    fetch('/api/data')
    .then(response => response.json())
    .then(data => setData(data.message)) // Update state with the fetched message
    .catch(err => console.error("Error fetching data: ", err)); // Log errors to console
  }, []); // Empty dependency array means this effect runs once after the initial render

  return (
    <Router>
      <div className="App">
        <header className="App-header">
            <p>{data || "Loading..."}  Display the fetched data or a loading message</p>
        </header>
        <div>
          <h1>African Gourmet Cuisine Hub</h1>
          <Routes>
            <Route path="/" element={<RecipeForm />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default App;
