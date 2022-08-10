<template>
  <div class="welcome">
    <el-row>
      <el-col :span="24">
        <div class="welcome">Welcome to our online IDE!</div>
      </el-col>
    </el-row>
    <el-container style="height: 500px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1', '3']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>options</template>
            <el-menu-item-group>
              <el-menu-item index="1-1" class="el-icon-menu">create new project</el-menu-item>
              <el-menu-item index="1-2" class="el-icon-setting">settings</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-aside>

      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <!-- <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>查看</el-dropdown-item>
              <el-dropdown-item>新增</el-dropdown-item>
              <el-dropdown-item>删除</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <span>王小虎</span> -->
          <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
            <el-menu-item index="1">all projects</el-menu-item>
            <el-menu-item index="2">my projects</el-menu-item>
          </el-menu>
        </el-header>

        <el-main>
          <el-table :data="tableData">
            <el-table-column prop="label" label="projects available"></el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  // data () {
  //   const item = {
  //     date: '2016-05-02',
  //     name: '王小虎',
  //     address: '上海市普陀区金沙江路 1518 弄'
  //   }
  //   return {
  //     tableData: Array(20).fill(item)
  //   }
  // }
}
</script>

<style>
* {
  text-align: center;
}

.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}
  .el-row {
    margin-bottom: 20px;
  }
  .el-col {
    border-radius: 4px;
  }
  .welcome {
    background: #99a9bf;
    border-radius: 10px;
    min-height: 20px;
    font-size: 20px;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: red;
  }
</style>
