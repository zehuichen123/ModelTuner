<template>
  <el-row>
    <el-col :span="4">
      <h2>Tuner</h2>
      <el-menu
        default-active="1"
        class="el-menu-vertical-demo"
        @select="set_index">
        <el-menu-item index="1">
          <i class="el-icon-setting"></i>
        </el-menu-item>
        <el-menu-item index="2">
          <i class="el-icon-document"></i>
        </el-menu-item>
        <el-menu-item index="3">
          <i class="el-icon-pie-chart"></i>
        </el-menu-item>
        <el-menu-item index="4">
          <i class="el-icon-headset"></i>
        </el-menu-item>
      </el-menu>
    </el-col>
    <el-col :span="20">
      <el-main>
        <Config_app v-if="num==='1'"></Config_app>
        <Result_app v-if="num==='2'"></Result_app>
        <Visual_app v-if="num==='3'"></Visual_app>
        <About_app v-if="num === '4'"></About_app>
      </el-main>
    </el-col>
  </el-row>
</template>

<script>
  import Config_app from "@/components/Config_app";
  import Result_app from "@/components/Result_app";
  import Visual_app from "@/components/Visual_app";
  import About_app from "@/components/About_app";

  export default {
    name: "Mobile",
    components:{About_app, Config_app, Result_app, Visual_app},
    data(){
      return {
        num: "1",
      }
    },
    methods: {
      set_index(key) {
        this.num = key;
      }
    }
  }
</script>

<style scoped>
</style>
