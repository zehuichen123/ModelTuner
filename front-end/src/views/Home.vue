<template>
  <el-row>
    <el-col :span="4">
      <h1>Tuner</h1>
      <div style="margin-top: 20px; margin-bottom: 20px;">@lovesnowbest</div>
      <el-menu
        default-active="1"
        class="el-menu-vertical-demo"
        @select="set_index">
        <el-menu-item index="1">
          <i class="el-icon-setting"></i>
          <span slot="title">Home</span>
        </el-menu-item>
        <el-menu-item index="2">
          <i class="el-icon-document"></i>
          <span slot="title">Result</span>
        </el-menu-item>
        <el-menu-item index="3">
          <i class="el-icon-pie-chart"></i>
          <span slot="title">Visual</span>
        </el-menu-item>
        <el-menu-item index="4">
          <i class="el-icon-headset"></i>
          <span slot="title">About</span>
        </el-menu-item>
      </el-menu>
    </el-col>
    <el-col :span="20">
      <el-main>
        <Config v-if="num==='1'"></Config>
        <Result v-if="num==='2'"></Result>
        <Visual v-if="num==='3'"></Visual>
        <about v-if="num === '4'"></about>
      </el-main>
    </el-col>
  </el-row>
</template>

<script>
    import Config from "@/components/Config";
    import Result from "@/components/Result";
    import Visual from "@/components/Visual";
    import About from "@/components/About";

    export default {
      name: "Home",
      components:{About, Config, Result, Visual},
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
