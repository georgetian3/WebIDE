import Vue from 'vue'
import Router from 'vue-router'
import welcomePage from '@/components/welcomePage'
import codePage from '@/components/codePage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'welcomePage',
      component: welcomePage
    },
    {
      path: '/coding',
      name: 'codePage',
      component: codePage
    }
  ]
})
