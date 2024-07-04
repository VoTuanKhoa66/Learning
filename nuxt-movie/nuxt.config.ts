// nuxt.config.ts
export default defineNuxtConfig({
  devtools: { enabled: false },
  modules: [
    '@vesp/nuxt-fontawesome',
    'nuxt-swiper',
  ],
  css: [
    'bootstrap/dist/css/bootstrap.min.css',
    '@fortawesome/fontawesome-svg-core/styles.css',
  ],
  fontawesome: {
    icons: {
      solid: ['cog', 'magnifying-glass', 'play', 'circle-info', 'plus','thumbs-up','chevron-down','star','xmark']
    }
  },
  app: {
    head: {
      link: [
        {
          rel: 'stylesheet',
          href: 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css'
        }
      ],
      script: [
        {
          src: 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js',
          tagPosition: 'bodyClose'
        }
      ]
    }
  },
})
