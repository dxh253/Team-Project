/*const path = require('path')

module.exports = {
  outputDir: path.resolve(__dirname, '../mySite/mysite/templates'),
  transpileDependencies: true
}*/

const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
// devServer: {
//     proxy: {
//       '/api': {
//         target: 'http://127.0.0.1:8000',
//         changeOrigin: true
//       }
//     }
//   }
})