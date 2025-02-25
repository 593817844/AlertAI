import { createApp } from 'vue';  // 使用 createApp 来创建应用实例
import App from './App.vue';
import router from './router';
import ElementPlus from 'element-plus';  // 引入 ElementPlus 插件
import 'element-plus/dist/index.css';  // 引入 ElementPlus 样式

// 创建应用实例
const app = createApp(App);

// 注册插件
app.use(router);  // 使用路由
app.use(ElementPlus);  // 使用 ElementPlus

app.config.productionTip = false;  // 配置 Vue 应用的提示

// 挂载应用
app.mount('#app');
