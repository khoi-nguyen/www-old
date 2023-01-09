import { resolve } from 'path'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  build: {
    rollupOptions: {
      input: resolve(__dirname, 'src/main.ts'),
      output: {
        entryFileNames: "[name].js",
        assetFileNames: "[name].[ext]",
      }
    },
    emptyOutDir: false,
    outDir: 'build/',
  },
  plugins: [vue()]
})
