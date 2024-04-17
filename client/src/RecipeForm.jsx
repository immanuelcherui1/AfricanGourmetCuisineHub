import React, { useState } from 'react';
import axios from 'axios';

function RecipeForm() {
  const [recipeData, setRecipeData] = useState({
    title: '',
    instructions: '',
    authorName: '',
    country: '',
    category: ''
  });
  const [image, setImage] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setRecipeData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('title', recipeData.title);
    formData.append('instructions', recipeData.instructions);
    formData.append('authorName', recipeData.authorName);
    formData.append('country', recipeData.country);
    formData.append('category', recipeData.category);
    if (image) {
      formData.append('image', image);
    }

    try {
      const response = await axios.post('/recipes', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      console.log('Recipe created:', response.data);
      // Clear the form or give feedback to the user
    } catch (error) {
      console.error('Error posting recipe:', error.response.data);
      // Display error message to the user
    }
  };

  return (
    <div>
      <h1>Create Recipe</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Title:</label>
          <input
            type="text"
            name="title"
            value={recipeData.title}
            onChange={handleChange}
          />
        </div>
        <div>
          <label>Instructions:</label>
          <textarea
            name="instructions"
            value={recipeData.instructions}
            onChange={handleChange}
          />
        </div>
        <div>
          <label>Author Name:</label>
          <input
            type="text"
            name="authorName"
            value={recipeData.authorName}
            onChange={handleChange}
          />
        </div>
        <div>
          <label>Country:</label>
          <input
            type="text"
            name="country"
            value={recipeData.country}
            onChange={handleChange}
          />
        </div>
        <div>
          <label>Category:</label>
          <input
            type="text"
            name="category"
            value={recipeData.category}
            onChange={handleChange}
          />
        </div>
        <div>
          <label>Image:</label>
          <input
            type="file"
            onChange={(e) => setImage(e.target.files[0])}
          />
        </div>
        <button type="submit">Submit Recipe</button>
      </form>
    </div>
  );
}

export default RecipeForm;
