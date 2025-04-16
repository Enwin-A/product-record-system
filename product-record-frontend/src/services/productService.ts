import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/products/';

export const createProduct = (formData: FormData) => axios.post(API_URL, formData);
export const updateProduct = (id: string | number, formData: FormData) => axios.put(`${API_URL}${id}/`, formData);
export const fetchProduct = (id: string | number) => axios.get(`${API_URL}${id}/`);
export const fetchProducts = () => axios.get(API_URL);
export const deleteProduct = (id: string | number) => axios.delete(`${API_URL}${id}/`);
