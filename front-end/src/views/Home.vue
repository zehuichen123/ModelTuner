<template>
  <div class="Home">
    <el-row>
      <el-button @click="go_pc" style="width: 200px !important; height: 50px; margin-top: 40vh">PC Version</el-button>
    </el-row>
    <el-row>
      <el-button @click="go_mobile" style="width: 200px !important; margin-top: 30px; height: 50px;">Mobile Version</el-button>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: "Home",
    methods: {
      go_pc(){
        this.$router.push({name:"PC"});
        console.log("abc");
      },
      go_mobile(){
        console.log('bff');
        this.$router.push({name: "Mobile"})
      }
    },
  };
</script>

<style scoped>
</style>
