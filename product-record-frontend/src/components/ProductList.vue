<template>
  <div>
    <filter-bar 
      @update:search="searchQuery = $event"
      @update:sort="sortOption = $event"
      @update:available="showAvailableOnly = $event"
    />
    <div class="product-grid">
      <div 
        v-for="product in filteredProducts" 
        :key="product.id" 
        class="product-card"
        @click="goToDetail(product.id)"
      >
      <!-- the stock is just a makeshift tag -->
        <div class="badge" v-if="product.available">In Stock</div> 
        <img :src="product.image_url || defaultImage" alt="Product Image" />
        <h3>{{ product.name }}</h3>
        <p><strong>Colour:</strong> {{ product.colour }}</p>
        <p><strong>Size (mm):</strong> {{ product.size_mm }}</p>
        <router-link :to="`/product/${product.id}`">View Details</router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { fetchProducts } from '../services/productService';
import FilterBar from './FilterBar.vue';

interface Product {
  id: number;
  name: string;
  colour: string;
  part_number: string;
  size_mm: number;
  image_url?: string;
  available?: boolean;
}

const products = ref<Product[]>([]);
const searchQuery = ref('');
const sortOption = ref('name');
const showAvailableOnly = ref(false);
const defaultImage = 'https://via.placeholder.com/150';
const router = useRouter();

onMounted(async () => {
  try {
    const response = await fetchProducts();
    products.value = response.data.map(product => ({
      ...product,
      available: true  // Mark as available, for now.
    }));
  } catch (error) {
    console.error('Error fetching products:', error);
  }
});

const filteredProducts = computed(() => {
  let filtered = [...products.value];

  if (searchQuery.value) {
    filtered = filtered.filter(product =>
      product.name.toLowerCase().includes(searchQuery.value.toLowerCase())
    );
  }

  if (showAvailableOnly.value) {
    filtered = filtered.filter(product => product.available);
  }

  if (sortOption.value === 'name') {
    filtered.sort((a, b) => a.name.localeCompare(b.name));
  } else if (sortOption.value === 'size_mm') {
    filtered.sort((a, b) => a.size_mm - b.size_mm);
  } else if (sortOption.value === 'colour') {
    filtered.sort((a, b) => a.colour.localeCompare(b.colour));
  }

  return filtered;
});

const goToDetail = (id: number) => {
  router.push(`/product/${id}`);
};
</script>

<style scoped>
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: var(--spacing-lg); 
  margin-top: var(--spacing-lg); 
}

.product-card {
  position: relative;
  background-color: var(--card-bg-color);
  padding: var(--spacing-md);
  border-radius: var(--border-radius-lg);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
  text-align: center;
  transition: transform 0.2s, box-shadow 0.2s;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  border: 1px solid var(--border-color);
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}

.product-card img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  border-radius: var(--border-radius-md);
  margin-bottom: var(--spacing-md);
}

.product-card h3 {
  color: var(--secondary-color); 
  margin-top: 0;
  margin-bottom: var(--spacing-sm);
  font-size: 1.15em;
  flex-grow: 1;
}

.product-card p {
  margin: var(--spacing-xs) 0;
  font-size: 0.9em;
  color: #5c6166; 
}
.product-card p strong {
    
    color: var(--secondary-color);
}


.product-card a {
  display: inline-block;
  margin-top: var(--spacing-md);
  padding: var(--spacing-sm) var(--spacing-md);
  color: var(--secondary-color);
  text-decoration: none;
  font-weight: var(--font-weight-bold);
  border: 1px solid var(--secondary-color);
  border-radius: var(--border-radius-md);
  transition: background-color 0.2s, border-color 0.2s, color 0.2s;
}

.product-card a:hover {
  background-color: var(--accent-color-hover);
  border-color: var(--accent-color-hover);
  color: #ffffff;
}
.btn-primary {
  background-color: var(--secondary-color);
  color: #ffffff;
  border-color: var(--secondary-color);
}
.btn-primary:hover {
  background-color: var(--accent-color-hover);
  border-color: var(--accent-color-hover);
}
.badge {
  position: absolute;
  top: var(--spacing-sm); 
  right: var(--spacing-sm); 
  background-color: var(--secondary-color); 
  color: white;
  padding: var(--spacing-xs) var(--spacing-sm);
  border-radius: var(--border-radius-sm);
  font-size: 0.8rem;
  font-weight: var(--font-weight-bold);
}
</style>