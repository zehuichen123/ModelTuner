import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from "@/views/Home";
import Mobile from "@/views/Mobile";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/pc',
      name: 'Home',
      component: Home
    },
    {
      path: '/app',
      name: 'Mobile',
      component: Mobile,
    }
  ]
})
