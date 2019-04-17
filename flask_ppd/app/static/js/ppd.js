var base_url = "localhost:5000/";

var app = new Vue({
    el: '#app',
    data:  {
      message: '안녕하세요 Vue!'
    }
  })

var navbar = new Vue({
    el : '#navbar',
    methods: {
        
    },
})

var user = new Vue({
  el : '#user',
  data : {
    mem_sex : '0',
    member : []
   },
  methods : {
    addUser : function(event){
      this.member.push({
          mem_name :  document.querySelector("input[id=mem_name]").value,
          mem_address : document.querySelector("input[id=mem_address]").value,
          mem_birth : document.querySelector("input[id=mem_birth]").value,
          mem_sex : this.mem_sex
      });
      console.log(this.member)
      axios.post(base_url+"user", this.member)
      .then(repsone => {
        console.log(repsone);
      }).catch((err)=>{
        console.log(err);
      });
    },

    cancelUser : function(event){
      document.querySelector("input[id=mem_name]").value=""
      document.querySelector("input[id=mem_address]").value=""
      document.querySelector("input[id=mem_birth]").value=""
      this.mem_sex = '1'

      alert("등록이 취소 되었습니다.")
    }
  }
})

$(document).ready(function(){
    $('.sidenav').sidenav();
});

$(document).ready(function(){
  $('.datepicker').datepicker({
    selectMonths: true,
    yearRange : 100,
    format : 'yyyy-m-dd'
  });
  
});