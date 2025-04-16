<template>
  <div id="app">
    <header>
      <h1 style="font-family: 'Inconsolata', monospace;">Product Record System</h1>
      <nav>
        <router-link to="/">Home</router-link>
        <router-link to="/product/new">Add Product</router-link>
      </nav>
    </header>
    <main>
      <router-view />
    </main>
  </div>
</template>

<script setup lang="ts">
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Inconsolata:wght@200..900&display=swap');

:root {
  --primary-color: #EAE0C8;    
  --secondary-color: #536878; 
  --accent-color: #536878;    
  --accent-color-hover: #536878; 
  --danger-color: #dc3545;     
  --danger-color-hover: #c82333;


  --app-bg-color: #ffffff;       
  --content-bg-color: #ffffff;    
  --card-bg-color: var(--primary-color); 
  --header-bg-color: var(--secondary-color); 
  --filter-bg-color: #F1EFEC;      

  --text-color: #212529;       
  --text-color-light: #f8f9fa; 
  --text-color-muted: #6c757d;  
  --border-color: #dee2e6;    
  --light-gray: #f1f3f5;       

  --button-default-bg: #F1EFEC;     
  --button-default-border: #D4C9BE;  
  --button-default-text: var(--secondary-color); 
  --button-default-bg-hover: #e8e5e2; 
  --button-default-border-hover: #c7bdaf; 

  --spacing-xs: 0.25rem; 
  --spacing-sm: 0.5rem;  
  --spacing-md: 1rem;    
  --spacing-lg: 1.5rem;  
  --spacing-xl: 2rem;    

  --border-radius-sm: 6px;
  --border-radius-md: 10px;
  --border-radius-lg: 15px;

  --font-family-sans: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;

  --font-weight-normal: 200;
  --font-weight-bold: 400;
}
h1{
  --font-family-sans: 'Inconsolata', monospace;
  --font-weight-normal: 200;
  --font-weight-bold: 200;

}

*, *::before, *::after {
  box-sizing: border-box;
}

body {
  font-family: var(--font-family-sans);
  background-color: var(--app-bg-color); 
  color: var(--text-color);
  margin: 0;
  min-height: 100vh;
  line-height: 1.6;
  font-weight: var(--font-weight-normal);
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

header {
  background-color: var(--header-bg-color);
  padding: var(--spacing-md) var(--spacing-xl);
  text-align: center;
  color: var(--text-color-light);
}

header h1 {
  margin: 0 0 var(--spacing-sm) 0;
  margin-bottom: 20px;
  font-size: 2em;
  
}

nav {
  margin-top: var(--spacing-sm);
}

nav a {
  color: var(--text-color-light); 
  opacity: 0.85; 
  text-decoration: none;
  margin: 0 var(--spacing-sm);
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--border-radius-md);
  font-weight: var(--font-weight-bold);
  transition: background-color 0.2s ease, color 0.2s ease, opacity 0.2s ease;
}

nav a:hover,
nav a.router-link-exact-active {
  background-color: rgba(255, 255, 255, 0.1);
  color: white; 
  opacity: 1.0; 
}

main {
  flex-grow: 1;
  padding: var(--spacing-xl);
  background-color: var(--content-bg-color);
  width: 100%;
}
button, .btn {
  display: inline-block;
  border-radius: var(--border-radius-md);
  border: 1px solid transparent;
  padding: 0.6em 1.2em;
  font-size: 1em;
  font-weight: var(--font-weight-bold);
  font-family: inherit;
  cursor: pointer;
  transition: background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease;
  text-align: center;
  text-decoration: none;
}

button:not(.btn-primary):not(.btn-danger):not(.back-btn):not(.toggle-btn), 
.btn-default {
  background-color: var(--button-default-bg); 
  border-color: var(--button-default-border); 
  color: var(--button-default-text); 
}
button:not(.btn-primary):not(.btn-danger):not(.back-btn):not(.toggle-btn):hover,
.btn-default:hover {
  background-color: var(--button-default-bg-hover); 
  border-color: var(--button-default-border-hover); 
}

.btn-primary {
  background-color: var(--secondary-color);
  color: white;
  border-color: var(--secondary-color);
}
.btn-primary:hover {
  background-color: #435460; 
  border-color: #3c4b56;
}

.btn-danger {
    background-color: var(--danger-color);
    color: white;
    border-color: var(--danger-color);
}
.btn-danger:hover {
    background-color: var(--danger-color-hover);
    border-color: #bd2130;
}

input[type="text"],
input[type="number"],
input[type="file"],
textarea,
select {
  width: 100%;
  padding: var(--spacing-sm) var(--spacing-md);
  font-size: 1rem;
  font-family: inherit;
  margin-bottom: var(--spacing-sm);
  border: 1px solid var(--border-color); 
  border-radius: var(--border-radius-md); 
  background-color: #ffffff !important; 
  color: var(--text-color) !important;
}

input:focus, textarea:focus, select:focus {
    outline: none;
    border-color: var(--accent-color);
    box-shadow: 0 0 0 2px rgba(100, 108, 255, 0.25); /* Adjust color to match accent */
}


input[type="file"] {
  padding: var(--spacing-xs);
}

textarea {
  min-height: 100px;
  resize: vertical;
}

label {
  display: block;
  margin-bottom: var(--spacing-xs);
  font-weight: var(--font-weight-bold);
}

.filter-bar label {
  display: flex;
  align-items: center;
  gap: var(--spacing-xs);
  margin-bottom: 0;
  font-weight: var(--font-weight-normal);
  color: var(--text-color); 
}
.filter-bar input[type="checkbox"] {
  width: auto;
  margin-bottom: 0;
}
.filter-bar input[type="text"],
.filter-bar select {
   border-color: var(--button-default-border); 
   margin-bottom: 0; 
}
input::placeholder,
textarea::placeholder {
  color: var(--text-color-muted);
  opacity: 0.8;
}
</style>