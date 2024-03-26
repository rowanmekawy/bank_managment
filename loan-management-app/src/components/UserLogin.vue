<template>
  <v-container>
    <!-- Login Form -->
    <v-form @submit.prevent="login">
      <v-alert v-if="errorMessage" type="error" dismissible @click="errorMessage = ''">
        {{ errorMessage }}
      </v-alert>
      <v-text-field
        v-model="credentials.username"
        label="Username"
        required
      ></v-text-field>
      <v-text-field
        v-model="credentials.password"
        label="Password"
        type="password"
        required
      ></v-text-field>
      <v-btn type="submit" color="primary">Login</v-btn>
    </v-form>

    <!-- Redirect to Registration Page -->
    <v-btn @click="redirectToRegistration" color="secondary">Create Account</v-btn>
  </v-container>
</template>

<script>
import AuthService from '@/services/AuthService';
export default {
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      },
      errorMessage: '',
    };
  },
  methods: {
    logout() {
        localStorage.clear();
        this.$router.push('/login'); // Redirect to the login page
      },
    login() {
      AuthService.login(this.credentials)
        .then(response => {
          localStorage.clear();
          this.errorMessage = '';
          const token = response.data.token;
          localStorage.setItem('token', token); // Save the token in local storage
          this.$router.push('/loan-application'); // Redirect to the loan-payment
        })
        .catch(error => {
          console.error('Login error:', error);
          this.errorMessage = 'Failed to login. Please try again later.';
        });
    },
    redirectToRegistration() {
      localStorage.clear();
      this.$router.push('/user-register');
    },
  },
};
</script>
