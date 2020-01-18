/*
 ╔╦╗╔═╗  ╔═╗┌─┐┬  ┬  ┌─┐┌─┐┌┬┐┌─┐┬─┐
  ║║╠═╝  ║  │ ││  │  ├┤ │   │ │ │├┬┘
 ═╩╝╩    ╚═╝└─┘┴─┘┴─┘└─┘└─┘ ┴ └─┘┴└─
*/
class Scenarist{
    constructor(){
    }

    register_story(x){
        /* Register all the actions for the scenarist items */
        $('.view_'+x).off().on('click', function(event){
            event.preventDefault();
            event.stopPropagation();
            var t_id = $(this).attr('id')
            $.ajax({
                url: x+'s/'+t_id+'/view',
                success: function(answer) {
                    $('#'+x+'_'+t_id).html(answer);
                    prepare_ajax();
                    rebootlinks();
                },
                error: function(answer){
                    console.log('ooops... on view '+x+' :(');
                }
            });
        });
        $('.hide_'+x).off().on('click', function(event){
            event.preventDefault();
            event.stopPropagation();
            var t_id = $(this).attr('id')
            $('#'+x+'_'+t_id).html('');
            prepare_ajax();
            rebootlinks();
        });
        $('.edit_'+x).off().on('click', function(event){
            event.preventDefault();
            event.stopPropagation();
            var t_id = $(this).attr('id')
            $.ajax({
                url: x+'s/'+t_id+'/edit',
                success: function(answer) {
                    $('#'+x+'_'+t_id).html(answer);
                    prepare_ajax();
                    rebootlinks();
                },
                error: function(answer){
                    console.log('ooops... on edit '+x+':(');
                }
            });
        });
        $('.'+x+'_update').off().on('click',function(event){
            event.preventDefault();
            event.stopPropagation();
            console.log("update");
            var owner = $(this).closest('div.storyarticle').attr('id');
            var id = $(this).closest('div.storyarticle').attr('id').split('_')[1];
            var form = $(this).closest('form');
            var formdata = form.serialize();
            var urlupdate = x+'s/'+id+'/edit';
            $.ajax({
                url: urlupdate,
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                data: formdata,
                dataType: 'json',
                success: function(answer) {
                    console.log('Success... ');
                    $('#'+owner).html(answer);
                    rebootlinks();
                    $('button#'+id+'.view_'+x).click();
                },
                error: function(answer) {
                    console.log('Error... ');
                    console.log(answer);
                },
            });
        });
        $('.add_'+x).off().on('click',function(event){
            event.preventDefault();
            event.stopPropagation();
            var id = $(this).parent('p').prop('className');
            console.log(id);
            //var form = $(this).closest('form');
            var urlupdate = x+'s/add';
            $.ajax({
                url: urlupdate,
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                data: {'id': id},
                dataType: 'json',
                success: function(answer) {
                    console.log('Success... ');
                    console.log(id);
                    //$('#'+id).html(answer);
                    rebootlinks();
                    //$('button#'+id+'.view_'+x).click();
                },
                error: function(answer) {
                    console.log('Error... ');
                    console.log(answer);
                },
            });
        });
    }

    doConnect(){
        this.register_story('epic');
        this.register_story('drama');
        this.register_story('act');
        this.register_story('event');
    }
}
