<template>
  <v-container>
    <!-- Registration Form -->
    <v-form @submit.prevent="register">
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
    };
  },
  methods: {
    register() {
      AuthService.register(this.newUser)
        .then(() => {
          // Registration successful, redirect to login page
          this.$router.push('/user-login');
        })
        .catch(error => {
          console.error('Registration error:', error);
        });
    },
  },
};
</script>
