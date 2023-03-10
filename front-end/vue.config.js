const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  server: {
    proxy: {
      '/api': 'http://localhost:8000'
    }
  },
  transpileDependencies: true
})

//const path = require('path')

//module.exports = {
//  outputDir: path.resolve(__dirname, '../mySite/mysite/templates'),
//  transpileDependencies: true
//}
