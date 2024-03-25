import axios from 'axios';

const API_URL = 'http://localhost:8000/loan-payment/';

// TODO remove token and implment login and auth token pages
const token = '6ea1bbc6f958eebd3f79813fc3245832a57f3250';
localStorage.setItem('token', token);

export default {
  createLoanPayment(payload) {
    return axios.post(API_URL, payload, {
        headers: {
          'Authorization': `Token ${token}`
        }
      })
      .catch(error => {
        throw error.response.data;
      });
  },
  getLoanPayments() {
    return axios.get(API_URL, {
        headers: {
          'Authorization': `Token ${token}`
        }
      })
      .catch(error => {
        throw error.response.data;
      });
  },
  updateLoanPayment(id, payload) {
    return axios.put(`${API_URL}${id}/`, payload, {
        headers: {
          'Authorization': `Token ${token}`
        }
      })
      .catch(error => {
        throw error.response.data;
      });
  },
  deleteLoanPayment(id) {
    return axios.delete(`${API_URL}${id}/`, {
        headers: {
          'Authorization': `Token ${token}`
        }
      })
      .catch(error => {
        throw error.response.data;
      });
  },
};
