<template>
  <div style="margin: auto">
    <h3>Visualization</h3>
    <ve-line :data="chartData"></ve-line>
    <el-pagination
      background
      layout="prev, pager, next"
      :total="chartData.num_records"
      :page-size="1"
      :current-page="curr_page"
      @current-change="set_page">
    </el-pagination>
  </div>
</template>

<script>
  export default {
    name: "Visual_app",
    data: function () {
      return {
        curr_page: 1,
        chartData: {
          columns: ['Epoch', '1', '2', '3'],
          rows: [
            { 'Epoch': 0, '1': 4393, '2': 1093, '3': 0.32 },
            { 'Epoch': 1, '1': 3330, '2': 3230, '3': 0.26 },
            { 'Epoch': 2, '1': 2923, '2': 2623, '3': 0.76 },
            { 'Epoch': 3, '1': 1723, '2': 1423, '3': 0.49 },
            { 'Epoch': 4, '1': 3792, '2': 3492, '3': 0.323 },
            { 'Epoch': 5, '1': 4533, '2': 4293, '3': 0.78 }
          ],
          num_records: 4,
        },
      }
    },
    methods:{
      set_page(num){
        this.curr_page = num;
        let _self = this;
        _self.axios.get('/table/'+num.toString()).then(
          function (res) {
            _self.chartData = res.data;
          }
        )
      }
    },
    created() {
      let _self = this;
      _self.axios.get('/table/1').then(
        function (res) {
          _self.chartData = res.data;
        }
      )
    }
  }
</script>

<style scoped>

</style>
