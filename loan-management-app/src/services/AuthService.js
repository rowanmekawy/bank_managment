import axios from 'axios';

const API_URL = 'http://localhost:8000/';

export default {
  login(credentials) {
    console.log(credentials)
    return axios.post(`${API_URL}user/token/`, credentials);
  },
  register(userData) {
    return axios.post(`${API_URL}users/`, userData);
  }
};
