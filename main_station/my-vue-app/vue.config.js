const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/search': {
        target: 'https://local.so.v.ifeng.com',
        changeOrigin: true,
        pathRewrite: { '^/search': '' }
      }
    }
  }
})
