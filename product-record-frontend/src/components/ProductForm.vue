<template>
  <div>
    <h1>{{ isEdit ? 'Edit' : 'Create' }} Product</h1>
    <form @submit.prevent="submitForm" enctype="multipart/form-data">
      <label>Name:</label>
      <input v-model="form.name" type="text" required />

      <label>Colour:</label>
      <input v-model="form.colour" type="text" required />

      <label>Part Number:</label>
      <input v-model="form.part_number" type="text" required />

      <label>Size (mm):</label>
      <input v-model.number="form.size_mm" type="number" min="1" required />

      <label>Description:</label>
      <textarea v-model="form.description"></textarea>

      <label>Image:</label>
      <input type="file" name="image" @change="onFileChange" />

      <button type="submit" class="btn btn-primary">{{ isEdit ? 'Update' : 'Create' }}</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { createProduct, updateProduct, fetchProduct } from '../services/productService';

interface Product {
  name: string;
  colour: string;
  part_number: string;
  size_mm: number;
  description?: string;
  image_url?: string;
}

const route = useRoute();
const router = useRouter();
const isEdit = route.params.id !== undefined;
const productId: string | number = Array.isArray(route.params.id)
  ? route.params.id[0]
  : route.params.id || '';

const form = reactive<Product>({
  name: "",
  colour: "",
  part_number: "",
  size_mm: 0,
  description: ""
});

const fileInput = ref<File | null>(null);

if (isEdit && productId) {
  fetchProduct(productId)
    .then((res) => Object.assign(form, res.data))
    .catch(err => console.error("Error fetching product:", err));
}

const onFileChange = (e: Event) => {
  const target = e.target as HTMLInputElement;
  if (target.files && target.files.length > 0) {
    fileInput.value = target.files[0];
    console.log("File selected:", fileInput.value.name);
  } else {
    fileInput.value = null;
    console.log("No file selected.");
  }
};

const submitForm = async () => {
  try {
    const formData = new FormData();
    formData.append("name", form.name);
    formData.append("colour", form.colour);
    formData.append("part_number", form.part_number);
    formData.append("size_mm", form.size_mm.toString());
    if (form.description) {
      formData.append("description", form.description);
    }
    if (fileInput.value) {
      formData.append("image", fileInput.value);
      console.log("File appended to FormData:", fileInput.value.name);
    }
    console.log("Submitting form with data:", form);
    if (isEdit && productId) {
      await updateProduct(productId, formData);
    } else {
      await createProduct(formData);
    }
    router.push('/');
  } catch (error) {
    console.error("Error submitting form:", error);
  }
};
</script>

<style scoped>
form {
  max-width: 700px; 
  margin: 0 auto; 
  padding: var(--spacing-lg);
  background-color: var(--content-bg-color);
  border-radius: var(--border-radius-lg);
}

label {
  margin-top: var(--spacing-md); 
}

label:first-of-type {
  margin-top: 0;
}

button[type="submit"] {
  margin-top: var(--spacing-lg); 
  width: auto;
  padding-left: var(--spacing-lg);
  padding-right: var(--spacing-lg);
}
</style>
