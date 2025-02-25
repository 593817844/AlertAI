import axios from 'axios';
import router from '../router';
import { API_BASE_URL } from './config';

// 创建 axios 实例
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});


// 请求拦截器
apiClient.interceptors.request.use(config => {
  const token = localStorage.getItem('token'); // 从localStorage获取token
  const isLoginPage = config.url.includes('/login'); // 检查是否是登录接口请求

  if (token && !isLoginPage) { // 如果存在token并且不是登录请求，则添加到header
    config.headers['Authorization'] = `Bearer ${token}`;
  }

  return config;
}, error => {
  return Promise.reject(error);
});

apiClient.interceptors.response.use(response => {
  // 如果响应体中的code是401，手动抛出错误以便进入错误处理逻辑
  if (response.data && response.data.code === 401) {
    // 清除认证状态
    localStorage.removeItem('token');
    localStorage.removeItem('isAuthenticated');
    // 可选：如果使用Vuex，这里也可以dispatch一个action来更新state
    // store.dispatch('auth/logout');

    // 检查请求URL是否为登录页面
    if (!response.config.url.includes('/login')) {
      router.push('/login');
    }
    return Promise.reject({response: response});
  }
  return response;
}, () => {});


// 登录接口
export const login = (username, password) => {
  return apiClient.post('/user/login', { username, password });
};

// 获取告警列表
export const getAlarms = (page = 1, pageSize = 10) => {
  return apiClient.get('/alert', {
    params: { page, pageSize },
  });
};

// 获取告警分析结果
export const getAnalysis = (projectName) => {
  return apiClient.post(`/ai/${projectName}`);
};

// 获取系统信息
export const getSystemname = () => {
  return apiClient.get(`/system/getname`);
};




export default apiClient;