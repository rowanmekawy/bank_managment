import axios from 'axios';

const API_URL = 'http://localhost:8000/loan-applications/';

export default {
  createLoanApplication(payload) {
    return axios.post(API_URL, payload, {
      headers: {
        'Authorization': `Token ${localStorage.getItem('token')}`,
      },
    });
  },
  getLoanApplications() {
    return axios.get(API_URL, {
      headers: {
        'Authorization': `Token ${localStorage.getItem('token')}`,
      },
    });
  },
};
