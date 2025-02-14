// src/services/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  }
});

export const generateAIResponse = async (prompt) => {
  try {
    console.log('Sending prompt:', { prompt });
    const response = await api.post('/api/generate', { prompt: prompt });
    console.log('Response:', response.data);
    return response.data.content; // Wrap edilmiş response'dan content'i al
  } catch (error) {
    console.error('API Error:', error.response?.data || error);
    throw new Error(error.response?.data?.error || 'Bir hata oluştu');
  }
};
