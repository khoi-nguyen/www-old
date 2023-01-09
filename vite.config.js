import { resolve } from 'path'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  build: {
    lib: {
      entry: resolve(__dirname, 'src/main.ts'),
      fileName: 'main',
      formats: ['cjs', 'es'],
    },
    outDir: 'build/',
  },
  plugins: [vue()]
})
