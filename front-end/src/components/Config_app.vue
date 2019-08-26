<template>
  <div style="margin: auto;">
    <h3>Config for Model</h3>
    <el-form :label-position="labelPos" :model="form" size="small">
      <el-form-item class="small-margin" label="Layer Config">
        <el-input v-model="form.layer"></el-input>
      </el-form-item>
      <el-form-item class="small-margin" label="Epoch Num">
        <el-input v-model="form.epoch_num"></el-input>
      </el-form-item>
      <el-form-item class="small-margin" label="Learning Rate">
        <el-input v-model="form.lr"></el-input>
      </el-form-item>
      <el-form-item class="small-margin" label="Coef1">
        <el-input v-model="form.coef1"></el-input>
      </el-form-item>
      <el-form-item class="small-margin" label="Coef2">
        <el-input v-model="form.coef2"></el-input>
      </el-form-item>
      <el-form-item class="small-margin" label="K Component">
        <el-input v-model="form.K"></el-input>
      </el-form-item>
      <div style="margin-top: 20px;">
        <el-button type="primary" @click="startRun" :disabled="status">Start Trials</el-button>
        <el-button type="danger" @click="stopRun" :disabled="!status">Stop Trails</el-button>
      </div>
    </el-form>

  </div>
</template>

<script>
  export default {
    name: "Config_app",
    data(){
      return{
        labelPos: 'left',
        form : {
          layer: "120 60 30 10 1",
          epoch_num: "100",
          lr: "0.001",
          coef1: "1",
          coef2: "1",
          K: "3",
        },
        status: false,
      }
    },
    created(){
      let _self = this;
      _self.axios.get('/').then(
        function (res) {
          _self.status = res.data.status;
        }
      )
    },
    methods: {
      success_run() {
        this.$notify({
          title: 'Request Done!',
          message: '',
          type: 'success'
        });
      },
      bad_run() {
        this.$notify({
          title: 'Warning',
          message: 'Opps!',
          type: 'warning'
        });
      },
      error_run(error) {
        this.$notify({
          title: 'Error',
          message: error,
          type: 'error'
        });
      },
      startRun(){
        let _self = this;
        _self.axios.post('/start', _self.form)
          .then(function(res){
            if(res.status === 200){
              _self.success_run();
              _self.status = true;
            }
            else{
              _self.bad_run();
            }
          })
          .catch(function (error) {
            _self.error_run(error);
          })
      },
      stopRun(){
        let _self = this;
        _self.axios.get('/stop').then(
          function (res) {
            if(res.status === 200){
              _self.success_run();
              _self.status = false
            }
            else{
              _self.bad_run();
            }
          }).catch(function (error) {
            _self.error_run(error)
          }
        )
      }
    }
  }
</script>

<style scoped>
  .small-margin{
    margin-bottom: 4px !important;
  }
</style>
