<template>
  <div class="alarm-list">
    <el-table :data="alarms" style="width: 100%">
      <el-table-column prop="id" label="ID" width="180"></el-table-column>
      <el-table-column label="告警信息">
        <template v-slot:default="{ row }">
          {{ row.annotations.summary }}
        </template>
      </el-table-column>
      <el-table-column label="实例">
        <template v-slot:default="{ row }">
          {{ row.labels.instance }}
        </template>
      </el-table-column>
      <el-table-column label="项目">
        <template v-slot:default="{ row }">
          {{ row.labels.project }}
        </template>
      </el-table-column>
      <el-table-column label="应用">
        <template v-slot:default="{ row }">
          {{ row.labels.app }}
        </template>
      </el-table-column>
      <el-table-column label="严重性">
        <template v-slot:default="{ row }">
          {{ row.labels.severity }}
        </template>
      </el-table-column>
      <el-table-column label="状态">
        <template v-slot:default="{ row }">
          {{ row.status === 'firing' ? '触发中' : '已解决' }}
        </template>
      </el-table-column>
      <el-table-column label="开始时间">
        <template v-slot:default="{ row }">
          {{ formatTime(row.startsAt) }}
        </template>
      </el-table-column>
      <el-table-column label="结束时间">
        <template v-slot:default="{ row }">
          {{ row.endsAt ? formatTime(row.endsAt) : '-' }}
        </template>
      </el-table-column>
      <el-table-column label="持续时间(分钟)">
        <template v-slot:default="{ row }">
          {{ row.duration ? (row.duration / 60).toFixed(2) : '-' }}
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      @current-change="handlePageChange"
      :current-page="currentPage"
      :page-size="pageSize"
      :total="total"
      layout="prev, pager, next">
    </el-pagination>
  </div>
</template>

<script>
import { getAlarms } from '@/api/api';
import dayjs from 'dayjs'; // 引入dayjs进行时间格式化

export default {
  data() {
    return {
      alarms: [],
      currentPage: 1,
      pageSize: 10,
      total: 0
    };
  },
  created() {
    this.fetchAlarms();
  },
  methods: {
    fetchAlarms() {
      getAlarms(this.currentPage, this.pageSize)
        .then(response => {
          if (response.data.code === 200) {
            const responseData = response.data;
            this.alarms = responseData.data; // 使用返回的data字段
            this.total = responseData.total; // 更新总条目数
          } else {
            this.$message.error('获取告警信息失败：' + response.data.err_msg);
          }
        })
        .catch(error => {
          this.$message.error('请求出错：' + error.message);
        });
    },
    handlePageChange(page) {
      this.currentPage = page;
      this.fetchAlarms();
    },
    formatTime(time) {
      return dayjs(time).format('YYYY-MM-DD HH:mm:ss');
    }
  }
};
</script>

<style scoped>
.alarm-list {
  padding: 20px;
}
</style>