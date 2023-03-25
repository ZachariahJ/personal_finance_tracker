import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: "0.0.0.0",
    proxy: {
      "/api": {
        target: "http://153.106.86.201:5000/api/v1.0/",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ""),
      
      }
    }
  },
  resolve: {
    alias: {
      "@": "./src",
    },
  },
});
