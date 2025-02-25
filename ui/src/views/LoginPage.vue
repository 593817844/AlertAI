<template>
  <div class="login-container">
    <!-- 系统名称 -->
    <div class="system-name">
      AlertAI
    </div>

    <!-- 登录表单 -->
    <el-form :model="loginForm" :rules="rules" ref="loginForm" class="login-form">
      <el-form-item prop="username">
        <el-input
          v-model="loginForm.username"
          placeholder="用户名"
          prefix-icon="el-icon-user"
        ></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input
          type="password"
          v-model="loginForm.password"
          placeholder="密码"
          prefix-icon="el-icon-lock"
        ></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('loginForm')" class="login-button">登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { login } from '@/api/api';

export default {
  data() {
    return {
      loginForm: {
        username: '',
        password: ''
      },
      rules: {
        username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
        password: [{ required: true, message: '请输入密码', trigger: 'blur' }]
      }
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          login(this.loginForm.username, this.loginForm.password)
            .then(response => {
              if (response.data.code == 200) {
                localStorage.setItem('isAuthenticated', 'true');
                localStorage.setItem('username', this.loginForm.username);
                localStorage.setItem('token', response.data.token); // 假设后端返回 token
                this.$router.push('/home');
              } else {
                this.$message.error('登录失败：' + response.data.message);
              }
            })
            .catch(error => {
              this.$message.error('登录失败：' + error.message);
            });
        } else {
          console.log('表单验证失败');
          return false;
        }
      });
    }
  }
};
</script>

<style scoped>
html, body {
  height: 100%;
  margin: 0;
  overflow: hidden;
  background-color: #f7f9fc; /* 更柔和、更现代的背景色 */
}

.login-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  padding: 0 20px; /* 添加内边距以便在小屏幕上也能有良好的显示效果 */
  box-sizing: border-box;
  overflow: hidden; /* 确保容器内的内容不会导致滚动 */
}

.system-name {
  font-size: 48px;
  font-weight: 300;
  color: #333;
  margin-bottom: 60px;
}

.login-form {
  width: 100%;
  max-width: 400px;
  padding: 40px;
  background: #fff;
  border-radius: 15px;
  box-shadow: 0 15px 35px rgba(50, 50, 93, 0.1), 0 5px 15px rgba(0, 0, 0, 0.07);
  transition: all 0.3s ease;
}

.login-form >>> .el-input__inner {
  background: #f9f9f9;
  border: none; /* 移除边框避免重复 */
  border-radius: 5px;
  color: #333;
  font-size: 16px;
  padding: 12px 15px;
  width: 100%; /* 确保宽度占据整个父元素 */
  box-sizing: border-box; /* 调整盒子模型计算方式 */
}

.login-form >>> .el-input__inner::placeholder {
  color: #aaa;
}

.login-button {
  width: 100%;
  background: #1890ff;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  color: #fff;
  margin-top: 20px;
  padding: 12px;
  transition: all 0.3s ease;
}

.login-button:hover {
  background: #40a9ff;
}
</style>