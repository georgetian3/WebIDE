<template>
  <div class="welcome">
    <el-row>
      <el-col :span="24">
        <div class="welcome">
          <p>
            <img src="../assets/vscode-logo.png" id="logopic">
          </p>
          <h2>Welcome to Pscode Online!</h2>
        </div>
      </el-col>
    </el-row>
    <el-container style="height: 500px; border: 1px solid #eee">
      <el-aside width="160px" style="background-color: rgb(238, 241, 246)">
        <el-scrollbar style="width:160px">
          <el-menu :default-openeds="['1']">
            <el-submenu index="1">
              <template slot="title"><i class="el-icon-message"></i>options</template>
              <el-menu-item-group>
                <el-menu-item index="1-1" class="el-icon-menu" id="createnew">
                  <el-button type="text" @click="dialogVisible = true">create new project</el-button>
                  <el-dialog title="Type In The Project Name" :visible.sync="dialogVisible" width="30%"
                    :before-close="handleClose">
                    <el-input v-model="input" id="pro_name" clearable></el-input>
                    <span slot="footer" class="dialog-footer">
                      <el-button @click="dialogVisible = false">取 消</el-button>
                      <el-button type="primary" @click="create_new">确 定</el-button>
                    </span>
                  </el-dialog>
                </el-menu-item>
                <el-menu-item index="1-2" class="el-icon-setting" id="settings">settings</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
          </el-menu>
        </el-scrollbar>
      </el-aside>

      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
            <el-menu-item index="1">all projects</el-menu-item>
            <el-menu-item index="2">my projects</el-menu-item>
          </el-menu>
        </el-header>

        <el-main>
          <el-table :data="tableData" stripe>
            <el-table-column prop="label" label="projects available"></el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
    <div id="footer">
      <p id="author">作者：陈俊哲、田正祺、孙冯元、梁烨</p>
      <p>联系方式：xxx@mails.tsinghua.edu.cn</p>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
export default {
  data () {
    const item = {
      label: 'try'
    }
    // return {
    //   tableData: Array(3).fill(item)
    // }
    return {
      resources: [],
      dialogVisible: false,
      input: '',
      tableData: Array(3).fill(item)
    }
  },
  mounted () {
    setInterval(() => {
      this.getData()
    }, 10000)
  },
  methods: {
    create_new: function () {
      var proName = document.getElementById('pro_name').value
      this.dialogVisible = false
      var data = {}
      data['action'] = 'create'
      data['name'] = proName
      var res = this.postData('http://127.0.0.1:5000/projects', data)
      console.log(res)
    },
    async postData (url = '', data = {}) {
      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      })
      return response.json()
    },
    getData: function () {
      var stats = {}
      stats['action'] = 'getall'
      var res = this.postData('http://127.0.0.1:5000/projects', stats)
      console.log(res)
      // console.log(Object.keys(res))
      // if (Object.keys(res) ==  '') {
      //   console.log('')
      // } else {
      //   this.tableData.fill(res.keys)
      // }
    }
  }
}
</script>

<style>
  * {
    text-align: center;
  }

  .el-header {
    background-color: rgb(200,200,200);
    color: #333;
    line-height: 61px;
    height: 61px !important;
  }

  .el-aside {
    color: #333;
    overflow: -moz-scrollbars-none;
  }
  .el-row {
    margin-bottom: 20px;
  }
  .el-col {
    border-radius: 4px;
  }

  .el-submenu__title{
    height: 40px;
    line-height: 46px;
    padding-left: 0px !important;
    width: 160px;
  }
  .el-menu-item-group__title{
    padding:0px;
  }
  body{
    position:absolute;
    width: 80%;
    left: 10%;
  }
  h2{
    margin-top:40px;
    margin-bottom: 20px;
    margin-left: 80px;
  }
  p{
    margin-block-start: 0px;
    margin-block-end: 0px;
  }
  #footer{
    margin: 0px;
    padding-top: 10px;
    position: relative;
    height: 20px;
    font-size: 12px;
    text-align: right;
    color: #6E6F6F;
    background-color: rgb(64,64,64);
}
  #logopic{
    position: absolute;
    left: 30px;
    top: 20px;
    z-index: 2;
    width:70px;
    float:left;
  }
  #pro_name{
    width: 80%;
  }
  #createnew{
    top:0px;
    float: left;
    padding-left: 10px !important;
    vertical-align: middle;
    padding-top:0px;
    padding-right: 0px;
    margin-bottom:10px;
    margin-left: 0px;
    margin-top: 0px;
    min-width: 160px;
    height: 36px;
    left:0px;
  }
  #settings{
    position: relative;
    float: left;
    top:-15px;
    padding-left: 0px !important;
    margin-left: 0px;
    padding-right: 0px;
    left: 0px;
    min-width: 160px;
    height:36px;
  }
  .el-submenu.is-opened>.el-submenu__title{
    background-color: rgb(218,218,218);
  }
  .welcome {
    background: rgb(35,35,35);
    min-height: 20px;
    font-size: 20px;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: rgb(224,224,224);
  }
</style>
