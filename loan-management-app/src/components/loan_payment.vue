<template>
  <v-container>
    <v-alert v-if="errorMessage" type="error" dismissible @click="errorMessage = ''">
        {{ errorMessage }}
      </v-alert>
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>
            Loan Payments
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="openCreateDialog">Create Payment</v-btn>
          </v-card-title>
          <v-data-table
            :headers="headers"
            :items="payments"
            item-key="id"
          ></v-data-table>
        </v-card>
      </v-col>
    </v-row>

    <!-- Create Payment Dialog -->
    <v-dialog v-model="createDialog" max-width="500px">
      <v-card>
        <v-card-title>Create Payment</v-card-title>
        <v-card-text>
          <v-form>
            <v-text-field v-model="newPayment.amount_paid" label="Amount Paid"></v-text-field>
            <!-- <v-text-field v-model="newPayment.loan" label="Loan ID"></v-text-field> -->
            <v-select
            v-model="newPayment.loan"
            :items="loans"
            item-value="id"
            :item-text="item => `Amount: ${item.amount}`"
            label="Loan"
          ></v-select>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="createDialog = false">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="createLoanPayment">Create</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import LoanPaymentService from '@/services/LoanPaymentService';
import LoanApplicationService from '@/services/LoanApplicationService';

export default {
  data() {
    return {
      errorMessage: '',
      payments: [],
      loans: [],
      headers: [
        { text: 'ID', value: 'id' },
        { text: 'Amount Paid', value: 'amount_paid' },
        { text: 'Loan ID', value: 'loan' },
        { text: 'Status', value: 'status' },
      ],
      createDialog: false,
      newPayment: {
        amount_paid: '',
        loan: null,
      },
    };
  },
  mounted() {
    this.fetchLoanPayments();
  },
  methods: {
    fetchLoanPayments() {
      LoanPaymentService.getLoanPayments()
        .then(response => this.payments = response.data)
        .catch(error => {
          this.errorMessage = 'Error fetching loan payments. Please try again later.';
          console.error('Error fetching loan payments:', error)
        });
    },
    openCreateDialog() {
      this.createDialog = true;
      this.fetchLoans();
    },
    createLoanPayment() {
      LoanPaymentService.createLoanPayment(this.newPayment)
        .then(() => {
          this.createDialog = false;
          this.fetchLoanPayments();
        })
        .catch(error => {
          this.errorMessage = 'Error fcreating loan payments. Please try again later.';
          console.error('Error creating loan payment:', error)
        });
        
    },
    fetchLoans() {
      LoanApplicationService.getLoanApplications()
        .then(response => {
          this.loans = response.data;
        })
        .catch(error => {
          this.errorMessage = 'Error fetching loans. Please try again later.';
          console.error('Error fetching loans:', error);
        });
    },
  },
};
</script>

