import { createRouter, createWebHistory } from 'vue-router';
import ProductList from '../components/ProductList.vue';
import ProductForm from '../components/ProductForm.vue';
import ProductDetail from '../components/ProductDetail.vue';

const routes = [
  { path: '/', name: 'Home', component: ProductList },
  { path: '/product/new', name: 'CreateProduct', component: ProductForm },
  { path: '/product/:id', name: 'ProductDetail', component: ProductDetail, props: true },
  { path: '/product/:id/edit', name: 'EditProduct', component: ProductForm, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
