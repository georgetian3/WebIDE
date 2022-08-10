<template>
  <div class="coding_page">
    <el-header style="text-align: right; font-size: 12px">
      <h1>filename</h1>
    </el-header>
    <el-container style="height: 500px; border: 1px solid #eee">
      <el-aside width="50px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1']">
          <el-menu-item index="1-1" class="el-icon-folder" style="height: 50px"></el-menu-item>
        </el-menu>
        <el-container>
        </el-container>
      </el-aside>
    </el-container>
  </div>
</template>

<script>
export default {

}
</script>

<style>
  * {
    text-align: center;
    font-size: medium;
  }
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }
  .el-icon-folder {
    font-size: larger;
  }
  h1 {
    /* font-weight: normal; */
    color: purple;
  }
</style>
