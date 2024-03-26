import axios from 'axios';

const API_URL = 'http://localhost:8000/loan-payment/';

export default {
  createLoanPayment(payload) {
    return axios.post(API_URL, payload, {
        headers: {
          'Authorization': `Token ${localStorage.getItem('token')}`
        }
      })
      .catch(error => {
        throw error.response.data;
      });
  },
  getLoanPayments() {
    return axios.get(API_URL, {
        headers: {
          'Authorization': `Token ${localStorage.getItem('token')}`
        }
      })
      .catch(error => {
        throw error.response.data;
      });
  },
  updateLoanPayment(id, payload) {
    return axios.put(`${API_URL}${id}/`, payload, {
        headers: {
          'Authorization': `Token ${localStorage.getItem('token')}`
        }
      })
      .catch(error => {
        throw error.response.data;
      });
  },
  deleteLoanPayment(id) {
    return axios.delete(`${API_URL}${id}/`, {
        headers: {
          'Authorization': `Token ${localStorage.getItem('token')}`
        }
      })
      .catch(error => {
        throw error.response.data;
      });
  },
};
