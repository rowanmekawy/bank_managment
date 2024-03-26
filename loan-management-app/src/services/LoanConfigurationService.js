import axios from 'axios';

const API_URL = 'http://localhost:8000/loan-configuration/';

export default {
  getLoanConfigurations() {
    return axios.get(API_URL, {
      headers: {
        'Authorization': `Token ${localStorage.getItem('token')}`,
      },
    });
  },
};
