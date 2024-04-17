import React from "react";
import { Slide } from 'react-slideshow-image';
import 'react-slideshow-image/dist/styles.css';

import foodImage1 from "./image/image.jpg";
import foodImage2 from "./image/image2.jpg";
import foodImage3 from "./image/AdobeStock_319447161_Preview.jpeg";
import foodImage4 from "./image/AdobeStock_533000353_Preview.jpeg";
import foodImage5 from "./image/AdobeStock_615243490_Preview.jpeg";

function Home() {
  const images = [foodImage1, foodImage2, foodImage3, foodImage4, foodImage5];

  return (
    <div style={{ position: 'relative', width: '100%', height: '600px' }}>
      {/* Slideshow container */}
      <Slide easing="ease" duration={2000} transitionDuration={500} infinite={true} indicators={true} arrows={false} autoplay={true}>
        {images.map((each, index) => (
          <div key={index} className="each-slide" style={{ 'backgroundImage': `url(${each})`, width: '100%', height: '600px', backgroundSize: 'cover', backgroundPosition: 'center' }}>
            {/* Optional overlay or content could go here */}
          </div>
        ))}
      </Slide>

      {/* Welcome Text Overlay */}
      <div style={{ position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', color: 'white', textAlign: 'center', zIndex: 20, fontSize: '1.3rem', // Set background color to black
    padding: '20px', // Add some padding around the text
    borderRadius: '15px', // Rounded corners
    }}>
        <h1>Welcome to Africa Gourmet Cuisine Hub</h1>
        <h3>We have the best recipes for making your favorite food.</h3>
      </div>

      {/* Navigation bar positioned on top of the slideshow */}
      <nav style={{ position: 'absolute', top: '20px', right: '20px', display: 'inline-block' }}>
        <ul style={{ listStyleType: 'none', margin: 0, padding: 0, display: 'flex', fontSize: '1.2rem', zIndex: 10 }}>
          <li style={{ margin: '0 20px' }}><a href="#" style={{ color: 'white' }}>Home</a></li>
          <li style={{ margin: '0 20px' }}><a href="#" style={{ color: 'white' }}>Dashboard</a></li>
          <li style={{ margin: '0 20px' }}><a href="#" style={{ color: 'white' }}>Profile</a></li>
          <li style={{ margin: '0 20px' }}><a href="#" style={{ color: 'white' }}>About</a></li>
          <li style={{ margin: '0 30px', backgroundColor: 'red', boxShadow: '0px 4px 8px rgba(0, 0, 0, 0.5)' }}>
            <a href="#" style={{ color: 'white', padding: '20px 25px' }}>Guest</a>
          </li>
        </ul>
      </nav>
    </div>
  );
}

export default Home;
