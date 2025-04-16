<template>
    <div class="filter-bar">

      <input
        class="search-input"
        v-model="localSearch"
        placeholder="Search Products"
        @input="updateSearch"
        type="text"
      />
  
      <select v-model="localSort" @change="updateSort">
        <option value="name">Sort by Name</option>
        <option value="size_mm">Sort by Size</option>
        <option value="colour">Sort by Colour</option>
      </select>
  
      <label>
        <input
          type="checkbox"
          v-model="localAvailable"
          @change="updateAvailable"
        />
        Show only available products
      </label>
    </div>
  </template>
  
  
  <script setup lang="ts">
  import { ref, watch } from 'vue';
  import { defineEmits } from 'vue';
  
  const emit = defineEmits(['update:search', 'update:sort', 'update:available']);
  const localSearch = ref('');
  const localSort = ref('name');
  const localAvailable = ref(false);
  
  const updateSearch = () => {
    emit('update:search', localSearch.value);
  };
  const updateSort = () => {
    emit('update:sort', localSort.value);
  };
  const updateAvailable = () => {
    emit('update:available', localAvailable.value);
  };
  </script>
  
  <style scoped>
.filter-bar {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
  margin-bottom: var(--spacing-lg);
  background-color: var(--filter-bg-color); 
  padding: var(--spacing-md) var(--spacing-lg);
  border-radius: var(--border-radius-md);
  border: 1px solid var(--border-color);

  flex-wrap: nowrap;

  @media (max-width: 768px) {
    flex-wrap: wrap; 
  }
}
.search-input {
  flex: 2; 
  min-width: 250px; 
  background-color: #ffffff;
  border: 1px solid var(--border-color);
  border-radius: 20px; 
  padding: var(--spacing-sm);
}  


  .filter-bar select {
  flex: 1; 
  min-width: 150px; 
  margin-bottom: 0;
  background-color: #ffffff;
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius-lg);
  padding: var(--spacing-sm);
}


  .back-btn {
    background-color: var(--secondary-color);
    color: var(--text-color-light);
    border: none;
    padding: var(--spacing-sm) var(--spacing-md);
    border-radius: var(--border-radius-md);
    cursor: pointer;
    font-weight: var(--font-weight-bold);
    margin-right: var(--spacing-md);
  }
  .filter-bar input[type="checkbox"] {
  width: auto;
  margin-bottom: 0;
}


  .back-btn:hover {
  background-color: var(--accent-color-hover);
  }
  .filter-bar label {
  display: flex;
  align-items: center;
  gap: var(--spacing-xs);
  margin-bottom: 0;
  font-weight: var(--font-weight-normal);
  color: var(--text-color);
}
  </style>