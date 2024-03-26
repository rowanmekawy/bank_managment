<template>
  <v-container>
    <!-- Registration Form -->
    <v-form @submit.prevent="register">
      <v-alert v-if="errorMessage" type="error" dismissible @click="errorMessage = ''">
        {{ errorMessage }}
      </v-alert>
      <v-text-field
        v-model="newUser.username"
        label="Username"
        required
      ></v-text-field>
      <v-text-field
        v-model="newUser.password"
        label="Password"
        type="password"
        required
      ></v-text-field>
      <v-btn type="submit" color="primary">Create Account</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import AuthService from '@/services/AuthService';

export default {
  data() {
    return {
      newUser: {
        username: '',
        password: '',
      },
      errorMessage: '',
    };
  },
  methods: {
    register() {
      AuthService.register(this.newUser)
        .then(() => {
          this.errorMessage = '';
          // Registration successful, redirect to login page
          this.$router.push('/user-login');
        })
        .catch(error => {
          console.error('Registration error:', error);
          this.errorMessage = 'Registration error. Please try again later.';
        });
    },
  },
};
</script>
