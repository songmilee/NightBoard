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

$(document).ready(function(){
    $('.sidenav').sidenav();
});

$(document).ready(function(){
  $('.datepicker').datepicker();
});