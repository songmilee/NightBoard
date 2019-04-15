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
    mem_name : '',
    mem_address : '',
    mem_birth : '',
    mem_sex : '0',
    posts : []
   },
  methods : {
    addUser : function(event){
      this.mem_name = document.querySelector("input[id=mem_name]").value
      this.mem_address = document.querySelector("input[id=mem_address]").value
      this.mem_birth = document.querySelector("input[id=mem_birth]").value


      fetch('https://jsonplaceholder.typicode.com/posts/1')
      .then((response)=>{
        if(response.ok){
          return response.json();
        }
        throw new Error('Network response was not ok')  
      })
      .then((json)=>{
        this.posts.push({
          userId : json.userId,
          title: json.title,
          body: json.body
        });
        console.log(this.posts)
      })
      .catch((error)=>{
        console.log(error);
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
  $('.datepicker').datepicker();
});