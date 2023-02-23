const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: []
})
module.exports = {
  pages: {
    index: {
      entry: 'src/main.js',
      template: 'public/index.html',
    },
  },
}