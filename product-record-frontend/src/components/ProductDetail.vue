<template>
  <div class="product-detail-layout">
    <button class="back-btn" @click="goBack">← Back</button>

    <div class="product-detail-tile">

      <div class="product-header">
        <img :src="product.image_url || defaultImage" alt="Product Image" />
        <div class="info">
          <h2>{{ product.name }}</h2>
          <p><strong>Colour:</strong> {{ product.colour }}</p>
          <p><strong>Part Number:</strong> {{ product.part_number }}</p>
          <p><strong>Size (mm):</strong> {{ product.size_mm }}</p>
        </div>
      </div>

      <button class="toggle-btn" @click="showDescription = !showDescription">
        {{ showDescription ? '- Hide Description' : '+ Show Description' }}
      </button>

      <div v-if="showDescription" class="description">
        <p>{{ product.description || 'No description available.' }}</p>
      </div>

      <div class="actions">
        <router-link class="btn btn-primary" :to="`/product/${product.id}/edit`">Edit</router-link>
        <button class="btn btn-danger" @click="deleteProductHandler(product.id)">Delete</button>
      </div>

    </div> </div> 
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { fetchProduct, deleteProduct } from '../services/productService';

interface Product {
  id: number;
  name: string;
  colour: string;
  part_number: string;
  size_mm: number;
  description?: string;
  image_url?: string;
}

const route = useRoute();
const router = useRouter();
const product = ref<Product>({
  id: 0,
  name: '',
  colour: '',
  part_number: '',
  size_mm: 0,
  description: '',
  image_url: '',
});
const showDescription = ref(false);
const defaultImage = 'https://via.placeholder.com/150';

onMounted(async () => {
  const id = route.params.id;
  if (id) {
    try {
      const response = await fetchProduct(id);
      product.value = response.data;
    } catch (error) {
      console.error('Error fetching product:', error);
    }
  }
});

const goBack = () => router.back();

const deleteProductHandler = async (id: number) => {
  try {
    await deleteProduct(id);
    router.push('/');
  } catch (error) {
    console.error('Error deleting product:', error);
  }
};
</script>

<style scoped>
.product-detail {
  padding: var(--spacing-lg);
  background-color: var(--content-bg-color);
  border-radius: var(--border-radius-lg);
  max-width: 900px;
  margin: var(--spacing-lg) auto;
  text-align: left; 
}

.product-detail-layout {
  display: flex; 
  align-items: flex-start; 
  gap: var(--spacing-lg); 
  max-width: 1100px; 
  margin: var(--spacing-lg) auto; 
}
.product-detail-tile {
  background-color: var(--card-bg-color); 
  padding: var(--spacing-lg);           
  border-radius: var(--border-radius-lg); 
  border: 1px solid #e0d8c3;          
  box-shadow: 0 4px 8px rgba(0,0,0,0.08); 
  flex-grow: 1; 
  text-align: left; 
}
.back-btn {
  background: none;
  border: none;
  font-size: 1rem;
  color: var(--secondary-color);
  cursor: pointer;
  padding: var(--spacing-xs) 0; 
  font-weight: var(--font-weight-bold);
  white-space: nowrap; 
  margin-top: var(--spacing-sm); 
  flex-shrink: 0; 
}
.back-btn:hover {
    color: var(--accent-color);
}

.product-header {
  display: flex;
  gap: var(--spacing-lg);
  align-items: flex-start;
  flex-wrap: wrap;
  margin-bottom: var(--spacing-lg);
}

.product-header img {
  width: 200px;
  height: 200px;
  object-fit: cover;
  border-radius: var(--border-radius-md);
  flex-shrink: 0;
}

.info {
    flex-grow: 1;
}

.info h2 {
  margin-top: 0;
  margin-bottom: var(--spacing-md);
  font-size: 1.8em;
  color: var(--secondary-color); 
}

.info p {
  margin: var(--spacing-sm) 0;
  color: #5c6166; 
  line-height: 1.7;
}

.info p strong {
    color: var(--secondary-color); 
    font-weight: var(--font-weight-bold);
    margin-right: var(--spacing-xs);
}

.toggle-btn {
  background-color: rgba(255, 255, 255, 0.4); 
  border: 1px solid var(--button-default-border); 
  color: var(--button-default-text); 
  margin-bottom: var(--spacing-md);
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--border-radius-md); 
  cursor: pointer;
  transition: background-color 0.2s ease, border-color 0.2s ease;
}
.toggle-btn:hover {
  background-color: rgba(255, 255, 255, 0.6); 
  border-color: var(--button-default-border-hover);
}

.description {
  background-color: rgba(255, 255, 255, 0.2); 
  padding: var(--spacing-md);
  border-radius: var(--border-radius-md); 
  margin-bottom: var(--spacing-lg);
  line-height: 1.7;
  color: #5c6166; 
}
.description p {
    margin: 0; 
}

.actions {
  margin-top: var(--spacing-lg);
  display: flex;
  gap: var(--spacing-md);
  flex-wrap: wrap;
}

    
.back-btn {
  background: none;
  border: none;
  font-size: 1rem;
  color: var(--secondary-color);
  cursor: pointer;
  position: left;
  margin-left: 0px;
  margin-bottom: var(--spacing-lg); 
  padding: 0; 
  font-weight: var(--font-weight-bold);
}
.back-btn:hover {
    color: var(--accent-color);
}

.product-header {
  display: flex;
  gap: var(--spacing-lg); 
  align-items: flex-start; 
  flex-wrap: wrap;
  margin-bottom: var(--spacing-lg);
}

.product-header img {
  width: 200px; 
  height: 200px;
  object-fit: cover;
  border-radius: var(--border-radius-md); 
  border: 1px solid var(--border-color); 
  flex-shrink: 0; 
}

.info {
    flex-grow: 1; 
}

.info h2 {
  margin-top: 0;
  margin-bottom: var(--spacing-md);
  font-size: 1.8em;
  color: var(--secondary-color); 
}

.info p {
  margin: var(--spacing-sm) 0;
  color: var(--text-color); 
  line-height: 1.7;
}

.info p strong {
    color: var(--text-color); 
    font-weight: var(--font-weight-bold); 
    margin-right: var(--spacing-xs);
}

.toggle-btn {
  background-color: var(--button-default-bg);
  border-color: var(--button-default-border);
  color: var(--button-default-text);
  margin-bottom: var(--spacing-md);
  padding: var(--spacing-sm) var(--spacing-md);
}
.toggle-btn:hover {
  background-color: var(--button-default-bg-hover);
  border-color: var(--button-default-border-hover);
}


.description {
  background-color: var(--light-gray);
  padding: var(--spacing-lg); 
  border-radius: var(--border-radius-md);
  margin-bottom: var(--spacing-lg);
  border: 1px solid var(--border-color);
  line-height: 1.7; 
}

.actions {
  margin-top: var(--spacing-lg);
  display: flex;
  gap: var(--spacing-md); 
  flex-wrap: wrap; 
}

.actions .btn {
}
</style>