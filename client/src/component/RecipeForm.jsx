import { useState } from 'react';
import axios from 'axios';

const RecipeForm = () => {
    const [formData, setFormData] = useState({
        title: '',
        ingredients: '',
        instructions: '',
        area: ''

    });

    const handleChange = e => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const handleSubmit = async e => {
        e.preventDefault();
        try {
            const response = await axios.post('/submit_recipe', formData);
            console.log(response.data.message);
        } catch (error) {
            console.error('Error submitting recipe:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" name="title" value={formData.title} onChange={handleChange} placeholder="Title" />
            <textarea name="ingredients" value={formData.ingredients} onChange={handleChange} placeholder="Ingredients"></textarea>
            <textarea name="instructions" value={formData.instructions} onChange={handleChange} placeholder="Instructions"></textarea>
            <textarea name="country" value={formData.area} onChange={handleChange} placeholder="country"></textarea>
            <button type="submit">Submit</button>
        </form>
    );
};

export default RecipeForm;
