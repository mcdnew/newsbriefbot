import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  root: '.',             // <-- confirms index.html is in frontend/
  build: {
    outDir: 'dist',
  },
})

