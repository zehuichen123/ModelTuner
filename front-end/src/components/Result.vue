<template>
  <div style="margin: auto; width: 600px">
    <h2>Result</h2>
    <h3 style="text-align: left">Trial {{curr_page}}</h3>
    <el-table
      :data="table_data"
      stripe
      style="width: 100%; margin-bottom: 40px;">
      <el-table-column
        prop="trial"
        label="Epoch">
      </el-table-column>
      <el-table-column
        prop="precision"
        label="Precision">
      </el-table-column>
      <el-table-column
        prop="recall"
        label="Recall">
      </el-table-column>
      <el-table-column
        prop="fscore"
        label="F1 Score">
      </el-table-column>
    </el-table>
    <el-pagination
      background
      layout="prev, pager, next"
      :total="total_size"
      :current-page="curr_page"
      :page-size="page_size"
      @current-change="update_page">
    </el-pagination>
  </div>
</template>

<script>
    export default {
      name: "Result",
      data(){
        return {
          curr_page: 1,
          total_size: 100,
          table_data: [{
            trial: 1,
            precision: 0.954,
            recall: 0.934,
            fscore: 0.995,
          },{
            trial: 2,
            precision: 0.954,
            recall: 0.934,
            fscore: 0.995,
          }],
          all_data: [],
          page_size: 5,
        }
      },
      methods:{
        update_page(num){
          console.log(num);
          this.curr_page = num;
          this.table_data = this.all_data.slice((this.curr_page-1) * this.page_size, this.curr_page * this.page_size);
        }
      },
      created() {
        let _self = this;
        _self.axios.get('/data').then(
          function(res){
            _self.all_data = res.data.data_list;
            _self.page_size = res.data.page_size;
            _self.total_size = _self.all_data.length;
            _self.update_page(1);
          }
        )
      }
    }
</script>

<style scoped>

</style>
