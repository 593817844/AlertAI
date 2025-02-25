<template>
  <el-container style="height: 100vh;">
    <!-- 左侧菜单栏 (固定) -->
    <el-aside
      width="200px"
      style="background-color: #304156; position: fixed; top: 0; bottom: 0; left: 0;"
    >
      <!-- 系统名称 -->
      <div style="height: 60px; line-height: 60px; text-align: center; color: #fff; font-size: 18px; background-color: #263445;">
        AlertAI
      </div>

      <!-- 菜单栏 -->
      <el-menu
        background-color="#304156"
        text-color="#fff"
        active-text-color="#ffd04b"
        router
        :default-active="$route.path" 
      >
        <el-menu-item index="/home/alarm-list">
          <i class="el-icon-warning"></i>
          <span>告警列表</span>
        </el-menu-item>
        <el-menu-item index="/home/alarm-analysis">
          <i class="el-icon-data-analysis"></i>
          <span>告警分析</span>
        </el-menu-item>
      </el-menu>
    </el-aside>

    <el-container style="margin-left: 200px;">
      <!-- 顶部区域 (固定) -->
      <el-header
        style="background-color: #409EFF; color: #fff; position: fixed; top: 0; right: 0; left: 200px; z-index: 1000; display: flex; align-items: center; justify-content: flex-end; padding: 0 20px;"
      >
        <span style="margin-right: 20px;">欢迎, {{ username }}</span>
        <el-button type="text" @click="logout" style="color: #fff; text-decoration: none;">退出</el-button>
      </el-header>

      <!-- 右侧内容区域 (动态区域) -->
      <el-main style="margin-top: 60px; padding: 20px; overflow-y: auto;">
        <!-- 默认欢迎界面 -->
        <div v-if="$route.path === '/home'" class="welcome-container">
          <h1>欢迎使用 AlertAI 系统</h1>
          <p>请从左侧菜单栏选择功能</p>
        </div>
        <!-- 子路由内容 -->
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      username: localStorage.getItem('username') || '用户'
    };
  },
  methods: {
    logout() {
      localStorage.removeItem('isAuthenticated');
      localStorage.removeItem('username');
      localStorage.removeItem('token');
      this.$router.push('/login');
    }
  }
};
</script>

<style scoped>
/* 美化滚动条 */
.el-main::-webkit-scrollbar {
  width: 8px;
}
.el-main::-webkit-scrollbar-thumb {
  background-color: #c1c1c1;
  border-radius: 4px;
}
.el-main::-webkit-scrollbar-track {
  background-color: #f1f1f1;
}

/* 菜单栏美化 */
.el-menu {
  border-right: none;
}
.el-menu-item {
  font-size: 14px;
}
.el-menu-item:hover {
  background-color: #263445 !important;
}
.el-menu-item.is-active {
  background-color: #1f2d3d !important;
}

/* 顶部区域美化 */
.el-header {
  box-shadow: 0 2px 4px rgba(10, 10, 121, 0.1);
}

/* 欢迎界面样式 */
.welcome-container {
  text-align: center;
  margin-top: 100px;
}
.welcome-container h1 {
  font-size: 32px;
  color: #0d406a;
}
.welcome-container p {
  font-size: 16px;
  color: #666;
}
.el-button--text:hover {
  text-decoration: underline; /* 悬停时显示下划线 */
  opacity: 0.8; /* 悬停时稍微透明 */
}

</style>