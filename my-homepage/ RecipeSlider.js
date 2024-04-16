import React, { useState, useEffect } from 'react';

function RecipeSlider() {
    const [recipes, setRecipes] = useState([
        { title: "Pasta Carbonara", imageUrl: "/src/image/e18ca971264c418f1aad191e329a3737.jpg" },
        { title: "Chicken Tikka Masala", imageUrl: "path-to-image/chicken.jpg" },
        { title: "Beef Stew", imageUrl: "path-to-image/beef.jpg" }
    ]);
    const [currentSlide, setCurrentSlide] = useState(0);

    useEffect(() => {
        const interval = setInterval(() => {
            setCurrentSlide((currentSlide + 1) % recipes.length);
        }, 3000); // Change image every 3000 milliseconds
        return () => clearInterval(interval);
    }, [currentSlide, recipes.length]);

    return (
        <div>
            <h2>{recipes[currentSlide].title}</h2>
            <img src={recipes[currentSlide].imageUrl} alt={recipes[currentSlide].title} style={{ width: '100%', height: 'auto' }} />
        </div>
    );
}

export default RecipeSlider;
