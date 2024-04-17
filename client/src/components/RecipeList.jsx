import  { useState, useEffect } from 'react';
import axios from 'axios';

const RecipeList = () => {
    const [recipes, setRecipes] = useState([]);

    // Fetch recipes from the server
    useEffect(() => {
        const fetchRecipes = async () => {
            try {
                const response = await axios.get('/api/recipes');
                setRecipes(response.data); // Assuming the API returns an array of recipes
            } catch (error) {
                console.error('Error fetching recipes:', error);
            }
        };

        fetchRecipes();
    }, []);

    return (
        <div>
            <h2>Recipes List</h2>
            <ul>
                {recipes.length > 0 ? (
                    recipes.map((recipe) => (
                        <li key={recipe.id}>
                            <h3>{recipe.title}</h3>
                            <p>Ingredients: {recipe.ingredients}</p>
                            <p>Instructions: {recipe.instructions}</p>
                            <p>Country: {recipe.country}</p>
                            {recipe.image && <img src={recipe.image} alt={recipe.title} style={{ width: "100px" }} />}
                        </li>
                    ))
                ) : (
                    <p>No recipes available.</p>
                )}
            </ul>
        </div>
    );
};

export default RecipeList;
