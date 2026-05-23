import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Homepage/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path:'/login',
      name:'login',
      component:()=>import('../views/Login/index.vue')
    },
    {
      path:'/register',
      name:'resgister',
      component:()=>import('../views/Register/index.vue')
    },
    {
      path:'/pay',
      name:'pay',
      component:()=>import('../views/Pay/index.vue')
    },
    {
      path:'/goods',
      name:'goods',
      component:()=>import('../views/Goods/index.vue')
    },
    {
      path:'/my',
      name:'my',
      component:()=>import('../views/UserInfo/index.vue')
    }
  ],
})

export default router


router.beforeEach((to, from, next) => {
  // 检查用户是否访问了需要登录的页面
  if (to.path === '/my' || to.path === '/pay') {
    // 如果没有 token，跳转到登录页面
    if (!sessionStorage.getItem('token')) {
      next('/login');  // 没有登录，重定向到登录页
    } else {
      next();  // 已登录，允许访问目标页面
    }
  } else {
    next();  // 对于其他页面，直接放行
  }
});


