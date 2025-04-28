<script>
import { Form } from '@primevue/forms';

export default {
  name: 'QuizFormPage',
  data() {
    return {
      quizName: '',
      description: '',
    };
  },
  methods: {
    submitForm() {
      console.log('Form submitted!', {
        quizName: this.quizName,
        description: this.description,
      });
    },
  },
};
</script>

<template>
  <h2>Create a quiz</h2>
  <Form v-slot="$form" :initialValues :resolver="resolver" @submit="submitForm" class="flex flex-col gap-4 w-full sm:w-56">
    <div class="p-fluid">
      <div class="p-field">
        <label for="quizName">Quiz Name</label>
        <input
          id="quizName"
          v-model="quizName"
          type="text"
          class="rounded-md outline"
          required
        />
      </div>
      <div class="p-field">
        <label for="description">Description</label>
        <textarea
          id="description"
          v-model="description"
          class="p-inputtext p-component"
          required
        ></textarea>
      </div>
      <button type="submit" class="p-button p-component">Submit</button>
    </div>
    </Form>
  <i class="pi pi-bitcoin" style="font-size: 1rem"></i>
</template>
