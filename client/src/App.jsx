import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import RecipeForm from './RecipeForm';

function App() {
  return (
    <Router>
      <div>
        {/* Navigation bar, sidebar, etc., can be placed here */}
        <Routes>
          <Route path="/" element={<RecipeForm />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
