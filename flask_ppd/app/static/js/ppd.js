const base_url = "localhost:5000/";

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
   },
  methods : {
    addUser : function(event){

      name = document.querySelector("input[id=mem_name]").value;
      address = document.querySelector("input[id=mem_address]").value;
      birth = document.querySelector("input[id=mem_birth]").value;

      /**
       * Input 값 null 체크
       */
      if(!name){
        alert("이름을 채워주세요");
      } else if(!address){
        alert("주소를 채워주세요");
      } else if(!birth) {
        alert("생일을 입력해주세요.")
      }
      
      /**
       * 서버로 데이터 전송
       */
      if(name && address && birth){
        axios.post("/user", {
          'mem_name' :  name,
          'mem_address' : address,
          'mem_birth' : birth,
          'mem_sex' : this.mem_sex
        })
        .then(repsone => {
          console.log(repsone);
          alert(repsone);
        }).catch((err)=>{
          console.log(err);
        });
      }
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