// src/router/index.js
import Vue from 'vue';
import Router from 'vue-router';
import UserLogin from '@/components/UserLogin';
import LoanPayment from '@/components/loan_payment';
import UserRegister from '@/components/UserRegister';
import LoanApplication from '@/components/LoanApplication';

Vue.use(Router);

export default new Router({
  mode: 'history', 
  routes: [
    {
      path: '/user-login',
      name: 'UserLogin',
      component: UserLogin,
    },
    {
      path: '/user-register',
      name: 'UserRegister',
      component: UserRegister,
    },
    {
      path: '/loan-application',
      name: 'LoanApplication',
      component: LoanApplication,
      meta: { requiresAuth: true },
    },
    {
      path: '/loan-payment',
      name: 'LoanPayment',
      component: LoanPayment,
      meta: { requiresAuth: true },
    },
  ],
});
