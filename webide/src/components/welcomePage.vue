<template>
  <div class="welcome">
    <el-row>
      <el-col :span="24">
        <div class="welcome">
          <p>
            <img src="../assets/vscode-logo.png" id="logopic">
          </p>
          <h2>Welcome to TSCode Online!</h2>
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
          <el-table :data="tableData" stripe :row-class-name="tableRowClassName" @row-contextmenu="rename"
            @row-click="jump">
            <el-table-column prop="label" label="projects available" class="table_column">
            </el-table-column>
            <el-table-column label="operations" width="130px">
              <template v-slot="scope">
                <el-button size="mini" type="rename" icon="el-icon-edit" @click.stop="dialogVisibleNew = true, changeRow(scope.row)">
                </el-button>
                <el-button size="mini" type="delete" icon="el-icon-delete" @click.stop="remove(scope.row)"></el-button>
              </template>
            </el-table-column>
          </el-table>
          <el-dialog title="Type In The New Project Name" :visible.sync="dialogVisibleNew" width="30%"
            :before-close="handleClose">
            <el-input v-model="input" id="new_name" @click.stop=""></el-input>
            <span slot="footer" class="dialog-footer">
              <el-button @click.stop="dialogVisibleNew = false">取 消</el-button>
              <el-button @click.stop="rename()">确 定</el-button>
            </span>
          </el-dialog>
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
    // const item = {
    //   label: 'try'
    // }
    // return {
    //   tableData: Array(3).fill(item)
    // }
    return {
      resources: [],
      dialogVisible: false,
      dialogVisibleNew: false,
      input: '',
      tableData: [],
      currentRow: 0
    }
  },
  created () {
    this.getData()
  },
  mounted () {
    setInterval(() => {
      this.getData()
    }, 10000)
  },
  methods: {
    nullsort (column) {
    },
    jump: function (row) {
      // let myURL = 'webide.georgetian.com:18080/?folder=/home/user/tscode/' + row['label']
      // let path = window.location.protocol + '//' + myURL
      // window.location.href = path
      window.alert('jump')
    },
    changeRow (row) {
      this.currentRow = row['index']
    },
    async rename () {
      this.dialogVisibleNew = false
      var newProName = document.getElementById('new_name').value
      var data = {}
      data['action'] = 'rename'
      data['old'] = this.tableData[this.currentRow]['label']
      data['new'] = newProName
      this.tableData[this.currentRow].label = newProName
      var res = this.postData('http://webide.georgetian.com:18081/projects', data)
      console.log(res)
    },
    async remove (row) {
      var numOfRow = row['index']
      const confirmRes = await this.$confirm('are you sure to delete this project?', '提示', {
        confirmButtonText: 'Yes',
        cancelButtonText: 'No'
      }).catch(err => err)
      if (confirmRes === 'cancel') {
        return this.$message.info('delete canceled!')
      } else if (confirmRes === 'confirm') {
        var data = {}
        data['action'] = 'delete'
        data['name'] = this.tableData[row.index].label
        var res = this.postData('http://webide.georgetian.com:18081/projects', data)
        console.log(res)
        this.tableData.splice(numOfRow, 1)
        return this.$message.info('delete completed!')
      }
    },
    // function for project creating
    create_new: function () {
      var proName = document.getElementById('pro_name').value
      for (var rowName in this.tableData) {
        // eslint-disable-next-line eqeqeq
        if (this.tableData[rowName]['label'] === proName) {
          this.dialogVisible = false
          return this.$message.info('you cannot have two projects with the same name!')
        }
      }
      this.dialogVisible = false
      var data = {}
      data['action'] = 'create'
      data['name'] = proName
      var res = this.postData('http://webide.georgetian.com:18081/projects', data)
      console.log(res)
      this.addProject(proName)
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
      var data = {}
      data['action'] = 'getall'
      var res = this.postData('http://webide.georgetian.com:18081/projects', data)
      res.then(stats => {
        var prolist = Object.keys(stats.data)
        console.log(this.tableData)
        if (prolist === '') {
          console.log('')
        } else {
          this.tableData = []
          for (var i = 0; i < prolist.length; i++) {
            this.addProject(prolist[i])
          }
        }
      })
    },
    addProject: function (proName) {
      let newProject = {}
      newProject.label = proName
      this.tableData.push(newProject)
    },
    tableRowClassName ({ row, rowIndex }) {
      row.index = rowIndex
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
  .table_column {
    text-align: left;
  }
</style>
