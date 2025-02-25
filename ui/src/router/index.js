import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '../views/LoginPage.vue';
import AlarmPage from '../views/AlarmPage.vue';
import AnalysisPage from '../views/AnalysisPage.vue';
import HomePage from '../views/HomePage.vue';

// 使用 createRouter 来创建路由实例
// const router = createRouter({
//   history: createWebHistory(),  // 创建一个基于浏览器的历史记录模式
//   routes: [
//     {
//       path: '/',
//       redirect: '/login'
//     },
//     {
//       path: '/login',
//       component: LoginPage
//     },
//     {
//         path: '/home',
//         component: HomePage,
//         meta: { requiresAuth: true }
//     },
//     {
//       path: '/alarm-list',
//       component: AlarmPage,
//       meta: { requiresAuth: true }
//     },
//     {
//       path: '/alarm-analysis',
//       component: AnalysisPage,
//       meta: { requiresAuth: true }
//     }
//   ]
// });
const router = createRouter({
  history: createWebHistory(), 
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      component: LoginPage
    },
    {
      path: '/home',
      component: HomePage,
      meta: { requiresAuth: true },
      children: [
        {
          path: 'alarm-list', // 子路由路径
          component: AlarmPage
        },
        {
          path: 'alarm-analysis', // 子路由路径
          component: AnalysisPage
        }
      ]
    }
  ]
});

//守卫路由，实现不登陆无法访问其他界面
router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('isAuthenticated');

  if (to.path === '/login' && isAuthenticated) {
    // 如果已登录且访问登录页，跳转到首页
    next('/home');
  } else if (to.meta.requiresAuth && !isAuthenticated) {
    // 如果需要登录且未登录，跳转到登录页
    next('/login');
  } else {
    // 其他情况正常放行
    next();
  }
});

export default router;
