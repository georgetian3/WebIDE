<template>
  <div class="welcome">
    <el-row>
      <el-col :span="24">
        <div class="welcome">Welcome to our online IDE!</div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {

}
</script>

<style>
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

    font-family: 'Avenir', Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-align: center;
      color: red;
  }
</style>
