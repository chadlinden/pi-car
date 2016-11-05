//-------------------------------------------------//
/*	Obligatory file header makes space up top		*/
//-------------------------------------------------//

Vue.http.headers.common['X-CSRF-TOKEN'] = document.querySelector('#csrf_token').getAttribute('value');

var app = new Vue({
	
	el: "#app",

	data: {
		jobCount: 0,
	},
	computed: {
	},
	ready: function(){
        this.getJobs();
	},
	methods: {
        getJobs: function()
        {
            this.$http.get('/api/find/scraper/id/all', function(data){
                this.jobCount = data;
            });
        }
	}
});
/*
function update() {
    setTimeout(function() {
        app.getJobs();
        update();
    }, 3000);
}
update();
*/