<template>
  <v-container>
    <v-alert v-if="errorMessage" type="error" dismissible @click="errorMessage = ''">
        {{ errorMessage }}
      </v-alert>
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>
            Loan Applications
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="openCreateDialog">Create Loan Application</v-btn>
          </v-card-title>
          <v-data-table
            :headers="headers"
            :items="applications"
            item-key="id"
          ></v-data-table>
        </v-card>
      </v-col>
    </v-row>

    <!-- Create Application Dialog -->
    <v-dialog v-model="createDialog" max-width="500px">
      <v-card>
        <v-card-title>Create Application</v-card-title>
        <v-card-text>
          <v-form>
            <v-text-field v-model="newApplication.amount" label="Amount"></v-text-field>
            <v-text-field v-model="newApplication.term_months" label="Term (Months)"></v-text-field>
            <v-select
                v-model="newApplication.loan_configuration"
                :items="loanConfigurations"
                item-value="id"
                :item-text="item => `Interest Rate: ${item.interest_rate}, Duration: ${item.duration}`"
                label="Loan Configuration"
                ></v-select>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeCreateDialog">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="createLoanApplication">Create</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-btn color="secondary" @click="redirectToLoanPayment">Go to Loan Payments</v-btn>
  </v-container>
</template>

<script>
import LoanApplicationService from '@/services/LoanApplicationService';
import LoanConfigurationService from '@/services/LoanConfigurationService';


export default {
  data() {
    return {
      errorMessage: '',
      applications: [],
      loanConfigurations: [],
      newApplication: {
        amount: '',
        term_months: 0,
        loan_configuration: 0,
      },
      createDialog: false,
      headers: [
        { text: 'Amount', value: 'amount' },
        { text: 'Term (Months)', value: 'term_months' },
        { text: 'Status', value: 'status' },
        { text: 'Remaining Amount', value: 'remaining_amount' },
      ],
    };
  },
  methods: {
    
    fetchLoanApplications() {
      LoanApplicationService.getLoanApplications()
        .then(response => {
          this.errorMessage = '';
          this.applications = response.data;
        })
        .catch(error => {
          this.errorMessage = 'Error fetching loan applications. Please try again later.';
          console.error('Error fetching loan applications:', error);
        });
    },
    createLoanApplication() {
      LoanApplicationService.createLoanApplication(this.newApplication)
        .then(response => {
          this.errorMessage = '';
          this.applications.push(response.data);
          this.closeCreateDialog();
        })
        .catch(error => {
          this.errorMessage = 'Error creating loan application. Please try again later.';
          console.error('Error creating loan application:', error);
        });
    },
    openCreateDialog() {
      this.createDialog = true;
      this.fetchLoanConfigurations();
    },
    closeCreateDialog() {
      this.createDialog = false;
      this.resetNewApplication();
    },
    fetchLoanConfigurations() {
      console.log('Fetching loan configurations...');
      LoanConfigurationService.getLoanConfigurations()
        .then(response => {
          this.errorMessage = '';
          this.loanConfigurations = response.data;
        })
        .catch(error => {
          this.errorMessage = 'Error fetching loan configurations. Please try again later.';
          console.error('Error fetching loan configurations:', error);
        });
    },
    resetNewApplication() {
      this.newApplication = {
        amount: '',
        term_months: 0,
        loan_configuration: 0,
      };
    },
    redirectToLoanPayment() {
      this.$router.push('/loan-payment');
    },
  },
  mounted() {
    this.fetchLoanApplications();
  },
};
</script>
