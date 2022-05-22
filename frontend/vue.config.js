// const { defineConfig } = require('@vue/cli-service')

// module.exports = defineConfig({
//     transpileDependencies: true,
//     css: {
//         loaderOptions: {
//             css: {
//                 modules: ['style-loader', 'css-loader']
//             }
//         }
//     }
// })


// const { defineConfig } = require('@vue/cli-service')

// module.exports = defineConfig({
//     transpileDependencies: true,
//     chainWebpack: config => {
//         config.module
//           .rule('css')
//           .use('style-loader')
//             .tap(options => {
//               // modify the options...
//               return options
//             })
//       }
// })

// const { defineConfig } = require('@vue/cli-service')
// const { VueLoaderPlugin } = require('vue-loader')

// module.exports = defineConfig({
//     transpileDependencies: true,
//     chainWebpack: config => {
//         const cssRule = config.module.rule('css').oneOf('vue')

//         cssRule.uses.clear()
    
//         cssRule
//         .test(/\.css$/)
//           .use('style-loader')
//             .loader('style-loader')
//             .end()
//             .use('css-loader')
//               .loader('css-loader')
//               .end()
        
//         // new VueLoaderPlugin()
//         config.module.rule('css').oneOf('vue-modules').use('vue-style-loader').tap(options => {
//             shadowMode: true
//             return options
//           })
//       },

// })

const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})