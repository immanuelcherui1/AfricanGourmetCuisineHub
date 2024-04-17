import  { useState } from 'react';
import axios from 'axios';

function RecipeForm() {
    const [formData, setFormData] = useState({
        title: '',
        ingredients: '',
        instructions: '',
        country: '',
        image: null
    });

    const handleChange = (e) => {
        const value = e.target.type === 'file' ? e.target.files[0] : e.target.value;
        setFormData({ ...formData, [e.target.name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = new FormData();
        data.append('title', formData.title);
        data.append('ingredients', formData.ingredients);
        data.append('instructions', formData.instructions);
        data.append('country', formData.country);
        data.append('image', formData.image);

        try {
            const response = await axios.post('http://localhost:5000/api/recipes', data, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            console.log('Response:', response.data);
        } catch (error) {
            console.error('Error posting recipe', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}  >
            <label>Title: <input type="text" name="title" value={formData.title} onChange={handleChange} /></label>
            <label>Ingredients: <textarea name="ingredients" value={formData.ingredients} onChange={handleChange}></textarea></label>
            <label>Instructions: <textarea name="instructions" value={formData.instructions} onChange={handleChange}></textarea></label>
            <label>Country: <input type="text" name="country" value={formData.country} onChange={handleChange} /></label>
            <label>Image: <input type="file" name="image" onChange={handleChange} /></label>
            <button type="submit">Submit Recipe</button>
        </form>
    );
}

export default RecipeForm;
