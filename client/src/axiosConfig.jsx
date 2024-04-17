import axios from 'axios';

// Set the base URL for all Axios requests
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:5555';

const axiosInstance = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Adding a request interceptor
axiosInstance.interceptors.request.use(request => {
  console.log('Starting Request', request);
  // You could also inject the auth token here
  return request;
}, error => {
  console.error('Error starting request:', error);
  return Promise.reject(error);
});

// Adding a response interceptor
axiosInstance.interceptors.response.use(response => {
  console.log('Response:', response);
  return response;
}, error => {
  console.error('Error:', error.response);
  return Promise.reject(error);
});

export default axiosInstance;
