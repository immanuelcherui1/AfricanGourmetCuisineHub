import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faInstagram, faFacebook, faTwitter } from '@fortawesome/free-brands-svg-icons';

function Footer() {
    return (
        <footer style={{ backgroundColor: '#ff0000', color: 'white', textAlign: 'center', padding: '10px', position: 'fixed', bottom: 0, width: '100%' }}>
            <p>© 2024 Your Website Name</p>
            <div>
                <a href="https://www.instagram.com" target="_blank" rel="noopener noreferrer" style={{ color: 'white', margin: '0 10px' }}>
                    <FontAwesomeIcon icon={faInstagram} size="lg" />
                </a>
                <a href="https://www.facebook.com" target="_blank" rel="noopener noreferrer" style={{ color: 'white', margin: '0 10px' }}>
                    <FontAwesomeIcon icon={faFacebook} size="lg" />
                </a>
                <a href="https://www.twitter.com" target="_blank" rel="noopener noreferrer" style={{ color: 'white', margin: '0 10px' }}>
                    <FontAwesomeIcon icon={faTwitter} size="lg" />
                </a>
            </div>
        </footer>
    );
}

export default Footer;
