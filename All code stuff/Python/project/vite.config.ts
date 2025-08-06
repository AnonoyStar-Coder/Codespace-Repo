import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  optimizeDeps: {
    exclude: ['lucide-react'],
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
      },
      '/preview': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
      },
      '/builder': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
      },
      '/export': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
      }
    }
  }
});