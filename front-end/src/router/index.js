import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import PC from "@/views/PC";
import Mobile from "@/views/Mobile";
import Home from "@/views/Home";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/pc',
      name: 'PC',
      component: PC
    },
    {
      path: '/app',
      name: 'Mobile',
      component: Mobile,
    },
    {
      path: '/',
      name: 'Home',
      component: Home,
    }
  ]
})
