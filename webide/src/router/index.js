import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import welcomePage from '@/components/welcomePage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'welcomePage',
      component: welcomePage
    }
  ]
})
