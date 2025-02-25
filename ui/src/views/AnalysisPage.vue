<template>
  <div class="alarm-analysis">
    <!-- 错误信息展示 -->
    <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>

    <!-- 项目选择器 -->
    <el-select v-if="projects && projects.length" v-model="selectedProject" placeholder="请选择项目" :disabled="isLoading || analysisButtonDisabled">
      <el-option
        v-for="(project, index) in projects"
        :key="index"
        :label="project"
        :value="project">
      </el-option>
    </el-select>
    <el-select v-else placeholder="无" :disabled="true">
      <el-option label="无" value="无"></el-option>
    </el-select>

    <!-- 分析中或显示结果 -->
    <div v-if="isLoading">分析中...</div>
    <el-input
      v-else
      type="textarea"
      :rows="10"
      placeholder="分析结果"
      v-model="analysisResult"
      :disabled="true">
    </el-input>

    <!-- 分析按钮 -->
    <el-button type="primary" @click="fetchAnalysis" :disabled="analysisButtonDisabled || isLoading">{{ isLoading ? '分析中...' : '分析' }}</el-button>
  </div>
</template>

<script>
import { getSystemname, getAnalysis } from '../api/api'; // 假设API函数在这里

export default {
  data() {
    return {
      selectedProject: '',
      projects: [],
      analysisResult: '',
      isLoading: false,
      errorMessage: '', // 新增字段用于显示错误消息
      analysisButtonDisabled: false, // 控制分析按钮是否禁用
    };
  },
  watch: {
    selectedProject(newVal) {
      this.analysisButtonDisabled = !newVal;
    }
  },
  created() {
    this.loadSystems();
  },
  methods: {
    loadSystems() {
      getSystemname().then(response => {
        if (response.data.code == 200) {
          this.projects = response.data.projects;
          console.log("Projects:", this.projects)// 打印确认数据
          console.log("Projects length:", this.projects.length)
          if (this.projects.length === 0) {
            
            console.log(this.projects.length)
            this.errorMessage = "没有可用的项目";
          } else {
            this.errorMessage = ''; // 清除错误信息，如果有项目的话
          }
        } else {
          console.error("获取系统信息失败:", response.err_msg);
          this.errorMessage = "获取系统信息失败";
        }
      }).catch(error => {
        console.error("请求系统信息失败", error);
        this.errorMessage = "请求系统信息时发生错误";
        this.projects = []; // 确保在出错时也给projects赋值以避免渲染错误
      });
    },
    fetchAnalysis() {
      this.isLoading = true;
      this.analysisResult = ''; // 清空之前的结果
      getAnalysis(this.selectedProject).then(response => {
        this.analysisResult = response.data; // 假设返回的数据直接作为分析结果
      }).catch(error => {
        console.error("获取分析结果失败", error);
        this.analysisResult = '获取分析结果时出错';
      }).finally(() => {
        this.isLoading = false;
      });
    }
  }
};
</script>

<style scoped>
.alarm-analysis {
  padding: 20px;
  max-width: 600px;
  margin: auto;
}

/* 错误信息样式 */
.error-message {
  color: red;
  margin-bottom: 15px;
}

/* 美化选择器 */
.el-select {
  width: 100%;
  margin-bottom: 15px;
}

/* 美化按钮 */
.el-button {
  width: 100%;
  margin-top: 15px;
}
</style>